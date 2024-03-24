import pandas as pd
import json

data = pd.read_csv('./../QUESTIONSCSV.csv')

dataJson = {}

def parseDataJsonId(id):
    idData = {}

    if id[0] == "M":
        idData["level"] = "Middle School"
    if id[0] == "H":
        idData["level"] = "High School"

    idData["set"] = f"Set {id[3]}"
    idData["round"] = f"Round {id[5]}"

    if id[6] == "T":
        idData["level"] = "Tossup"
    if id[6] == "B":
        idData["type"] = "Bonus"

    if id[7] == "0":
        idData["question"] = id[8]
    else:
        idData["question"] = id[7]+id[8]

    qT = id[9]+id[10]

    if qT == "LS":
        idData["question type"] = "Life Science"
    elif qT == "PS":
        idData["question type"] = "Physical Science"
    elif qT == "ES":
        idData["question type"] = "Earth Science"
    elif qT == "MA":
        idData["question type"] = "Math"
    elif qT == "GS":
        idData["question type"] = "General Science"
    elif qT == "PS":
        idData["question type"] = "Physical Science"

    qAT = id[11]+id[12]

    if qAT == "SA":
        idData["Question Answer Type"] = "Short Answer"
    elif qAT == "MC":
        idData["Question Answer Type"] = "Multiple Choice"

    return idData

def convertStrListToList(strList):
    return json.loads(strList)

for index, row in data.iterrows():
    qT = {}

    qT['info'] = parseDataJsonId(row['QID'])
    qT['question'] = row['Ques']
    qT['answerOpts'] = convertStrListToList(row['AnsOp'])
    qT['answer'] = row['Ans']

    dataJson[row['QID']] = qT

# File path
file_path = './../QUESTIONSJSON.json'

# Try loading the JSON file
try:
    with open(file_path, 'r') as json_file:
        fileData = json.load(json_file)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON in '{file_path}'.")
    exit()

# Update the dictionary with new data
fileData.update({"questions":dataJson})

# Write the updated dictionary back to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(fileData, json_file, indent=4)

print("JSON file updated successfully.")