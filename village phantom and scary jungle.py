print("welcome to this 'village phantom and Scary jungle'adventure game!!!")
name=input("enter your name:")
print(f"Hello{name}!In this your going to challenge that your really scar for phantoms and night jungles or u didn't scar.LET'S CHECK COME ON!!")
print("we are exiting to start the game")
start=input("let me know that in which ur interested in chasing or give up.")
if start=='chasing':
          print("wooh hoo!you have made your first step in this adventure,let's begin.")
          setting=input("which one do you prefer(1/2):")
          print("Great, let me tell you the rules and instructions while your playing.")
else:
    print("lame.You are done!")
    quit()
location=input('village phantom or scary jungle:')
if location=="village phantom":
    print("you are in a village phantom.you can either go to left or right.")
    direction=input("there are two ways,which way would you prefer?(left/right):")
    if direction=="left":
        location="a small light house"
        print("it can be easier to proceed to next step and helps you to dead later.")
        transport=input("you notice there exists a canoe or you can go there by walk if you have energy.")
        if transport=='walk':
            print("if you go to left side there exists a shopkeeper now can ask him where this a 'light house' here,or you can also find it by going straight to the shop.")
            print("you reached the light house.")
            press=input("press either($/^).")
            if press=="^":
                print("by pressing this you can reach the destination that you'll  know the information about phantom.Level is reached.")
            elif press=="$":
                print("to get bonus you press this,but you can't end this  game as soon as possible,press level 2.")
            else:
                print("unable to go further level,Quit.")
        elif transport=='canoe':
            print("you can reach the light house faster than by walk,which is 10min faster than the walk.")
        else:
            print("think sure about exiting!!!")

            follow=input("for continue just follow the 8 number.")
            if follow=="8":
                print("congrats on reaching the other level.MOve on,you find reward.")
            else:
                ("press back to exit")

    elif direction=="right":
        location="mountains"
        print("if you go in this may be you are out of chasing or rather difficult to go the next step.")
        transport = input("you notice there exists a canoe or you can go there by walk if you have energy.")
        if transport=='walk':
            print("if you go to right side there exists a newly formed bunglow there by you can walk 5min then you will reach the gate Later you will know the result.")
            print("you are unable to reached the light house.")
        elif transport=='canoe':
            print("you can reach the gate  faster than by walk,which is 10min faster than the walk.")
        else:
            print("invalid!!!")
            quit()
elif location=="scary jungle":
    print("welcome to the mighty nighty SCARY JUNGLE.Hope you can get better experience in it.")
    print("Note:Carry light coz it's dark,pay attention what you hear coz you'll dead if you don't!!")
    direction = input("there are two ways,which way would you prefer?(left/right):")
    if direction == "left":
        location = "the cops den"
        print("it can be easier to proceed to in this step and helps you to continue in the game....")
        transport = input("you notice there exists a bike or you can go there by walk if you have energy(and it will become to long).")
        if transport == 'walk':
            print(
                "if you go to left side there exists a house whch is called a cops den, now he can give you directions in order to go through the jungle.")
            print("now you completed the half of the game,press enter to continue....")
            press=input("Inorder to go further step press either(</>):")
            if press=="< ":
                print("continuee,follow the guidence properly:)")
            elif press=="> ":
                print("you might get scary for this,because you went to the lions den,congrats for going into the lions stomach.ALL THE BEST")
            else:
                print("exit the game^^^")
        elif transport == 'bike':
            print("you can reach the jungle fast but keep in mind that lights of the bike can let the wild creatures alive.Make sure no noise should come.")
            print("after you reach the jungle inorder to accomplish your goal follow the guidence given by us.")
        else:
            print("out of the chasing")
            press=input("Inorder to mouve further step you need to press(</>).")
            if press=="< ":
                print("by this you'll get the information about the mighty jungle.")
            elif press=="> ":
                print("It takes some time to proceed,after that you will find a different tree.")
                print("then go straight to the tree you'll find  away the interesting facts about the scary forest..:)")
    elif direction == "right":
        location = "river"
        print("to relax,you can swim in that without sound.")
        print("After that your goal is to cross the river.So to cross that river there are 2 mighty levels.")
        level=input("Here you experience two might levels,i.e..,Level-1 &Level-2:")
        if level=="1":
            print("in this there is a boat near you so that you can cross the river")
        elif level=="2":
            print("you can cross river by Ropes,it is mainly used in adventure trips.")
        else:
            print("dead")
            setting=input("Congrats you got keys to go the other level,to continue press Yes:")
            if setting=="yes":
                print("after finishing tthe above level,you'll notice a house near there,there by after reaching there you'll recieve the information about that jungle why its SCARY:")
            else:
                print("if not yes,then ur eaten by the creatures in the jungle.Opps,Better luck next time!!")
                quit()