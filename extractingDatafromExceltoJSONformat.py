import pandas as pd
import json

# Step 1: Read the Excel file
excel_file = pd.ExcelFile(r'C:\Users\Malhar\Desktop\BTECH CS\THIRD YEAR\MINI PROJECT - I\Student_Data.xlsx')

df = excel_file.parse(excel_file.sheet_names[0])

# Step 2: Convert the DataFrame to a JSON format
json_data = df.to_json(orient='records', lines=True)

# Step 3: Save the JSON data to a file (Optional)
with open('students_data.json', 'w') as json_file:
    json_file.write(json_data)

print("Data Successfully converted to JSON format.")

