lloyd = {
  "name": "Lloyd",
  "homework": [2, 2, 2, 2],
  "quizzes": [],
  "tests": [23, 55, 76, 120]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]


for student in students:
  homework = student["homework"]
  print(student["name"], "has the following homework" , homework)
  number = len(homework)
  print("# of Homeworks = " + str(number))
  total = 0
  total = sum(homework)
  print("Sum of homework average = " + str(total))
  average = total / number 
  print(int(average))

reqeust = input("tell me what item you want to see the averge for by typing one of the following homework, quizzes, tests >> ")
request = str(request)

