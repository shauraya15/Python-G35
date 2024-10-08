#Example 1: Create a list of programming languages

#Declaration of list
langs = []
#for adding elements/data to the list: append(data)
#syntax: list_name.append(data)
#Work: helps to store/add data at the end of list.

# print("Before adding elements:", langs)

#Initialization/assignment of list
# langs.append("Python")
# langs.append("Java")
# langs.append("C")
# langs.append("C++")
# langs.append("Javascript")

# print("After adding elements:", langs)

#Initialization at the time Declaration?
#to add/store data to the list explicitly then you can add by comma

# names = ["Bob", "Prince", "Tannu", "Pawan"]

# print(names)

#How to access the data from the list?
#Note: list follows 0 based indexing which means first element is at index 0 and so on.

#To access the element inside the list, you must know about index of the element.
#Note: python list also follows -ve indexing meaning that the last of the list is always at -1
#Syntax: list_name[index]

# names = ["Bob", "Prince", "Tannu", "Pawan", "Sohan"]

# print(names[1]) #Prince
# print(names[3]) #Pawan

# print(names[-1]) #Pawan
# print(names[-2]) #Tannu

#Let's access the element using loop:

#Note: list is a sequnece type of data type.

#Without using range function
# for i in names:
#     print(i)


#With using range function
# for i in range(4):
#     print(names[i])

#To Run loop dynamically on any list, it is super important to know the total element inside list in term of range() function

#How will you know about the total element inside the list?
#Solution: len(list_name): help to give you length/number of element inside the list.

# print(len(names)) #5

# names = ["Bob", "Prince", "Tannu", "Pawan", "Sohan"]

# for i in range(len(names)):
#     print(names[i], end=" ")

#Example 1: Given list of number, your task is to print sequre of each number.

# nums = [1,2,3,4,5,6,7,8,9,10]

# for i in nums:
#     print(i**2, end=" ")

#Example 1: Given list of number, your task is to print sequre of even number number.

# for i in nums:
#     if i%2==0:
#         print(i**2, end=" ")

#Example 3: Given list of number, your task is to print factorial of each number.

# nums = [1,2,3,4,5,6,7,8,9,10]

# for i in nums:
#     # logic for factorial number
#     fact = 1
#     for j in range(1,i+1):
#         fact*=j
#     print(f"Factorial of {i} is {fact}")

#Example 4: Given number list, you need to find out the odd number and put them in seperate list.

# nums = [1,2,3,4,5,6,7,8,9,10]

# OddNumbers = []

# for i in nums:
#     if i%2!=0:
#         OddNumbers.append(i)

# print(OddNumbers)

#Example 5: Given number list, you need to find out the cube of each number and put them in seperate list.

#Exmaple 6: Given Two List one for names of the person and second for their cities, your task is to print the output in the following manner.

#Prince----"Noida"

# names = ["Pawan", "Deepak", "Mahi", "Rohan", "Rohit"]
# cities = ["Noida", "Delhi", "Chandigarh", "Rajpura", "Gurugram"]

# for i in range(len(names)):
#     print(names[i],"----", cities[i])


#Other functions of list:

#insert(index, data): to add element in list at specefic index.

# cities = ["Noida", "Delhi", "Chandigarh"]

# cities.insert(2, "Gurugram")
# cities.insert(0, "Bhopal")

# print(cities)

#Conclusion: List is the best choice according to the following points:

#1. List is the best choice you're using it for traversing/updating/searching/visiting each element.
#2. List is the best choice if you're using it for same type of data not for different type.

# names = ["Rakesh", "Sahil", "Mahi"]
# ages = [23, 18, 28]
# maritalStatus= [True, False,False]
# cities = ["Noida", "Dlehi", "Gurugram"]

#or

# person = ["Rakesh", 23, True, "Noida", "Sahil", 18, False, "Delhi", "Mahi", 28, False, "Gurugram"]

#Find out the age of Rakesh
#To find out the age of Rakesh first you need to filter the proper data.

# person = ["Rakesh", 23, True, "Noida", "Sahil", 18, False, "Delhi", "Mahi", 28, False, "Gurugram"]

# #Extra Work
# names = []
# for i in range(0, len(person), 4):
#     names.append(person[i])
# print(names)

# ages = []
# for i in range(1, len(person), 4):
#     ages.append(person[i])
# print(ages)

# meritalStatus = []
# for i in range(2, len(person), 4):
#     meritalStatus.append(person[i])
# print(meritalStatus)

# cities = []
# for i in range(3, len(person), 4):
#     cities.append(person[i])
# print(cities)


# #Real Logic
# for i in range(len(names)):
#     if names[i] =="Rakesh":
#         print("Age of Rakesh",ages[i])

#3. List is the bad choice, if your frequent operation is adding and deleting at specefic index.

#Example: Addition

numbers = [1,2,3,4,5]

#Add 10 at index 1
#insert(index, data)
#Syntax: listName.insert(index, data)
# numbers.insert(1, 10)
# print(numbers) # [1,10,2,3,4,5]

#Example: Delition

# numbers = [1,2,3,4,5]
#Delete element at index 2

#NOte: in above Example as well there will be lots of shifting will happen.

#Assingment:
#Problem 1: delete element at particular index.
#Problem 2: add element at particular index without insert()


#Good Example 1: Take input for numbers from user and add to the list.

# numList = []
# num = int(input("Enter Numbers: "))
# numList.append(num)

# print(numList)

# numList = []

# #taking input for numList
# while True:
#     num = int(input("Enter Numbers: "))
#     numList.append(num)

#     res = input("Do you want to add more numbers(Y/N): ")
#     if res =='N' or res=='n':
#         print("Current List: ",numList)
#         break

# #for operation on numList

# print("Welcome to My Applicaiton")
# while True:
#     print("1. Sum of All Numbers")
#     print("2. Average of All Numbers")
#     print("3. List Even Numbers")
#     print("4. List Odd Numbers")
#     print("5. Sum of Even Numbers")
#     print("6. Sum of Odd Numbers")
#     print("7. Exit")
#     choice = int(input("Enter Your Choice: "))

#     if choice==1:
#         #logic of sum of all numbers
#         sum = 0
#         for num in numList:
#             sum+=num
#         print("Sum of All Numbers: ",sum)
#     elif choice==2:
#         #logic for average of all numbers
#         sum = 0
#         for num in numList:
#             sum+=num
#         print("Average of All Numebrs: ",sum/len(numList))
#     elif choice ==3:
#         #logic for list all even numbers
#         print("Even Numbers: ", end='')
#         for num in numList:
#             if num%2==0:
#                 print(num, end=" ")
#         print()
#     elif choice ==4:
#         #logic for list all odd numbers
#         print("Odd Numbers: ", end='')
#         for num in numList:
#             if num%2!=0:
#                 print(num, end=" ")
#         print()

#     elif choice ==5:
#          #sum of all even numbers
#         evenSum = 0
#         for num in numList:
#             if num%2==0:
#                 evenSum+=num
#         print("Sum of Even Numbers: ",evenSum)
#     elif choice == 6:
#         #sum of all odd numbers
#         oddSum = 0
#         for num in numList:
#             if num%2!=0:
#                 oddSum+=num
#         print("Sum of Odd Numbers: ",oddSum)
#     elif choice == 7:
#         res = input("Do you want to exit(Y/N): ")
#         if res=='Y' or res =='y':
#             print("Thank you for using applicaiton!")
#             break
#     else:
#         print("Invalid Choice")





