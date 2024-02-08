'Write a Python function to sum all the numbers in a list.'

def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [1,2,3,4,5]
print ("The sum of my_list is", sum_of_list(my_list))
