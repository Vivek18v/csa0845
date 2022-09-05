#author: v.vivek.
#program name:reverse a word.
#date:05/09/2022.
def reverse(a):
	str = ""
	for i in a:
		str = i + str
	return str

a = "145*999=144855"

print(" original string is : ", end="")
print(a)

print(" reverse string(using loops) is : ", end="")
print(reverse(a))
