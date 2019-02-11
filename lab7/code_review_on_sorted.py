student_scores = {
  'Ivan': 5.00,
  'Alex': 3.50,
  'Maria': 5.50,
  'Georgy': 5.00
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sort dictionary by key, using custom function (default syntax)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# in 'item' sorted will pass the (key, value) tuple returned from student_scores.items()
def sort_by_key(item):
  return item[0]

# sort dictionary by value, using custom function
def sort_by_value(item):
  return item[1]

print(sorted(student_scores.items(), key=sort_by_key))
print(sorted(student_scores.items(), key=sort_by_value), '\n')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sort dictionary by key, using custom function (lambda syntax)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(sorted(student_scores.items(), key=lambda item:item[0]))
print(sorted(student_scores.items(), key=lambda item:item[1]), '\n')

