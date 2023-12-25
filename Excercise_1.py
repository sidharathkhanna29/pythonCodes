ctd = 'y'
while ctd != 'n':
    a = int(input("Enter Assignment score: "))
    q = int(input("Enter Quiz score: "))
    t1 = int(input("Enter Test 1 score: "))
    t2 = int(input("Enter Test 2 score: "))
    grade = ""
    gp = ""

    final = float(0.25 * (a + q + t1 + t2))
    if final > 100 or final < 0:
        print("Out of Scope, check your scores")
    else:
        if final >= 94:
            grade = "A+"
            gp = "4.0"
        elif final >= 87:
            grade = "A"
            gp = "3.7"
        elif final >= 80:
            grade = "A"
            gp = "3.5"
        elif final >= 77:
            grade = "B+"
            gp = "3.2"
        elif final >= 73:
            grade = "B"
            gp = "3.0"
        elif final >= 70:
            grade = "B-"
            gp = "2.7"
        elif final >= 67:
            grade = "C+"
            gp = "2.3"
        elif final >= 63:
            grade = "C"
            gp = "2.0"
        elif final >= 60:
            grade = "C-"
            gp = "1.7"
        elif final >= 50:
            grade = "D"
            gp = "1.0"
        else:
            grade = "F"
            gp = "0.0"

        # print("Final mark is {}, and grade is {} and Grade Point is {}".format(final, grade, gp))
        print(f"Final mark is {round(final)}, and grade is {grade} and Grade Point is {gp}")
    ctd = input("Do you want to continue: ")
