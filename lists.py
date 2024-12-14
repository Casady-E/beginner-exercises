my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0]) #prints 1
print(my_list[1])
print(my_list[2])

#prints out 1,2,3
for x in my_list:
    print(x)

#does not work
# mylist = [1,2,3]
# print(mylist[10])


# Exercise
numbers = [1, 2, 3]
strings = ["Hello World"]
names = ["John", "Eric", "Jessica"]

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)