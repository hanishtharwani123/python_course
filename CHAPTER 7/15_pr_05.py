num = int(input("Enter the number"))
sum = 0
for i in range(1, num+1):
    sum = sum + i
print(f"Sum of the n natural number is {sum}")







# Sum of natural numbers up to num

num = int(input("Enter the number"))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# Python Program to find Sum of N Natural Numbers
 
number = int(input("Please Enter any Number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))