import random
global gold
gold = 0
global health
health = 100
def Qsix():
    global gold
    global health
    global weapon 
    options2 = ["Fight the dragon with your weapon", "Try to bond with the dragon."]
    print("When the cage door opens, you are face to face with a huge black dragon. You had no idea that dragons even existed. You were completely unprepared.")
    print ("Here are your options")
    for each in options2:
        print(str(options2.index(each)+1)+". " + each)
    lastanswer = input("What do you choose? ")
    if lastanswer == "1":
        print("You started to fight with your " + weapon + " and lost. The dragon scorched you to bits")
        print("You have failed.")
    if lastanswer == "2":
        print("Congratulations! You successfully put your hand on the dragon with it trusting you. You guided the dragon back into the cage and collected those 5 coins. You are on your way home!")
def Qfive():
    global health
    global gold
    global weapon
    print( 
    "You find your way to the city and somehow get into the university. "
    "The people put you in the infirmary and nurse you back to health. "
    "When the nurses leave, you overhear someone talking about a dragon fight outside the door. "
    "Something about gaining coins. You decide to explore about it. "
    "You explore and find that the fight is to the death and it gives you 5 coins if you manage to scare the beast back into its cage or kill it."
)
    arsenal = ["axe", "dagger", "trident"]
    print ("You get to the arena and are in front of an arsenal of 3 weapons") 
    for each in arsenal:
        print(str(arsenal.index(each)+1)+". " + each)
    print ("However, you are pushed in without being able to choose one, so someone throws in a ")
    weaponnumber = random.randint(0,2)
    weapon = arsenal[weaponnumber]
    print (weapon)
    Qsix()
def Qfour():
    global health
    global gold
    options = ["Walk around the creature and lose the oppurtunity to gain coins", "fight and risk your life for the coins?"]
    print ("You have no idea where you are going, so you plan to visit the city nearby. On your way, you encounter a vicious creature with a pouch full of gold.")
    print("You have 2 options: ")
    for each in options:
        print(str(options.index(each)+1)+". " + each)
    qfour = input("What do you want to do? ")
    if qfour == "1":
        print("You try to creep around the creature, but the thing sees you anyways and takes 200 health. You failed your mission in the worst possible way.")
        health = health - 200
        print ("health : " + str(health))
        print ("gold : " + str(gold))
        Qfive()
    if qfour == "2":
        print("You use your knife and successfully kill the creature. However, in the process, the coins in the pouch fall down the nearby cliff. You are only able to recover 3.")
        print("Fighting the creature exerts you and you lose 25 health.")
        health = health - 50
        gold = gold + 2
        print ("health : " + str(health))
        print ("gold : " + str(gold))
        Qfive()

def Qthree():
    global health
    global gold
    qthree = input("The second you leave your house a fortune teller comes up to you and says 'Welcome, traveler. Roll this dice and you may earn good luck!'say 'roll'")
    if qthree == "roll":
        dice = random.randint(1,6)
        print ("You rolled a " + str(dice))
        if dice <= 3:
            print ("The fortune teller tells you that you have gained good luck on your journey! She gives you 25 health, a knife, and directions to the nearest city.")
            health = health + 25
            print ("health : " + str(health))
            print ("gold : " + str(gold))
            Qfour()
        if dice > 3:
            print ("The fortune teller tells you that you have gained bad luck on your journey! She takes 25 health from you.")    
            health = health - 25
            print ("health : " + str(health))
            print ("gold : " + str(gold))
            Qfour()
print("hello fellow traveler! Today is a fine and beautiful day.")
name = input("What is your name? ")
print("Hello, ",name,". It is 3012 AE and you are on Isle of Berk. We are your guides until you die, I mean win. You currently have 0 gold and 100 health."
      "You want to go home? Get 5 gold coins to afford a ticket and the resources to get there. Good luck, the journey is far from safe!")
qone = input("Are you ready? ")
if qone == "yes":
    print("Let's go! You wake up in a room full of strange people. They stare at you, curious and expecting answers from you.")
    qtwo = input("Do you 1) tell them about you or 2) Ignore them and go about your business? ")
    if qtwo == "1":
        print ("The strange people introduce themselves and take care of you. In the morning, they give you 1 coin to start your journey.")
        gold = gold + 1
        print ("health : " + str(health))
        print ("gold : " + str(gold))
    if qtwo == "2":
        print ("The Dragonslayers are offended by the sheer disrespect you have for them. The kick you out without anything for the journey. You lose 25 health.")
        health = health - 25
    Qthree()
else:
    print("FAIL! You die. Please start over.")
