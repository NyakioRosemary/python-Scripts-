# what? send a message to the students to remind then of their assignments and current grades
# assign list input of names, no_of assignments, and current_grade
name = input("Enter student names(separate with comma ,): ").title().split(",")
no_of_assignments = input("Enter student assignments(integer numbers & separate with comma ,): ").split(",")
current_grade = input("Enter student current grade(integer numbers & separate with comma ,): ").split(",")
# message to be printed out
message ="Hi {},\nThis is a reminder that you have {} \nassignments left to submit before you can graduate. Your current grade \nis {} and can increase to {} if you submit\nall assignments before the due date.\n"
""" for all asigned list values they all have a relationship so we zip them
        print by formating all the variables current grade and no. of assignment being ints
        then multiply by 2 to predict a number if the complete the assignments"""
for names, assignments, current_G in zip(name, no_of_assignments, current_grade):
    while True:
        try:
            #print(message.format(names, assignments, current_G, int(current_G)+int(assignments)*2))
            break
        except ValueError:
            print("Grade and Assignments must be Integers! Rerun program and give it a another try.")
            break
        except KeyboardInterrupt:
            print("\n No inputs taken.")
            break
        finally:
            ("Nice.")