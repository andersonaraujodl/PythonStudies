'''
Write a program that receives 2 grades of a student (from 0 to 10) and return if they passed,
failed or will have to do a final test.

You should know that*:
1) A student fails if their final G.P.A is less than 5.0;
2) A student has to do a final test if their final G.P.A is between 5.0 and 6.9;
3) A student passes is their final G.P.A is 7.0 or more.

*Based on the Brazilian system.
'''
#const
NUMBER_OF_GRADES = 2
FAIL_GPA = 4.9
APPROVED_GPA = 7.0

firstGrade = float(input("What's the first grade? "))
secondGrade = float(input("What's the second grade? "))

finalGpa = (firstGrade + secondGrade) / NUMBER_OF_GRADES

if finalGpa <= FAIL_GPA:
    print("You failed with a final G.P.A of {}! You better study more next time.".format(finalGpa))
elif finalGpa >= APPROVED_GPA:
    print("Congratulations! You passed with a final G.P.A of {}!".format(finalGpa))
else:
    print("Almost there! You will need to do a final test to try to improve your final G.P.A of {}!".format(finalGpa))