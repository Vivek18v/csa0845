def reverse(a):
	num = ""
	for i in a:
		num = i + num
	return num

a = "AD1947"

print(" original number is : ", end="")
print(a)

print(" reverse number(using loops) is : ", end="")
print(reverse(a))
