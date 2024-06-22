# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2052962
# Date: 04.12.2023

#import graphic module
from graphics import *

#assigning the variables
Count_of_Progress = 0
Count_of_ModuleTrailer = 0
Count_of_Do_Not_Progress = 0
Count_of_Exclude = 0
outputs=[]
Final_output = 0  
height_of_coloumn = 0


#Function which checks weather the user inputs are valid or not and if its valid, what's the output should be.
def Evaluate_student_progress(Pass_credits, Defer_credits, Fail_credits):
    global Count_of_Progress, Count_of_ModuleTrailer, Count_of_Do_Not_Progress, Count_of_Exclude
    
    #Checking whether the user inputs are out of range
    if Pass_credits not in [0,20,40,60,80,100,120]:
        return "Out of range"
    
    if Defer_credits not in [0,20,40,60,80,100,120]:
        return "Out of range"
    
    if Fail_credits not in [0,20,40,60,80,100,120]:
        return "Out of range"

    # Checking whether the addition of 3 values are equal to 120.
    if Pass_credits + Defer_credits + Fail_credits != 120:
        return 'Total Incorrect'

    # Calculating the outputs while getting the count of each output.
    if Pass_credits == 120:
        Count_of_Progress += 1
        return 'Progress'

    elif Pass_credits == 100 and (Defer_credits == 20 or Fail_credits == 20):
        Count_of_ModuleTrailer += 1
        return 'Progress (Module Trailer)'

    elif Fail_credits >= 80:
        Count_of_Exclude += 1
        return 'Exclude'

    else:
        Count_of_Do_Not_Progress += 1
        return 'Do not progress - module retriever'

#Function which gets the inputs from the user
def user_inputs():    
    while True:
        try:
            # getting the inputs from the user
            Pass_credits = int(input("How many pass credits? "))
            Defer_credits = int(input("How many defer credits? "))
            Fail_credits = int(input("How many fail credits? "))
            return Pass_credits, Defer_credits, Fail_credits

        except ValueError:
            # The output which should appear if the user enters a letter without entering a number
            print("Integer Required")


#Function which runs if its a student
def student(): 
    Pass_credits, Defer_credits, Fail_credits = user_inputs()   
    Final_output = Evaluate_student_progress(Pass_credits, Defer_credits, Fail_credits)
    print(Final_output)
    print()

#Function which runs if its a staff member.
def staff():
    while True:
        try:
            Pass_credits, Defer_credits, Fail_credits = user_inputs()
            Final_output = Evaluate_student_progress(Pass_credits, Defer_credits, Fail_credits)
            print(Final_output)
            print()

            # Appending final output with pass, defer, and fail credits to the 'outputs' list.
            outputs.append(f"{Final_output} - {Pass_credits}, {Defer_credits}, {Fail_credits}")

            #checking whether user wants to continue or quit.
            exiting = input("Please enter 'y' to continue or 'q' to exit: ").lower()

            # Check if the input is valid 
            while exiting not in ["y", "q"]:
                print("Invalid input.")
                exiting = input("Please enter 'y' to continue or 'q' to exit: ")
                exiting.lower()

            # Break the loop if user chooses to exit
            if exiting == "q":
                break
        
        except ValueError:
            print("Integer Required")

    

    print('Part 2')

    # Printing each element in the 'outputs' list on a new line
    print('\n'.join(outputs))

    # File path for the 'outputs' file on the desktop
    file_path = r"C:\Users\DELL\Desktop\CW\outputs"  

    # Writing outputs which are in 'outputs' list on text file.
    file = open("Summary", 'w')
    file.write("Part 3\n")
    file.write("\n".join(outputs))
    file.close()

    #Create window for the historgam.
    window = GraphWin("Histogram for the inputs", 800, 600)
    window.setBackground("Mint Cream")# Set the background colour of the window

    #Checking what is the maximun count out of all 4 output counts.
    maximum_count = max(Count_of_Progress, Count_of_ModuleTrailer, Count_of_Do_Not_Progress, Count_of_Exclude)

    # Scaling counts to ensure the column with the highest count reaches the top level.
    scaling_factor = 200 / maximum_count

    # Draw the progress coloumn
    progress_coloumn = Rectangle(Point(100, 400), Point(175, 400 - Count_of_Progress * scaling_factor))
    progress_coloumn.setFill("green")
    progress_coloumn.draw(window)

    # Draw the Progress (Module trailer) coloumn
    module_trailer_coloumn = Rectangle(Point(200, 400), Point(275, 400 - Count_of_ModuleTrailer* scaling_factor))
    module_trailer_coloumn.setFill("yellow")
    module_trailer_coloumn.draw(window)

    # Draw the Do Not Progress (module retriever) coloumn
    module_retriever_coloumn = Rectangle(Point(300, 400), Point(375, 400 - Count_of_Do_Not_Progress * scaling_factor))
    module_retriever_coloumn.setFill("orange")
    module_retriever_coloumn.draw(window)

    # Draw the exclude coloumn
    exclude_coloumn = Rectangle(Point(400, 400), Point(475, 400 - Count_of_Exclude * scaling_factor))
    exclude_coloumn.setFill("red")
    exclude_coloumn.draw(window)

    #Draw the black line under coloumns
    straight_line = Line(Point(75,400),Point(500,400))
    straight_line.draw(window)

    #Adding the heading as a text.
    heading = Text(Point(150,80),'Histogram Results')
    heading.draw(window)

    #Adding the progression names under each coloumn.
    progress_text = Text(Point(135,420),'Progress')
    progress_text.draw(window)

    module_trailer_text = Text(Point(235,420),'Trailer')
    module_trailer_text.draw(window)

    module_retriever_text = Text(Point(340,420), 'Retiever')
    module_retriever_text.draw(window)

    exclude_text = Text(Point(435,420), 'Exclude')
    exclude_text.draw(window)

    #Displaying the count above each coloumn.
    progress_count = Text(Point(140,390 - Count_of_Progress * scaling_factor), str(Count_of_Progress)) 
    progress_count.draw(window)

    module_trailer_count = Text(Point(240,390 - Count_of_ModuleTrailer* scaling_factor), str(Count_of_ModuleTrailer))
    module_trailer_count.draw(window)

    module_retriever_count = Text(Point(345, 390 - Count_of_Do_Not_Progress * scaling_factor), str(Count_of_Do_Not_Progress))
    module_retriever_count.draw(window)

    exclude_count = Text(Point(440, 390 - Count_of_Exclude * scaling_factor),str(Count_of_Exclude))
    exclude_count.draw(window)

    #To display total outcomes in the bottom of the window.
    total_outcomes = Text(Point(160,460),'Total Outcomes = ')
    total_outcomes.draw(window)

    total_count = Text(Point(240,460),str(Count_of_Progress+Count_of_ModuleTrailer+Count_of_Do_Not_Progress+Count_of_Exclude))
    total_count.draw(window)

    #Close the window when the user clicks the mouse.
    window.getMouse()
    window.close()

#Calls the corresponding function (student or staff) after user enters if he/she is a student or staff.
def main():
    user_menu = input("Are you a student or staff? ")
    
    user_menu.lower()
    
    if user_menu == 'student':
        student()
    elif user_menu == 'staff':
        staff()
    else:
        print("Invalid input.")

#calling the main function.
main()
