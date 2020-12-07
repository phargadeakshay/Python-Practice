#import sys


#
# print("print version")
# print(sys.version)
# print("version info")
# print (sys.version_info)


# time print karnayasti
# import datetime
# time_sang = datetime.datetime.now()
# print("time aahe: ")
# print(time_sang.strftime("%d-%m-%y %H:%M:%S"))


# Area of a Circle
# from math import pi
# r = float(input("Enter The Value of redius "))
# area = pi*r**2
# print(f"Area Of Circle With Redius + {r} + is: + {area}")

# Nane ulata karne
# fname=(input("Enter Your First Name"))
# lname=(input("Enter Your Last Name"))
# print(f"Hellow {lname} {fname}")

# Generate a list and tuple with comma-separated numbers
# values = input("Input Some Comma Seperated Numbers")
# list = values.split(",")
# tuple = tuple(list)
# print(f"List Ghya {list} ")
# print(f"Tuple Ghaya {tuple}")

# #Input a filename and print the extension of that
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print (f"The extension of the file is : {f_extns[-1]}" )

# #display the first and last colors from a given list
# color_list = ["Red","Green","Black","meginta","Orange"]
# print(color_list[0],color_list[-1])

##Display a sample examination schedule
# exam_st_date = (11,12,2014,14,10,2015)
# print( "The examination will start from : %i / %i / %i  next date %i / %i / %i"%exam_st_date)

# #Print the calendar of a given month and year
# import calendar
# y = int(input("Enter the Year "))
# m = int(input("Enter the Month "))
# print(calendar.month(y,m))

# #two date madhil days kadhane
# from datetime import date
# f_date = date(2007,7,7)
# l_date = date(2020,12,8)
# total_d = l_date - f_date
# print(total_d.days/365)

# from math import pi
# r = int(input("Enter The Redius "))
# v = 4/3 * pi * r**3
# print(f"Volume Of Sphere with Radius {r} is {v} ")

#
# n = int(input("Enter The Number "))
# if n > 17:
#       t = n-17
#       r = t*2
#       print(f"{n} is Greter Than 17 and differance is {r}")
# else:
#      t = 17-n
#      print(f"{n} is less thaqn 17 and differance is {t}")


# # Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
# print(sum_thrice(5, 5, 5))


# #Get a new string from a given string where 'Is' has been added to the front.
# # If the given string already begins with 'Is' then return the string unchanged
# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str
#
# print(new_string("Array"))
# print(new_string("IsEmpty"))


# #Get a string which is n (non-negative integer) copies of a given string
# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + " "  + str
#       #print(result)
#    return result
#
# print(larger_string('Akshay', 10))
# print(larger_string('*', 10))


# # Find whether a given number is even or odd, print out an appropriate message to the user
# n = int(input("Enter Any number "))
# if n % 2 > 0:
#     print(f"{n} is Odd Number")
# else:
#     print(f"{n} is Even Number")


# #Count the number 4 in a given list
# def cout_num_list(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count = count + 1
#     return count
#
# list1 = [1, 2, 3, 4, 5, 6, 4, 7, 4, 8, 9, 4, 5, 4, 4, 4, 1, ]
# list2 = [4, 6, 7, 8, 9, 2, 3, 14, 3, 4, 3, 7]
# print(cout_num_list(list1))
# print(cout_num_list(list2))


# #Test whether a passed letter is a vowel or not
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))

# #print Histogram
# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while (times > 0):
#             output = output + "*"
#             times = times - 1
#         print(output)
# histogram([5, 3, 12, 6])



# #Print all even numbers from a given numbers list in the
# #same order and stop the printing if any numbers that come after
# #237 in the sequence
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]
#
# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)



##Print out a set containing all the colors from a list which are not present in other list
# color_list_1 = set(["White", "Black", "Red","purple"])
# color_list_2 = set(["Red", "Green","maginta"])
#
# print(color_list_1.difference(color_list_2))

#
# diploma_friends= set(["kishor", "sagar", "sourabh","aniket","Harshad"])
# digree_friend = set(["Suraj", "datta","aniket","sourabh"])
# print(diploma_friends.difference(digree_friend))

# #Compute the greatest common divisor (GCD) of two positive integers (mothayat motha aasa number jyane x and y la bhag jail)
# def gcd(x,y):
#     kat = 1
#
#     if x % y == 0:
#         return y
#     for i in range(int(y), 0, -1):
#         if x % i == 0 and y % i == 0:
#             kat = i
#             break
#     return kat
# print(gcd(11460,14500))

# #Write a Python program to get the least common multiple (LCM) of two positive integers
# # (lahanat lhan aasa number jayala x and y ne bhag jail)
# def lcm(x,y):
#     if x > y:
#         z = x
#     else:
#         z = y
#     while(True):
#         if z % x == 0 and z % y == 0:
#             rat = z
#             break
#         z += 1
#     return rat
#
# print(lcm(15,17))
# print(lcm(4,6))


# #Sum of three given integers. However, if two values are equal sum will be zero
# def sum(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
#
# print(sum(2, 1, 2))
# print(sum(3, 2, 2))
# print(sum(2, 2, 2))
# print(sum(1, 2, 3))



# #Sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
#
# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))


# #compound Intrest Formule
# def total(amt,int,year):
#   rat = amt * (1+ int/100)**7
#   return rat
# print(total(10000,3.5,7))



# # For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)


# #Get OS name, platform and release information
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# #Write a python program to get the path and name of the file that is currently executing.
# import os
# print("Current File Name : ",os.path.realpath(__file__))


# #Write a Python program to find out the number of CPUs using
# import multiprocessing
# print(multiprocessing.cpu_count())

# #Parse a string to Float or Integer
# n = "246.2458"
# print(float(n))
# print(int(float(n)))

# #username of our PC
# import getpass
# print(getpass.getuser())


# #Find local IP addresses using Python's stdlib
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


# #Sum of the first n positive integers
# n= int(input("Enter The Number: "))
# sum_of = (n*(n+1))/2
# print(sum_of)

# a = "hello this is feet to centimeter convertetr"
# print(a.upper())
# h_feet = int(input("Enter Feet"))
# h_inch = int(input("Enter Inch"))
# h_inch += h_feet*12
# h_cm = h_inch * 2.54
# print(f"Height =  {h_cm} cm")


# #Calculate the hypotenuse of a right angled triangle
# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
#
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is", c )


# #Convert all units of time into seconds
# days = int(input("Input days: ")) * 3600 * 24
# hours = int(input("Input hours: ")) * 3600
# minutes = int(input("Input minutes: ")) * 60
# seconds = int(input("Input seconds: "))
#
# time = days + hours + minutes + seconds
#
# print("The  amounts of seconds", time)

## Write a Python program to get an absolute file path.
# import os
# def file_path(path_fname):
#
#     return os.path.abspath(path_fname)
#
# print("absolute path is ===",file_path("rama.txt"))


# #Calculate body mass index
# height = float(input("Input your height in meters: "))
# weight = float(input("Input your weight in kilogram: "))
# print("Your body mass index is: ", round(weight / (height **2), 2))

# #Write a Python program to get the details of math module.
# # Imports the math module
# import math
# #Sets everything to a list of math module
# math_ls = dir(math) #
# print(math_ls)


# #Find the available built-in modules
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))


# #Write a Python program to get the size of an object in bytes.
# import sys
# str1 = "one"
# str2 = "four"
# str3 = "three"
# print(f"memory size of {str1} {(sys.getsizeof(str1))} bytes ")

# #Concatenate N strings
# list_of_colors = ['Red', 'White', 'Black']
# colors = '-'.join(list_of_colors)
# print()
# print("All Colors: "+colors)
# print()

# #Calculate the sum over a container
# s = sum([10,30,60])
# print(f"sum of container is {s}")

# #Count the number of occurrence of a specific character in a string
# s = "The quick brown fox jumps over the lazy dog."
# print()
# print(s.count("q"))
# print()

# #Check whether a file path is a file or a directory
# import os
# path="rama.txt"
# if os.path.isdir(path):
#     print("\nIt is a directory")
# elif os.path.isfile(path):
#     print("\nIt is a normal file")
# else:
#     print("It is a special file (socket, FIFO, device file)" )
# print()

# #Get the size of a file
# import os
# file_size = os.path.getsize("rama.txt")
# print("\nThe size of abc.txt is :",file_size,"Bytes")
# print()


# B=["a","b","c"]
# print(B[1:])

# #Write a Python program to calculate the length of a string.
# def string_length(str1):
#     count = 0
#     for char in str1:
#         count += 1
#     return count
# print(string_length('akshayphargade'))


# #Count the number of characters (character frequency) in a string
# def char_frequency(str1):
#     counts = dict()
#
#     for i in str1:
#         if i in counts:
#             counts[i] += 1
#         else:
#             counts[i] = 1
#     return counts
# print(char_frequency("akshayphargade"))

# #Count the occurrences of each word in a given sentence
# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for i in words:
#         if i in counts:
#             counts[i] += 1
#         else:
#             counts[i] = 1
#
#     return counts
#
# print( word_count('the quick brown fox jumps over the lazy dog.'))

# #Prints the unique words in sorted form from a comma separated sequence of words
# items = input("Input comma separated sequence of words")
# words = [word for word in items.split(",")]
# print(",".join(sorted(list(set(words)))))



# #Get a string made of the first 2 and the last 2 chars from a given a string
# def string_both_ends(str):
#   if len(str) < 2:
#     return ''
#
#   return str[0:2] + str[-2:]
#
# print(string_both_ends('w3resource'))
# print(string_both_ends('w3'))
# print(string_both_ends('w'))



# def add_string(str1):
#   length = len(str1)
#
#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'
#
#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))

# #Change a given string to a new string where the first and last chars have been exchanged
# def change_sring(str1):
#     return str1[-1:] + str1[1:-1] + str1[:1]
#
#
# print(change_sring('abcd'))
# print(change_sring('12345'))


# #Remove the characters which have odd index values of a given string
# def remove_odd_value(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result = result + str[i]
#     return result
# print(remove_odd_value("abcdefghijklmnopqrstuvwxyz"))

# #Display an input string in upper and lower cases
# latter = input("what is favourite language is ")
# mothha = latter.upper()
# chhota = latter.lower()
# print(mothha)
# print(chhota)

# ##Insert a string in the middle of a string
# def insert_string_inmeddle(str,word):
#     return str[:2] + word + str[2:]
#
# print( insert_string_inmeddle("[[]]",'python'))
# print(insert_string_inmeddle("{{}}","javascript"))
# print(insert_string_inmeddle("(())","data scientisti"))

## Convert JSON data to Python object
# import json
# json_obj = '{"Name": "Sagar", "Class" : "B.E", "Age" : "24" }'
# python_obj = json.loads(json_obj)
#
# print("\nJson data")
# print(python_obj)
#
# print("name: ", python_obj["Name"])
# print("class: ",python_obj["Class"])
# print("age: ",python_obj["Age"])

# #Write a Python program to convert Python object to JSON data.
#
# import json
# python_obj = {'Name': 'Sagar', 'Class': 'B.E', 'Age': '24'}
# print(type(python_obj))
# json_obj = json.dumps(python_obj)
# print(json_obj)


#list exercise


#Write a Python program to sum all the items in a list
# def sum_list(number):
#     sum_number = 0
#     for i in number:
#         sum_number += i
#     return sum_number
# print(sum_list([1,2,3,4,5,6,4]))

#Write a Python program to multiplies all the items in a list
# def multi_list(items):
#     multi_numbers = 1
#     for i in items:
#         multi_numbers *= i
#     return multi_numbers
# print(multi_list([2,3,6]))

#rite a Python program to get the largest number from a list
# def greter_num(items):
#     w_greter = items[0]
#     for i in items:
#         if i > w_greter:
#             w_greter = i
#     return w_greter
# print(greter_num([1,2,30,15,10]))

#Write a Python program to get the smallest number from a list
# def small_num(items):
#     small = items[0]
#     for i in items:
#         if i < small:
#             small = i
#     return small
# print(small_num([22,33,14,25,78,66,11]))

#Write a Python program to find the list of words that are longer than n from a given list of words.
# def markas(n,str):
#     rega = []
#     text = str.split(" ")
#     for i in text:
#         if len(i) > n:
#             rega.append(i)
#     return rega
# print(markas(3, "The quick brown fox jumps over the lazy dog"))

#Write a Python function that takes two lists and returns True if they have at least one common member.
# def true_list(list1,list2):
#     result = False
#     for i in list1:
#         for j in list2:
#             if i == j :
#                 result = True
#     return result
# print(true_list([1,5,8,8,8,87,7],[456,6,6,858,852,285,4,8]))

#Write a Python program to shuffle and print a specified list.
# from random import shuffle
# color = ["Red","Green","White","Pink","Orange","magenta"]
# shuffle(color)
# print(color)

#Write a Python program to generate all permutations of a list in Python.
# import itertools
# tena = [1,2,3,4,5,6]
# print(list(itertools.permutations(tena)))

#Write a Python program to get the difference between the two lists.
# list1 = [1, 3, 5, 7, 9]
# list2 = [1, 2, 4, 6, 7, 8]
# diff_list1_list2 = list(set(list1) - set(list2))
# diff_list2_list1 = list(set(list2) - set(list1))
# total_diff = diff_list1_list2 + diff_list2_list1
# print(total_diff)

#Write a Python program access the index of a list.
# num = [8,6,4,7,5,3,5,44]
# for num_index,num_value in enumerate(num):
#  print(num_index,num_value)

#Write a Python program to convert a list of characters into a string.
# rada = ["A","K","S","H","A","Y"]
# str1 = "".join(rada)
# print(str1)

#Write a Python program to find the index of an item in a specified list
# list1 = [30,88,99,77,55,22,75]
# tata = list1.index(77)
# print(tata)

#Write a Python program to flatten a shallow list.
# import itertools
# original_list =[[1,4,56,5],[5,77],[100],[44,74,56,874,2,1]]
# new_merge_list = list(itertools.chain(*original_list))
# print(new_merge_list)

#merge list
# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)

#Write a Python program to select an item randomly from a list.
# from random import shuffle
# import random
# logan = [1,5,64,8,6,8,7,3,4,6,45,88,665,45,62]
# shuffle(logan)
# print(logan)
# print(random.choice(logan))

#Write a python program to check whether two lists are circularly identical.
# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
#
# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print('Compare list1 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
# print('Compare list2 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

#Write a Python program to get the frequency of the elements in a list.
# import collections
# pekka = [10,20,33,10,10,10,55,44,55,77,66,44,775,30,10,33,55,44,20,0,0,0,0]
# print("Original List : ",pekka)
# kpr = collections.Counter(pekka)
# print("Frequency of the elements in the List :",kpr)

# import collections
# pekka = [10,20,33,10,10,10,55,44,55,77,66,44,775,30,10,33,55,44,20,0,0,0,0,"aks","aks","ap","aq","aks"]
# print("Original List : ",pekka)
# kpr = collections.Counter(pekka)
# print("Frequency of the elements in the List :",kpr)

#working on dictionary
#Write a Python program to add a key to a dictionary.
# d = {2:10,3:11,4:12,5:13}
# print(d)
# d.update({6:14})
# print(d)

#Write a Python program to concatenate following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4 = {}
# for d in (dic1,dic2,dic3):
#     dict4.update(d)
# print(dict4)

#Write a Python program to check whether a given key already exists in a dictionary
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def key_present(x):
#     if x in d:
#         print(f"key {x} is present in given dict")
#     else:
#         print(f"key {x} is not present in given dict")
# key_present(1)

#Write a Python program to iterate over dictionaries using for loops.
# d = {'x':10,'y':20,'z':30}
# for dict_key,dict_value in d.items():
#     print(dict_key,"=",dict_value)

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# n =int(input("Enter Any Number: "))
# d = dict()
# for x in range(1,n+1):
#     d[x] = x*x
# print(d)

#Write a Python script to merge two Python dictionaries.
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# #d = d1.copy()
# d1.update(d2)
# print(d1)

#Write a Python program to iterate over dictionaries using for loops.
# d = {'Red': 1, 'Green': 2, 'Blue': 10}
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key])

#Write a Python program to sum all the items in a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247,'10':1,'20':2}
# print(sum(my_dict.values()))

#Write a Python program to multiply all the items in a dictionary.
# my_dict = {'data1':100,'data2':54,'data3':247}
# result=1
# for value in my_dict:
#     result=result * my_dict[value]
#
# print(result)

#Write a Python program to remove a key from a dictionary
# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict:
#     del myDict['a']
# print(myDict)

#Write a Python program to map two lists into a dictionary.
# pekka = ["nana","akshay","pekka","tCS","phargade"]
# logan = [4,6,5,3,8]
# merge_file = dict(zip(logan,pekka))
# print(merge_file)

#Write a Python program to sort a dictionary by key.
# r = {'nana': 4, 'akshay': 6, 'pekka': 5, 'tCS': 3, 'phargade': 8}
# print(r)
# for k in sorted(r):
#  print('%a = %a '%(k,r[k]))

#Write a Python program to combine two dictionary adding values for common keys.
# from collections import Counter
# a = {'a':300,'b':200, 'c':100}
# T = {'a':200,'b':200,'c':500}
# D = Counter(a) + Counter(T)
# print(D)

#Write a Python program to print all unique values in a dictionary
# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# s = set()
# for dic in L:
#    for val in dic.values():
#       s.add(val)
# print("Unique Values: ",s)

# L = [{"V":"akshay"}, {"V": "sagar"}, {"VI": "kishor"}, {"VI": "kunal"}, {"VII":"sagar"}, {"V":"Anand"},{"VIII":"vishal"}]
# s= set()
# for dic in L :
#     for val in dic.values():
#         s.add(val)
# print(s)
#               #or or or or or or or or or or or
# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# #Write a Python program to find the highest 3 values in a dictionary.
# from heapq import nlargest
# my_dict = {'a':50000, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# large = nlargest(5,my_dict,key=my_dict.get)
# print(large)

#Write a Python program to combine values in python list of dictionaries.
# from collections import Counter
# tem_list = [{'item': 'item1', 'amount': 450}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in tem_list:
#     result [d['item']]+= d['amount']
# print(result)

#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.

# from collections import defaultdict, Counter
# str1 = 'w3resource'
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

#a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("Key  value  Count")
# for count , (key,value) in enumerate(dict_num.items(),1):
#   print(key ,'  ',value,'    ',count)

#Write a Python program to print a dictionary line by line.
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print(b,':', students[a][b])

#Write a Python program to check multiple keys exists in a dictionary.
# student = {
#   'name': 'Alex',
#   'class': 'V',
#   'roll_id': '2'
# }
# print(student.keys() >= {'class', 'name'})
# print(student.keys() >= {'name', 'Alex'})
# print(student.keys() >= {'roll_id', 'name'})

#Write a Python program to count number of items in a dictionary value that is a list.
# dict =  {'Alex': ['subj1', 'subj2', 'subj3',1,1,1], 'David': ['subj1', 'subj2']}
# logan = {'a':[1,5,64,8,6,8,7,3,4,6,45,88,665,45,62]}
# ctr = sum(map(len,dict.values()))
# btr = sum(map(len,logan.values()))
# print(ctr)
# print(btr)

#Write a Python program to sort Counter by value.
# from collections import Counter
# x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
# print(x.most_common())
# print(x.items())