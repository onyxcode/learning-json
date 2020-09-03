import json
import jsonWrite

jsonWrite

with open ('profile.json', 'r', encoding='utf-8') as profile:
  prf = json.load(profile)
  print(f"Your name is {prf['name']}.\nYou are {prf['age']} years old.\nYour hobby is {prf['hobby']}.")