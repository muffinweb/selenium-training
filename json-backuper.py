import json

load_backup = open("backup.json", "r")
backup_content = load_backup.read()
load_backup.close()
jsonBackup = json.loads(backup_content)

newDatas = [
    {
        "name": "Savas",
        "age": "35"
    },
    {
        "name": "Tulay",
        "age": "36"
    }
]

for item in newDatas:
    data.append(item)

jsonData = json.dumps(data)


open("backup.json", "w").write(jsonData)
print("Done successfully")
