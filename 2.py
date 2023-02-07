age = input("введите возраст")
age = int(age)

if 11 <= age % 100 == 19:
  print(f"вам{age} лет")
elif age <= 10 == 1:
  print(f"вам{age}год")
elif 2 <= age % 10 <= 4:
  print(f"вам{age}года")
elif 5 <= age % 10 <= 9 or age % 10 == 0:
  print(f"вам{age}лет")