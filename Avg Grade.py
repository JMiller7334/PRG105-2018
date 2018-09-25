def calc_average(s1, s2, s3, s4, s5):  # gets average score and returns it to the main function
    mean = (s1 + s2 + s3 + s4 + s5)/5
    return mean

def assign_grade(score):  # assigns a letter grade using elif and returns that letter grade to the main function.
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade

def main():  # gets user input, calls other functions, prints results to the user.
    score1 = int(input("Please enter a test score. "))
    score2 = int(input("Please enter a test score. "))
    score3 = int(input("Please enter a test score. "))
    score4 = int(input("Please enter a test score. "))
    score5 = int(input("Please enter a test score. "))

    average = calc_average(score1, score2, score3, score4, score5)
    letter_grade = assign_grade(average)
    print("The average score: " + str(average) + "Letter grade: " + letter_grade)

main()