programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Function"])

#  add to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary = {}


# wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)


# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



# from the challenge my solution
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def grade(score):
    str_scored = ""
    if score < 70:
        str_scored = "Fail"
    elif 70 < score <= 80:
        str_scored = "Acceptable"
    elif 80 < score <= 90:
        str_scored = "Exceeds Expectations"
    else:
        str_scored = "Outstanding"
    return str_scored

for student in student_scores:
    student_grades[student] = grade(student_scores[student])

print(student_grades)


# Solution from challenge
# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary
for student in student_scores:

    # Get the value (student score) by using the key each time.
    score = student_scores[student]

    # Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'