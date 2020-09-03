import json

name = input("What's your name?\n")

age = input("What's your age?\n")

hobby = input("What's your hobby?\n")

x = {"name":name,"age":age,"hobby":hobby}

name = x["name"]

age = x["age"]

hobby = x["hobby"]

print(f"My name is {name}, I am {age} years old and I love {hobby}!")