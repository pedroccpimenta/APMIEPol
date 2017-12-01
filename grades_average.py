# Estatística básica sobre uma lista de números

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  print('Print Grades')
  for grade in grades_input:
    print (grade)
  return

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average=grades_average(scores)
  variance=0
  for x in scores:
    variance+=(average-x)**2
    
  variance=float(variance/float(len(scores)))
  print (type(variance))  
  return(variance)

print (grades_variance(grades))


def grades_std_deviation(variance):
  return (variance ** .5)


variance=grades_std_deviation(grades_variance(grades))


print (print_grades(grades))
print (grades_sum(grades))
print (grades_average(grades))
print (grades_variance(grades))
print ('Std Deviation:',grades_std_deviation(variance))
