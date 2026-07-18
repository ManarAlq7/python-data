import json

text = '{"name": "Manar", "skills": ["python", "git"]}'
data = json.loads(text)

print(data["name"])
print(data["skills"][0])
print(json.dumps(data))