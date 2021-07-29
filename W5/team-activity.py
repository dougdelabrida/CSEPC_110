grade_percentage = float(input("What's your grade percentage?: "))

if grade_percentage > 100:
  print("You're a genius. You broke the school's record.")

if grade_percentage < 0:
  print("You'll repeat the class. 2x")

letter = ""

# determine the letter
if grade_percentage >= 90:
  letter = "A"
elif grade_percentage >= 80:
  letter = "B" 
elif grade_percentage >= 70:
  letter = "C"
elif grade_percentage >= 60:
  letter = "D"
else:
  letter = "F"

# add + or -
if grade_percentage % 10 >= 7 and (letter != "A" and letter != "F"):
  letter = letter + '+'

if grade_percentage % 10 < 7 and letter != "F":
  letter = letter + '-'

print("")

result = "Congrats, you passed the course" if grade_percentage >= 70 else "You didn't pass. Good luck next time";

print(f"{result}. Your final grade is: {letter}")
