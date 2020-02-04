
def main():
	first=input("Enter the first number:")
	second=input("Enter the second number:")

	if(first.isdigit() and second.isdigit()):
		opr=input("Choose the operation(+,-,/,*)")
		if (opr=="+"):
			print("The answer is",int(first)+int(second))
		elif(opr=="-"):
			print("The answer is",int(first)-int(second))
		elif(opr=="/"):
			print("The answer is",int(first)/int(second))
		elif(opr=="*"):
			print("The answer is",int(first)*int(second))
		else:
			print("Operation is not valid")
	else:
		print("Not a number!")

	#write your code here
	pass




if __name__ == '__main__':
	main()
