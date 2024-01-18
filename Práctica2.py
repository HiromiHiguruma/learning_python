
def game ():
    
    Palm = True
    fingers = 5
    while Palm == True:
    
        if fingers >=1:
         confirmation = input ("Do you want to remove a finger. ")
         correct_answer = "yes"

         if confirmation.lower() == correct_answer :
            fingers = fingers -1
            print ("You have " + str(fingers) + " fingers. ")
         elif confirmation == "I don't have any fingers":
             print ("Too bad")

         else:
                fingers = fingers
                print ("You have " + str(fingers) + " fingers. ")
        else:
            print ("You have no more fingers. ")
            Palm = False
    if Palm == False:
        Answer = input ("Do you want to play again?")
        if Answer.lower() == "yes":
            game ()
        else:
            print ("Bye bye. ")
            input()
game ()