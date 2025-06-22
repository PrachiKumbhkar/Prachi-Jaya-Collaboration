# Ques.9.  Write a Python program to count the number of lists in a given list of lists.

list2 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
count=0

for el in list2:
    if type(el) == list:
        count +=1
    
print(count)

# Ques. 10.  Write a Python program to extract specified size of strings from a give list of string values.

# strList = ['Python', 'list', 'exercises', 'practice', 'solution']

def getStrings(strList,n):
    specifiedLenStr = []
    for i in strList:
        print(i)
        if(len(i)==n):
            specifiedLenStr.append(i)

    return specifiedLenStr


print(getStrings(['Python', 'list', 'exercises', 'practice', 'solution'],4))


#  factorial 

def factorial(n):
    fact = 1 

    if n == 1 or n==0 :
        return "factorial is 1"
    
    else:
        for i in range(2, n+1):
            fact = fact*i 

    return fact

print(factorial(5))

#  fibonacci

def fibonacci(n):
    fibolist = [0,1]

    for i in range(2,n):
        fibolist.append(fibolist[i-1] + fibolist[i-2])
    return fibolist

print(fibonacci(8))

#  check a number is prime or not

def checkprime(n):
    if n == 1 or n==n:
        return "prime number"
    
    else:
        for i in range(2,n):
            if n % i ==0:
                return "Not prime"
            else:
                return "prime"
            
print(checkprime(11))

#  check leap year
def leapyear(year):
    if year % 4 ==0 :
        if year%100 == 0 :
            if year %400 ==0:
                print("leap")
            else:
                print("not leap")
        else:
            print("leap year")
    else:
        print("not leap year")

leapyear(2014)

# Ques. 17 . Write a  Python program to remove characters that have odd index values in a given string.

# stringList1 = "hii Jaya Kumbhkar Coderwin LongestWord Excersicesss"

def oddindexvalue(string):
    oddindexremoved = ""

    for i in range(len(string)):
        if i %2 ==0 :
            oddindexremoved += string[i]

    return oddindexremoved

print(oddindexvalue("hii Jaya Kumbhkar Coderwin LongestWord Excersicesss"))

# Ques. 18.  Write a Python program to count the occurrences of each word in a given sentence.

# sentence ="The quick brown fox jumps over the lazy dog. The fox was quick."

def occurenceofword(string):
    emptydict = {}

    splittedlist = string.split(" ")

    for el in splittedlist:
        if el not in emptydict:
            emptydict[el] = 1 

        else:
            emptydict[el] = emptydict[el] + 1 

    return emptydict

print(occurenceofword("The quick brown fox jumps over the lazy dog. The fox was quick."))


# Ques. 19.  Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def copies(string):
    repeatedly = ""
    if len(string) ==2:
        return string*4
    else:
        repeatedly = repeatedly + string[-2:]*4

    return repeatedly

print(copies("exercise"))

# # 3. Write a Python program to get the largest number from a list.

l1 = [23,45,6,9,84,35]
largest_num = l1[0]
shortest_num = l1[0]

for i in l1:
    if i > largest_num:
        largest_num = i 

print(largest_num)

#  seocnd method

sortedlist = sorted(l1)
print(sortedlist)

getlastelement = sortedlist[-1]
print("this is the largest element : " , getlastelement)


# 5.Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
given_list=['abc', 'xyz', 'aba', '1221']

count = 0 
for el in given_list:
    if el[0] == el[-1]:
        count +=1

print(count)


# 6.  sort list using logic 
lists = [23,45,6,9,84,35,22]

for i in range(len(lists)):
    min_index = i 

    for j in range(i+1 , len(lists)):
        if lists[j] < lists[min_index]:
            min_index =j 

    lists[i] , lists[min_index] = lists[min_index] , lists[i]

print(lists)

# second method 
newsorted = sorted(lists,key = lambda x : x)
print(newsorted)

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]              Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# first method
sortedinputlist = sorted(input_list , key = lambda x : x[-1])
print(sortedinputlist)

#  second method

for i in range(len(input_list)):
    min_indx  = i 

    for j in range(i+1, len(input_list)):
        if input_list[j][-1] < input_list[min_indx][-1]:
            min_indx = j 

    input_list[i] , input_list[min_indx] = input_list[min_indx] , input_list[i]

print(input_list)


#  remove duplicate from a list 
ls = [1,2,2,3,4,4,5,7,7]

# first method
uniquele = []
for i in ls:
    if i not in uniquele:
        uniquele.append(i)
print(uniquele)

#  second method
emp_dict ={}
uniquelist = []
for i in ls:
    if i not in emp_dict:
        emp_dict[i] =1 

    else:
        emp_dict[i] = emp_dict[i] + 1

for key,value in emp_dict.items():
    if value == 1 :
        uniquelist.append(key)
print(uniquelist)

# 8. Write a Python program to check if a list is empty or not.
def checkemptylist(lists):
    emp = []

    if lists == emp:
        return "empty"
    else:
        return "not empty"
    
print(checkemptylist([]))
print(checkemptylist([1,2,3]))

#  seocond method

def checkempty(lists):
    if len(lists) == 0:
        return "empty"
    else:
        return "not empty"
    
print(checkempty([1]))

# 10 .Write a Python program to find the list of words that are longer than n from a given list of words.
def longer_than_n(lists,n):
    wordlists = []

    for word in lists:
        if len(word) > n :
            wordlists.append(word)

    return wordlists

print(longer_than_n(["jaya","kumbhkar","coderwin","indore","hello","thoughtwin","hiihello"],4))


# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']               Expected Output : ['Green', 'White', 'Black']
def remove_specified_index(lists,n):
    after_removed = []

    for i in range(len(lists)):
        if i not in n:
            after_removed.append(lists[i])

    return after_removed

print(remove_specified_index(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] ,[0,4,5]))

generated_list = []

new_squaredlist = []
for el in range(1,31):
    generated_list.append(el*el)

first5 = generated_list[0:5]
last5 = generated_list[-5:]

new_squaredlist.append(first5+last5)

print(new_squaredlist)

# check prime in list
lists = [11,32,16,7,8,17,3,64]
for i in lists:
    if i> 1 :
        for j in range(2,i):
            if i % j ==0:
                break

        else:
            print(i , "prime")

import random
ls1 = [22,45,76,434,778,342,65]
randomlychoosed = random.choice(ls1)
print(randomlychoosed)

# Write a Python program to count the number of elements in a list within a specified range.
def countelement(lists,start,end):
    return len(lists[start:end])
print(countelement([22,56,43,87,65,87,54,32,67,89,23,55,32,82,61,28],3,9))

#35.  Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
ls2 = ["p","q"]
newlist=[] 
for i in range(1,6):
    for j in ls2:
        newlist.append(j+str(i))
        
print(newlist)

# 39. Write a  Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]    Expected Output: 113350

def myfunc(lists):
    strings = ""

    for el in lists:
        strings = strings+ str(el)

    return int(strings)

print(myfunc([11,33,50]))





















