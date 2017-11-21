# exemplo de codeacademy
# Pedro Pimenta, Nov. 2017

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
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

# Add your function below!
def average(numbers):
	total=float(sum(numbers))
	return float(total/len(numbers))

def get_average(student):
  homework=average(student["homework"])
  quizzes=average(student['quizzes'])
  tests=average(student['tests'])
  return .1*homework+.3*quizzes+.6*tests

def get_letter_grade(score):
  if score >= 90.:
    return "A"
  elif score >= 80.:
    return "B"
  elif score >= 70.:
    return "C"
  elif score >= 60.:
  	return "D"
  else:
    return "F"


def get_class_average(class_list):
  results=[]
  for student in class_list:
    r=get_average(student)
    results.append(r)
    print (results)
    print ("average:",average(results))
    
  return average(results)
    
    
class_list=[lloyd, alice, tyler]
print (class_list)
get_class_average(class_list)

get_class_average([alice, lloyd])
