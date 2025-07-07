# Ask user for a number and use for loop to print its multiplication table.

num = int(input("Enter a number: "))
print("Your mutipication table of:Multiplication Table Generator",num)

for i in range (1, 11):
    print(f"{num} x {i} = {num*i}")
