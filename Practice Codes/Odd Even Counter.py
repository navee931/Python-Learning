# Loop through numbers from 1 to N and count how many are even and how many are odd.

n = int(input("Enter a number: "))
even = 0
odd = 0

for i in range(1, n+1):
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("Odd", odd)
print("Even", even)
