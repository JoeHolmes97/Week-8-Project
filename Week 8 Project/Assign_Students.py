
# Module for assigning students

def AssignStudents(o_StudentList, s_Classes): # Function for assigning a student to a class

    bContinue = True

    while bContinue == True:

        GenFun.DisplayStudents(o_StudentList) # Run the DisplayStudents function with the list o_StudentList

        print("\n----------------Assign Student----------------\n")

        s_MenuItems = ["Which student would you like to assign to a class?"] # Create a list with this string as the only entry

        for i in range(0, len(o_StudentList)): # Loop a number of times equal to the number of students
            s_MenuItems.append(o_StudentList[i].FirstName + " " + o_StudentList[i].LastName) # Add the first and last name of the current student to the end of the list

        s_MenuItems.append("Return to main menu") # Add this option to the end of the list

        iMenuChoice = int(GenFun.Menu(s_MenuItems)) # Run the Menu function with the list s_MenuItems

        if iMenuChoice == len(s_MenuItems) - 1: # If the user chooses the last menu option, do this
            
            bContinue = False # Set bContinue to False, exiting the loop

            LineBreak()

        else:

            bLoop = True

            while bLoop == True:
                
                s_MenuItems = ["\n Which class would you like to assign " + o_StudentList[iMenuChoice-1].GetName() + " to?"]

                for x in range(0, len(s_Classes)):

                    s_MenuItems.append(s_Classes[x])

                s_MenuItems.append("Return")

                iClassChoice = int(GenFun.Menu(s_MenuItems))

                if iClassChoice == len(s_MenuItems) - 1:
                    
                    bLoop = False

                else: 

                    bLoop = False

                    o_StudentList[iMenuChoice - 1].sClassName = s_Classes[iClassChoice-1]

                    print("You have successfully assigned " + o_StudentList[iMenuChoice-1].GetName() + " to " + s_Classes[iClassChoice-1])
