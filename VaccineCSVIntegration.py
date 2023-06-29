import csv
import json

# Define the input and output file names
input_file = 'VaccineOverview.csv'
dictionary = 'dictionary.json'
output_file = 'Output.csv'
output_rows = []
vaccineDef = []
vaccineDictDef = []
codeDef = []

# Opening JSON file
k = open(dictionary)
jsonData = json.load(k)

for i in range(0, 63):
    r = i * 2  # Getting an index that makes sense to the json
    vaccineDef.append(jsonData['vaccineTable'][r])
    vaccineDictDef.append(jsonData['vaccineTable'][r + 1]['vaccineDict'])
    codeDef.append(jsonData['vaccineTable'][r + 1]['codeDict'])

# Read the input CSV file and transform the Data
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    # for all rows, loop through the Employee/Student ID's
    for row in reader:
        id_number = row['Employee/Student ID']
        # append output if date != null
        for i in range(0, len(vaccineDef)):
            vaccine = vaccineDef[i]
            # If row = null, skip
            if row[vaccine] == '':
                continue
            output_rows.append({
                'Employee/Student ID': id_number,
                'vaccine': vaccine,
                'Date of Vaccine': row[vaccine],
                'Mapped Vaccine': vaccineDictDef[i],
                'Code': codeDef[i]
            })

with open(output_file, 'w', newline='') as f:
    fieldnames = [
        'Employee/Student ID',
        'vaccine',
        'Date of Vaccine',
        'Mapped Vaccine',
        'Code'
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_rows)

print(f"CSV file '{output_file}' has been generated.")
k.close()