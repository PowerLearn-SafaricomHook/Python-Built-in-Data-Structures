
#step 1: Create an empty list called my_list
my_list = []

#sep 2: append the elemets 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# print(my_list)

#step 3: Insert te value 15 at the second positon (index 1)

my_list.insert(1,15)

# print(my_list)

#Step 4 : Extend my_list with another list [5,60,70,80]

my_list.extend([50,60,70,80])

# print(my_list)

# step 5 : Remove the last element from my_list

my_list.pop()

# print(my_list)

#step 6 :Sort my_list in asceding order

my_list.sort()

# print(my_list)

#step 7 : Find and print the index of the value 30

index_of_30 = my_list.index(30)

# print("index of 30:",index_of_30)

#Print the final my_list to verify

print("Final List",my_list)