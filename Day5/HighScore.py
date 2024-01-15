# Input a list of student scores
student_scores = input("Scores : ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_score = 0
for score in student_scores :
    max_score = student_scores[0]
    if score > max_score :
        max_score = score

print(f"High Score : {max_score}")