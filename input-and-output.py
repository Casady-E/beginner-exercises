# Prints out the input received from stdin
astring=input()# give hello as input
print(input())

#num=int(input())
#print (num)
decimalnum=input()
decimalnum=float(input())
print(decimalnum)

#give two integers in first line and more than two integers in third line
a, b = map(int, input().split())
array = input().split()
sum = 0
for each in array:
    sum = sum + int(each)
print(a, b, sum)  # prints first two integers from first line and sum of integers of second line

a = 5
b = 0.63
c = "hello"
print ("a is : {}, b is {},c is {}".format(a,b,c))

#Exercise

# Taking the name input using input()
name = input("Enter your name: ")

# Taking the age input using input() and converting it to integer
age = int(input("Enter your age: "))

# Taking the country input using input()
country = input("Enter your country: ")

# Displaying the formatted sentence with name, age, and country
print("Hello, my name is {}, I am {} years old, and I am from {}.".format(name, age, country))