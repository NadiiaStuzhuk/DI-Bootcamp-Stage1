import json

# Define the input JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Parse the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Step 2: Access and print the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Step 3: Add the "birth_date" key to the "employee" dictionary
data["company"]["employee"]["birth_date"] = "1995-04-12"

# Step 4: Save the modified dictionary into a JSON file
file_path = "modified_employee.json"
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Successfully updated JSON and saved to '{file_path}'.")