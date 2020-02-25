# I am Prerak Patel and my student number is 000736376, I have designed this
# program by myself and I have not shared this anyone.My professor's name is
# Tiffany,Antopoloski


def average( quizWeight, quizAverage, labWeight, labAverage, assignmentWeight, assignmentAverage,\
                         examWeight, examAverage ):
    
    grade_average = ( quiz_weight * quiz_average + lab_weight * lab_average + assignment_weight * assignment_average + \
                         exam_weight * exam_average ) / ( quiz_weight + lab_weight + assignment_weight + exam_weight )
    return grade_average
def grade(total):
    if ( total >= 90):
        course = "Your grade is A"
    elif (75 <= total > 90):
        course = "Your grade is B"
    elif (60 <= total > 75):
        course = "Your grade is C"
    elif (50 <= total > 60):
        course = "Your grade is D"
    elif (total < 50):
        course = "Your grade is F"    
    return course


lab_weight = int(input("What is the weight of the labs in the course? "))
quiz_weight = int(input("What is the weight of the quizzes in the course? "))
assignment_weight = int(input("What is the weight of the assignments in the course? "))
exam_weight = int(input("What is the weight of the exams in the course? "))

lab_number = int(input("How many labs do you have in the course ? "))
quiz_number = int(input("How many quizzes do you have in the course ? "))
assignment_number = int(input("How many assignments do you have in the course ? "))
exam_number = int(input("How many exams do you have in the course ? "))

quiz_counter = 0
total = 1
quiz_marks = ""

while (quiz_counter != quiz_number):
    quiz_counter += 1
    quiz_marks = int(input("How many percentege have you got in your Quiz " + str(quiz_counter) + " ? "))
    total = total + quiz_marks
print("\n")
quiz_average = total / quiz_counter

lab_counter = 0
total = 1
lab_marks = ""

while (lab_counter != lab_number):
    lab_counter += 1
    lab_marks = int(input("How many percentege have you got in your Lab " + str(lab_counter) + " ? "))
    total = total + lab_marks
print("\n")
lab_average = total / lab_counter

assignment_counter = 0
total = 1
assignment_marks = ""

while (assignment_counter != assignment_number):
    assignment_counter += 1
    assignment_marks = int(input("How many percentege have you got in your Assignment " + str(assignment_counter) + " ? "))
    total = total + assignment_marks
print("\n")
assignment_average = total / assignment_counter

exam_counter = 0
total = 1
exam_marks = ""

while (exam_counter != exam_number):
    exam_counter += 1
    exam_marks = int(input("How many percentege have you got in your Exam " + str(exam_counter) + " ? "))
    total = total + exam_marks
print("\n")
exam_average = total / exam_counter

total_average = average( quiz_weight, quiz_average, lab_weight, lab_average, assignment_weight, assignment_average,\
                         exam_weight, exam_average )

Course_grade = grade( total_average )

print("You have grand total of " + str(total_average) + " and " + str(Course_grade) + ".")
