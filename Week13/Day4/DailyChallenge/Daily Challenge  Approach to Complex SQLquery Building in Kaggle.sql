import sqlite3
import pandas as pd
from IPython.display import display

# ==============================================================================
# 1. LOAD AND EXPLORE THE DATA
# ==============================================================================
# Connect to the IPL SQLite database
# (Adjust path to '/kaggle/input/indian-premier-league-sqlite/database.sqlite' if running on Kaggle)
db_path = 'database.sqlite'
conn = sqlite3.connect(db_path)

# Load sqlite_master to inspect all tables in the database
print("--- Step 1: Database Master Table (All Tables) ---")
df_tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
display(df_tables)

# Load each user table (excluding binary sysdiagrams) and print its column names to identify common keys
print("\n--- Table Schemas & Common Columns ---")
for table_name in df_tables['name']:
    if table_name not in ('sysdiagrams', 'sqlite_sequence'):
        cols_df = pd.read_sql_query(f"PRAGMA table_info({table_name});", conn)
        print(f"{table_name:<18} -> {cols_df['name'].tolist()}")


# ==============================================================================
# 2. QUERY 1: SELECT ALL COLUMNS FROM PLAYER_MATCH TABLE
# ==============================================================================
# Explanation: Selects all columns from the Player_Match table to inspect how
# players (Player_Id) are linked to matches (Match_Id), roles (Role_Id), and teams (Team_Id).
print("\n--- Query 1: Player_Match Table (First 10 Rows) ---")
sql_q1 = '''
SELECT * 
FROM Player_Match;
'''
df_q1 = pd.read_sql_query(sql_q1, conn)
display(df_q1.head(10))


# ==============================================================================
# 3. QUERY 2: BATSMAN VS RUNS
# ==============================================================================
# Explanation: Joins Ball_by_Ball, Batsman_Scored, and Player on the composite
# delivery key (Match_Id, Over_Id, Ball_Id, Innings_No) to sum total career runs per striker.
print("\n--- Query 2: Total Runs Scored by Each Batsman (Top 15) ---")
sql_q2 = '''
SELECT 
    b.Striker AS Player_Id,
    p.Player_Name,
    SUM(bs.Runs_Scored) AS Total_Runs
FROM Ball_by_Ball b
JOIN Batsman_Scored bs 
    ON b.Match_Id = bs.Match_Id 
   AND b.Over_Id = bs.Over_Id 
   AND b.Ball_Id = bs.Ball_Id 
   AND b.Innings_No = bs.Innings_No
JOIN Player p 
    ON b.Striker = p.Player_Id
GROUP BY b.Striker, p.Player_Name
ORDER BY Total_Runs DESC;
'''
df_q2 = pd.read_sql_query(sql_q2, conn)
display(df_q2.head(15))


# ==============================================================================
# 4. QUERY 3: FIFTIES AND HUNDREDS
# ==============================================================================
# Explanation: First aggregates runs scored by each batsman per match in a CTE,
# then counts how many times a player scored 50-99 runs (Fifties) and >= 100 runs (Hundreds).
print("\n--- Query 3: Fifties and Hundreds Scored by Each Batsman (Top 15) ---")
sql_q3 = '''
WITH batsman_match_runs AS (
    SELECT 
        b.Striker AS Player_Id,
        b.Match_Id,
        SUM(bs.Runs_Scored) AS Runs_In_Match
    FROM Ball_by_Ball b
    JOIN Batsman_Scored bs 
        ON b.Match_Id = bs.Match_Id 
       AND b.Over_Id = bs.Over_Id 
       AND b.Ball_Id = bs.Ball_Id 
       AND b.Innings_No = bs.Innings_No
    GROUP BY b.Striker, b.Match_Id
)
SELECT 
    bmr.Player_Id,
    p.Player_Name,
    SUM(CASE WHEN bmr.Runs_In_Match >= 50 AND bmr.Runs_In_Match < 100 THEN 1 ELSE 0 END) AS Fifties,
    SUM(CASE WHEN bmr.Runs_In_Match >= 100 THEN 1 ELSE 0 END) AS Hundreds
FROM batsman_match_runs bmr
JOIN Player p 
    ON bmr.Player_Id = p.Player_Id
GROUP BY bmr.Player_Id, p.Player_Name
ORDER BY Hundreds DESC, Fifties DESC;
'''
df_q3 = pd.read_sql_query(sql_q3, conn)
display(df_q3.head(15))


# ==============================================================================
# 5. QUERY 4: BEST BOWLING FIGURES
# ==============================================================================
# Explanation: Calculates wickets taken and runs conceded by each bowler per match.
# Note on Cricket Rules in this Schema:
# - Bowler-credited wickets exclude 'run out' (3), 'retired hurt' (5), and 'obstructing the field' (9),
#   so we filter Kind_Out IN (1, 2, 4, 6, 7, 8).
# - Bowler runs conceded include Batsman_Scored + wides (Extra_Type_Id = 2) and noballs (Extra_Type_Id = 4).
# Uses ROW_NUMBER() to rank each bowler's best single-match performance (most wickets, fewest runs conceded).
print("\n--- Query 4: Best Bowling Figures for Each Bowler (Top 15) ---")
sql_q4 = '''
WITH bowler_match_stats AS (
    SELECT 
        b.Bowler AS Player_Id,
        b.Match_Id,
        COUNT(CASE WHEN wt.Kind_Out IN (1, 2, 4, 6, 7, 8) THEN 1 END) AS Wickets_In_Match,
        SUM(
            COALESCE(bs.Runs_Scored, 0) + 
            CASE WHEN er.Extra_Type_Id IN (2, 4) THEN er.Extra_Runs ELSE 0 END
        ) AS Runs_Conceded_In_Match
    FROM Ball_by_Ball b
    LEFT JOIN Batsman_Scored bs 
        ON b.Match_Id = bs.Match_Id 
       AND b.Over_Id = bs.Over_Id 
       AND b.Ball_Id = bs.Ball_Id 
       AND b.Innings_No = bs.Innings_No
    LEFT JOIN Extra_Runs er 
        ON b.Match_Id = er.Match_Id 
       AND b.Over_Id = er.Over_Id 
       AND b.Ball_Id = er.Ball_Id 
       AND b.Innings_No = er.Innings_No
    LEFT JOIN Wicket_Taken wt 
        ON b.Match_Id = wt.Match_Id 
       AND b.Over_Id = wt.Over_Id 
       AND b.Ball_Id = wt.Ball_Id 
       AND b.Innings_No = wt.Innings_No
    GROUP BY b.Bowler, b.Match_Id
),
ranked_bowling AS (
    SELECT 
        Player_Id,
        Wickets_In_Match,
        Runs_Conceded_In_Match,
        ROW_NUMBER() OVER (
            PARTITION BY Player_Id 
            ORDER BY Wickets_In_Match DESC, Runs_Conceded_In_Match ASC
        ) AS rn
    FROM bowler_match_stats
)
SELECT 
    rb.Player_Id,
    p.Player_Name,
    rb.Wickets_In_Match AS Best_Wickets,
    rb.Runs_Conceded_In_Match AS Best_Runs_Conceded,
    rb.Wickets_In_Match || '/' || rb.Runs_Conceded_In_Match AS Best_Bowling_Figures
FROM ranked_bowling rb
JOIN Player p 
    ON rb.Player_Id = p.Player_Id
WHERE rb.rn = 1
ORDER BY rb.Wickets_In_Match DESC, rb.Runs_Conceded_In_Match ASC;
'''
df_q4 = pd.read_sql_query(sql_q4, conn)
display(df_q4.head(15))


# ==============================================================================
# 6. QUERY 5: COMPREHENSIVE CAREER METRICS
# ==============================================================================
# Explanation: Combines all previous building blocks (matches played, total runs,
# highest score, fifties, hundreds, total wickets, and best bowling figures)
# into a single unified career profile table for all IPL players.
print("\n--- Query 5: Comprehensive Career Metrics for IPL Players (Top 20) ---")
sql_q5 = '''
WITH matches_played AS (
    SELECT 
        Player_Id,
        COUNT(DISTINCT Match_Id) AS Matches_Played
    FROM Player_Match
    GROUP BY Player_Id
),
batsman_match_runs AS (
    SELECT 
        b.Striker AS Player_Id,
        b.Match_Id,
        SUM(bs.Runs_Scored) AS Runs_In_Match
    FROM Ball_by_Ball b
    JOIN Batsman_Scored bs 
        ON b.Match_Id = bs.Match_Id 
       AND b.Over_Id = bs.Over_Id 
       AND b.Ball_Id = bs.Ball_Id 
       AND b.Innings_No = bs.Innings_No
    GROUP BY b.Striker, b.Match_Id
),
batting_career AS (
    SELECT 
        Player_Id,
        SUM(Runs_In_Match) AS Total_Runs,
        MAX(Runs_In_Match) AS Highest_Score,
        SUM(CASE WHEN Runs_In_Match >= 50 AND Runs_In_Match < 100 THEN 1 ELSE 0 END) AS Fifties,
        SUM(CASE WHEN Runs_In_Match >= 100 THEN 1 ELSE 0 END) AS Hundreds
    FROM batsman_match_runs
    GROUP BY Player_Id
),
bowler_match_stats AS (
    SELECT 
        b.Bowler AS Player_Id,
        b.Match_Id,
        COUNT(CASE WHEN wt.Kind_Out IN (1, 2, 4, 6, 7, 8) THEN 1 END) AS Wickets_In_Match,
        SUM(
            COALESCE(bs.Runs_Scored, 0) + 
            CASE WHEN er.Extra_Type_Id IN (2, 4) THEN er.Extra_Runs ELSE 0 END
        ) AS Runs_Conceded_In_Match
    FROM Ball_by_Ball b
    LEFT JOIN Batsman_Scored bs 
        ON b.Match_Id = bs.Match_Id 
       AND b.Over_Id = bs.Over_Id 
       AND b.Ball_Id = bs.Ball_Id 
       AND b.Innings_No = bs.Innings_No
    LEFT JOIN Extra_Runs er 
        ON b.Match_Id = er.Match_Id 
       AND b.Over_Id = er.Over_Id 
       AND b.Ball_Id = er.Ball_Id 
       AND b.Innings_No = er.Innings_No
    LEFT JOIN Wicket_Taken wt 
        ON b.Match_Id = wt.Match_Id 
       AND b.Over_Id = wt.Over_Id 
       AND b.Ball_Id = wt.Ball_Id 
       AND b.Innings_No = wt.Innings_No
    GROUP BY b.Bowler, b.Match_Id
),
bowling_career AS (
    SELECT 
        Player_Id,
        Wickets_In_Match || '/' || Runs_Conceded_In_Match AS Best_Bowling_Figures,
        SUM(Wickets_In_Match) OVER (PARTITION BY Player_Id) AS Total_Wickets,
        ROW_NUMBER() OVER (
            PARTITION BY Player_Id 
            ORDER BY Wickets_In_Match DESC, Runs_Conceded_In_Match ASC
        ) AS rn
    FROM bowler_match_stats
)
SELECT 
    p.Player_Id,
    p.Player_Name,
    COALESCE(mp.Matches_Played, 0) AS Matches_Played,
    COALESCE(bat.Total_Runs, 0) AS Total_Runs,
    COALESCE(bat.Highest_Score, 0) AS Highest_Score,
    COALESCE(bat.Fifties, 0) AS Fifties,
    COALESCE(bat.Hundreds, 0) AS Hundreds,
    COALESCE(bwl.Total_Wickets, 0) AS Total_Wickets,
    COALESCE(bwl.Best_Bowling_Figures, 'N/A') AS Best_Bowling_Figures
FROM Player p
LEFT JOIN matches_played mp 
    ON p.Player_Id = mp.Player_Id
LEFT JOIN batting_career bat 
    ON p.Player_Id = bat.Player_Id
LEFT JOIN bowling_career bwl 
    ON p.Player_Id = bwl.Player_Id AND bwl.rn = 1
ORDER BY Total_Runs DESC, Total_Wickets DESC;
'''
df_q5 = pd.read_sql_query(sql_q5, conn)
display(df_q5.head(20))