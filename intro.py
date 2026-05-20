#c=0
#a = "this is python"
#for i in a:
 #   if i==" ":
 #       c+1
#print(c)
        
 # address="d-1 267/268 mayur-vihar-phase-3 110096"     

#c=0
#address="d-1 267/268 mayur-vihar-phase-3 110096"
#number="0123456789"
#for i in address:
 #   if i in number:
  #     c+=1
#print(c)

# start=10
# end=20
# while start <= end:
#     if start%2==0:
#         print(start)
#     start+=2

#wap to take a number from user input and print formatted table
# num=int(input("Enter your number : "))
# i=1
# while i <= 10:
#     print(f"{num} * {i} = {num*i}")
#     i+=1    

#wap to take a number from user input and print reversed formated table.

# num=int(input("Enter your number : "))
# i=10
# while i >= 1:
#     print(f"{num} * {i} = {num*i}")
#     i-=1


# wap to print the total of even number from 1 to 15.
# wap to chek the give string by user is "palindrame" or not palindrame".
# wap to reverse the digits : 1234 output : 4321

text="aman"
copy_text=text
rev=""
i=len(text)-1

while i>=0:  
    rev=rev+text[i]
    i-=1
if copy_text==rev:
    print("palindrome")
else:
  print("not palindrom")