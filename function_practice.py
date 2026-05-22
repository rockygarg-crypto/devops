# what is function in python.

# 1. every function has their own purpose.
# 2. function is block of instruction(code) which exucute inside its own block.
# 3. function is reusable means define one time use manytime (dry).
# 4. function has two main part.
#   1. first function defination.
#   2. second function calling.
# 5. in python by default return.

# def add():
#     a=20
#     b=11
#     c=a+b
#     print(c)
# add()

# function divide in four category.
# 1.take nothing return nothing.
# 2.take nothing return something.
# 3.take somthing return nothing.
# 4.take somthing return something.

# posotional parameter.

# def add(a=0,b=0): (default parameter)
#     print("addition :",a+b)
 

# def sub(a=0,b=0):
#     print("subtraction :",a-b)

# def mul(a=0,b=0):
#     print("multi :",a*b)

# def div(a=0,b=0):
#     print("division :",a/b)

# num1=int(input("Enter your number :- "))
# num2=int(input("Enter your first number :- "))

# opt= input("+,-,*,/ :- ")

# if opt == "+":
#     add(num1,num2)
# elif opt =="-":
#     sub(num1,num2)
# elif opt =="*":
#     mul(num1,num2)
# elif opt == "/":
#     div(num1,num2)
# # else:
# #     print("Wrong input")


# def add(a,b):
#     return a+b
# res=add(10,30)

# def sub(a,c):
#     return a-c
# print(sub(10,res)) (argument)


# wap to check number pass by argument is odd or even.
# def odd_even(a):
#     if a % 2 ==0:
#         print("even")
#     else:
#         print("odd")
# odd_even(4)

# wap of check which number is greater and two number by user.
#wap to check the character pass by user is vowel or consonant.

# def check_char(a):
#     if a in "aeiou":
#         print("vowels")
#     else:
#         print("consonants")
# check_char("a")

# wap to check is number completly divide by 2 and 3 and return.
# "yes number is completly divide"
# "no number is not completly divide"


# def check_number(n):
#     if n % 2 == 0 and n % 3 == 0:
#         return "yes number is completly divide"
#     else:
#         return "yes number is not completly divide"
            
# res=check_number(7)
# print(res)

# wap to return length of a string pass by user without using len()
# def len_string(s):
#     c=0
#     for i in s:
#         c=c+1
#     return c
# print(len_string("devops"))

# wap to check given how many vowels in given string.

# def count_vowel(a):
#     c=0
#     for i in a:
#         if i in "aeiou":
#             c+=1
#     return c
# res=count_vowel("programing")
# print(res)

# # local varibles vs global variable.
# def msg():
#     global name
#     name="dev" 
#     print(name)
# msg()
# print("outside :",name)

# wap to count our "p" in "python programing" return total occurence.

# def count_char(ch):
#     c=0
#     for i in ch:
#         if i == "p":
#             c+=1
#         return c
# res=count_char("programing")
# print(res)
    

# # wap to retrun sum of indexes.
# def sum_indexes(a):
#     s=0
#     for i in range(len(a)):
#         s=s+i
#     return s
# res=sum_indexes("python")
# print(res)




