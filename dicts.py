user = {"name": "Manar", "age": 25}

print(user["name"])
print(user.get("email", "no email"))

for key, value in user.items():
    print(key, "=", value)