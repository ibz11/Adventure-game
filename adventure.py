name = input("Type your in your name:")
print("Welcome ", name ,"to adventure world")

answer = input(
    "Your are on a dirt road. Are you going  left or right?: ").lower()
    

if answer == "left":
    answer=input("You have gotten to a river.Type walk to walk around it or type swim to swim: ")
    if answer == "swim":
        print("You have drowned.Failed!")
    elif answer == "walk":
        print("You walked and you became lost.Failed!")
    else:
         print("Invalid choice!")
       
elif answer == "right":
       print ('You have chosen',answer,"You can proceed!")
       answer=input("You have arrived at a village.Type scout to scout or walk to walk in: ")
       if answer == "scout":
         print("You picked",answer,"You were caught and imprisoned.You lost!")
       elif answer=="walk":
           print("You picked ",answer,"you were welcomed by the villagers")
           answer=input("The villagers give you food.Should you eat or avoid?: ")
           if answer == "eat":
               print("You picked",answer,"The food was poisoned you died!")
           elif answer == "avoid":
               print("You picked",answer,"You survived!You won the game")
           else:
               print("invalid choice!You lost!")

       else:
           print("invalid choice.You lose")

       
else:
      exit()
            


