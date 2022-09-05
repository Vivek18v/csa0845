#author: v.vivek.
#program name:reverse a word.
#date:05/09/2022.
num1 = 1101
num2 = 1011
num3 = 1001



if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
