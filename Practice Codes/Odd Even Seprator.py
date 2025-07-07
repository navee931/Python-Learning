# Take a list and separate even/odd into two lists.

num = []
even = []
odd = []
while True:
    nums = input("Enter numbers and Type done when finish: ")
    if nums.lower() == "done":
        break
    num.append(int(nums))

for n in num:
    if n%2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Even no's: ", even)
print("Odd no's: ", odd)
