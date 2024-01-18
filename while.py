def ejercicio1 ():
    i=1
    while i<= 10:
            print (i)
            i+=1
    print ("Done!")

def ejercicio2 ():
      secret_word="chicago"
      guess=""
      guess_count = 0
     

      while guess!=secret_word and guess_count <= 2 :
            guess=input ("Enter the secret word. ")
            guess_count+=1
      if guess_count<=2:
        print ("You win.")
      else:
           print("You lose")
ejercicio1 ()