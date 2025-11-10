friends = ["Amit", "Sara", "John", "Riya", "Karan"]
birthdays = {}

for friend in friends:
    date = input("Enter birthday of " + friend + ": ")
    birthdays[friend] = date

print("---- Birthdays ----")
for name in birthdays:
    print(name, ":", birthdays[name])
