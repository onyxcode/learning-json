import json

name = input("What's your name?\n")

age = input("What's your age?\n")

hobby = input("What's your hobby?\n")

x = {"name":name,"age":age,"hobby":hobby}

with open ('profile.json', 'w') as jsonTest:
  json.dump(x, jsonTest)

print("Profile written.")