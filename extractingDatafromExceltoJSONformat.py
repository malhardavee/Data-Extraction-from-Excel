import pandas as pd

# Step 1: Read the Excel file
excel_file = 'https://1drv.ms/x/s!AmRsz_agFuR2q26V2aZMu_0FpCy6?e=ANPgp1'
df = pd.read_excel(excel_file)

# Step 2: Convert the DataFrame to a JSON format
json_data = df.to_json(orient='records')

# Step 3: Save the JSON data to a file (Optional)
with open('students_data.json', 'w') as json_file:
    json_file.write(json_data)

print("Data Successfully converted to JSON format.")
