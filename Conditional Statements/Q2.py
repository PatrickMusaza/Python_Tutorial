score = int(input("Enter the score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 60 > score >=0:
    grade = 'F'
else:
    grade = 'Invalid Score'
print(f"Grade: {grade}")