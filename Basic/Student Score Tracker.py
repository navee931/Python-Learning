# Store marks of students and calculate average using loop.

scores = []

while True:
    score = input("Enter score or Type done to finish: ")
    if score.lower() == "done":
        break
    scores.append(int(score))

average = sum(scores)/len(scores)
print("Average of student marks: ",average)


# Store marks of students and calculate average.

num = input("Enter score seprated by comma: ")
scores = [int(score.strip()) for score in num.split(',')]
average = sum(scores)/len(scores)
print("Average of student marks: ",average)