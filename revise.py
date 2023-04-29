# Rawan Amr ,1C ,WE Zayed
# print(WE_Zayed == Top_El_Top)  # outputs: True , and will do FOREVER !

"""
my_list = [12, 43, 65, 32, 87, 91]

def maxNum (mylist):
    maxnum = 0
    for i in mylist:
        if i > maxnum:
            maxnum = i

    return maxnum

print(maxNum(my_list)) # outputs 91 
"""



"""
def EvenOrOdd (num):
    if num != 0 and num > 0:
        
        if num % 2 == 0 :
            return "EVEN"
        
        return "ODD"
    
    else:
        return "ERROR : INPUT NOT ACCEPTED. NUM is ZERO or NEGATIVE!"  

print(EvenOrOdd(5)) # outputs "ODD"
print(EvenOrOdd(4)) # outputs "EVEN"
print(EvenOrOdd(0)) # outputs "ERROR : INPUT NOT ACCEPTED. NUM is ZERO or NEGATIVE!"

"""


"""
def calcAge(birthdate,dateToday):
    
    "This function accepts two inputs in the following string format : 'dd/mm/yyyy' ,the first is the the birthdate of the person and the second is the date today and returns an integer of the age of that person in years"

    day,month,year = [int(x) for x in dateToday.split("/")]
    birthday,birthmonth,birthyear = [int(x) for x in  birthdate.split("/")]

    age = year - birthyear
    
    if month < birthmonth or (month == birthmonth and day < birthday):
        age -= 1
            
    return age    

print(calcAge("25/1/2008","29/4/2023")) # outputs 15
"""

"""
num = int(input("Enter an integer number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("ERROR: you CANNOT enter a ZERO")
"""

"""
number = int(input("Enter an integer : "))

def Cube(num):
    for i in range(1,num + 1):
        cube = i ** 3
        print("Current Number is :", i,  "and the cube is", cube)

Cube(number)
"""

"""
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)

    i += 1

"""

"""
def maxNum(a,b,c):
    nums = [a,b,c]

    maxnum = nums[0]
    
    for num in nums:
        if num > maxnum:
            maxnum = num

    return maxnum

print(maxNum(15,5,206)) # outputs 206 
"""


"""   
def km_to_miles(km):
    return km * 0.62137

print(km_to_miles(8)) # outputs 4.97096
print(km_to_miles(10)) # outputs 6.213699999999999
"""

"""
def evenSum(lst):
    Sum = 0  
    for i in lst:
        if i % 2 == 0:
            Sum += i
    return Sum

print(evenSum([1,2,3,4,5,6])) # outputs 12
"""

"""
def listProduct(lst):
    product = 1
    
    for i in lst:
        product *= i
        
    return product
    
    
print(listProduct([2,3,4])) # outputs 24
"""

"""
# used float()instead of int() to increase the range of accepted input and decrease probability of error occurence
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

nums = [a,b,c]

min_num = nums[0]

for num in nums:
    if num < min_num:
        min_num = num

print(min_num)
"""

"""
def isPalindrome(word):
    if word == word[::-1]:
        return True
    return False

print(isPalindrome("level")) # outputs True
print(isPalindrome("Rawan Amr :)")) # outputs False

"""


