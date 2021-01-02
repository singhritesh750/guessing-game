flag = 0  # represents player is not smarting with giving out of box guesses
option1 = "Y"  # to ask for next chance
option2 = "Y"  # to ask for interest to play again
guess_number = 0  # initializing
while option2.upper() == "Y":
    print("check1")
    # as for name and detail of players
    print("Hello mate!")
    print("Please,enter your name")
    name = input()
    print("and your gender is: M OR F")
    gender = input()
    if gender.upper() == "M":
        print("check2")
        print("Okay Sir.I got it")
    elif gender.upper() == "F":
        print("check3")
        print("Ooo well well.Dear Mam\nLet me assure you it is a bit tough game\nBut anyway, you will enjoy it")
    else:
        print("check4")
        print("YOU HAVE ENTERED SOMETHING OTHER THAN M//F\nBUT ALRIGHT WE WILL ENTERTAIN IT")

    print("Thank you for your assistance!")
    print("Hope you will enjoy the game")

    # ask for numbers
    print("Please guess two number you want to guess between")
    print("Enter the higher value")
    larg = float(input())
    print("Enter the lower value")
    s = float(input())
    diff = larg - s

    # generate a random number
    import random

    print("check5")
    random_1 = random.randint(s, larg)
    print("A random number has been generated for the game")
    # print(random_1)

    flag = 0
    option1 = "Y"
    option2 = "Y"

    while flag == 0 and (option1.upper()) == "Y" and (
            option2.upper()) == "Y":  # to check player is not smarting with giving out of box guesses and to check for
        # interest to play to check for next chance
        print("check6")
        print("Now enter the number you are guessing")
        try:
            guess_number = float(input())
            # c= input("\n")   #can use this code to assign input value to check what data_type is inputted

        except:
            print("Are you tying to be smart? This is incorrect input")
            print("Wanna try again y/n \n")
            option1 = input()
            flag = 0
            if option1.lower == "y":
                continue
            if option1.lower() != 'y':
                option2 = option1
                break

            # check for guessed number between the entered number
        if guess_number < s or guess_number > larg:  # check for out of box guesses
            print("check7")
            print("You have guessed a wrong number")
            print("Wanna try again y/n \n")
            option1 = input()
            flag = 0  # represents player is smarting with giving out of box guesses

        else:
            print("check8")
            # guess_number = float(c) #can use this code to assign input value when confirm that its a float
            flag = 1  # represents player is not smarting with giving out of box guesses
            # pass

            # match them
            # if match not found show wrong selection message and again ask for guessing
            if guess_number != random_1:
                print("check9")
                print("Its a Bad choice")
                if s <= guess_number <= larg:  # Simplify chained comparison if guess_number >=s and guess_number <= low
                    print("check10")
                    # Simplify chained comparison guess_number >= s and guess_number <= (s + diff / 4)
                    if s <= guess_number <= (s + diff / 4):
                        print("check23")
                        if random_1 <= (s + diff / 4):
                            print("check11")
                            print("Nice try!Close enough")
                            print("Wanna try again y/n \n")
                            option1 = str(input())
                            flag = 0
                        else:
                            print("check12")
                            print("Guessing less")
                            print("Wanna try again y/n \n")
                            option1 = str(input())
                            flag = 0
                    # Simplify chained comparison elif guess_number <= low and guess_number >= (low - diff / 4)
                    elif larg >= guess_number >= (larg - diff / 4):
                        print("check24")
                        if random_1 >= (larg - diff / 4):
                            print("check13")
                            print("Nice try!Close enough")
                            print("Wanna try again y/n \n")
                            option1 = str(input())
                            flag = 0
                        else:
                            print("check14")
                            print("Guessing high")
                            print("Wanna try again y/n \n")
                            option1 = str(input())
                            flag = 0
                    # Simplify chained comparison elif guess_number >= (s + diff /4)and guess_number<=(low - diff/4)
                    elif (s + diff / 4) <= guess_number <= (larg - diff / 4):
                        print("check15")
                        # Simplify chained comparison if random_1 >= (s + diff / 4) and random_1 <= (low - diff / 4):
                        if (s + diff / 4) <= random_1 <= (larg - diff / 4):
                            print("check16")
                            # if (random_1 >=guess_number and (random_1 - diff / 8) <= guess_number) or (
                            # guess_number >= random_1 and (guess_number - diff / 8) <= random_1):
                            if (random_1 >= guess_number >= (random_1 - diff / 8)) or (
                                    guess_number >= random_1 >= (guess_number - diff / 8)):
                                print("check17")
                                print("Nice try! but Guess again. You are very close")
                                print("Wanna try again y/n \n")
                                option1 = str(input())
                                flag = 0
                            elif random_1 <= guess_number:
                                print("check18")
                                print("Guessing high")
                                print("Wanna try again y/n \n")
                                option1 = str(input())
                                flag = 0
                            else:  # if(guess_number -6 >=1 && guess_number -6<=20 )&&(random_1 -6>=1 && random_1-6<=20)
                                print("check19")                         #print(name"you are guessing it very low ")
                                print("Guessing low")
                                # elif(guess_number>1&&guess_number<20)&&(random_1-6>=1&&random_1-6<=20)
                                print("Wanna try again y/n \n")  # print("Oh! "name" You are close ")
                                option1 = str(input())  # print("Oh! "name" You are close ")
                                flag = 0  # elif guess_number + 5 <= 20
                        else:  # print(name" you are guessing it very high")
                            print("check20")
                            if guess_number >= random_1:  # elif guess_number < 20
                                print("check21")
                                if guess_number - diff / 8 <= random_1:  # print("")
                                    print("close")                       #elif guess_number>
                                    print("Wanna try again y/n \n")
                                    option1 = str(input())
                                    flag = 0
                                else:
                                    print("guessing high")
                                    print("Wanna try again y/n \n")
                                    option1 = str(input())
                                    flag = 0
                            elif guess_number <= random_1:
                                print("check22")
                                if random_1 - diff / 8 <= guess_number:
                                    print("close")
                                    print("Wanna try again y/n \n")
                                    option1 = str(input())
                                    flag = 0
                                else:
                                    print("guessing low")
                                    print("Wanna try again y/n \n")
                                    option1 = str(input())
                                    flag = 0
            # if match found greet with beautiful message
            elif guess_number == random_1 and flag == 1:
                print("congrats", name, " ! you get that very correct.\nGreat job")
                print("wanna play again y/n ")
                option1 = str(input())
                print("wanna play new game y/n ")
                option2 = str(input())

if option2.upper() != "Y":
    print("It's alright if you are not interested\nWe will play next time")
