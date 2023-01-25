import random


class Player:
    def __init__(self):
        self.playerList = []
        self.numPlayers = int(input("How many people are going to be playing"))

        for z in range(self.numPlayers):
            self.playerList.append(input("What is your name?"))
        print(self.playerList)



class GamePlay:

    def __init__(self):
        z = Player()
        self.list_of_suspects = ["Mrs. Bob", "Mr. Joe", "Billy", "Tim"]
        self.list_of_weapons = ["stick", "keyboard","shoe", "door handle"]
        self.list_of_rooms = ["bathroom", "laundry room", "bedroom", "dining room"]


        self.whowasit = {"Suspect" : self.list_of_suspects.pop(random.randrange(0,len(self.list_of_suspects))), "Weapons" : self.list_of_weapons.pop(random.randrange(0,len(self.list_of_weapons))), "Room" : self.list_of_rooms.pop(random.randrange(0,len(self.list_of_rooms)))}
        print(self.whowasit)
        self.current_player = 0
        guesscount= 0
        murdererCopy = self.list_of_suspects.copy()
        weaponCopy = self.list_of_weapons.copy()
        roomCopy = self.list_of_rooms.copy()

        print(murdererCopy, weaponCopy, roomCopy)

        while z.playerList.__len__() > 0:
            currentPlay = z.playerList.pop(0)
       # self.murderer = {'Suspect': self.list_of_suspects.pop(random.randrange(0,len(self.list_of_suspects)))}
        #print(self.murderer)
        #self.weapon = {'Weapon': self.list_of_weapons.pop(random.randrange(0,len(self.list_of_weapons)))}
       # print(self.weapon)
        #self.room = {'Room': self.list_of_rooms.pop(random.randrange(0,len(self.list_of_rooms)))}
        #print(self.room)

            action= input("What do you want to do?" + str(currentPlay) + "\n" "Type room to enter and investigate a room" "\n" "Type i to interrogate a suspect" "\n" "Type guess to guess a suspect")

            if action == "room":
                print("You enter the room: " + random.choice(roomCopy) + " and find a " + random.choice(weaponCopy))
            if action == "i":
                print("You interrogate: " + random.choice(murdererCopy) + " and find that they are not the murderer.")

            z.playerList.append(currentPlay)


            if action == "guess":

                murdererguess = input("Who is the murderer?")
                if murdererguess == self.whowasit["Suspect"]:
                    guesscount = guesscount + 1
                    print(guesscount)

                weaponguess = input("Which weapon did the killer use?")
                if weaponguess == self.whowasit["Weapons"]:
                    guesscount = guesscount + 1


                roomguess = input("which room did the murder take place?")
                if roomguess == self.whowasit["Room"]:
                    guesscount = guesscount + 1


                if guesscount == 3:
                    print("Wow. great work! You solved the case!")
                    z.playerList.clear()
                if guesscount < 3:
                    print("Oh no! You guessed wrong. Try harder next time")
                    z.playerList.pop(z.playerList.__len__() - 1)




#options = input("What do you want to do?" "\n" "type r to enter room" )

        # Here the user is asked to enter the name first
        #if options == "r":
            #print("You enter the" + self.roomCopy.peek(random.randrange(0, len(self.list_of_rooms.copy()))))





if __name__ == '__main__':
    GamePlay()
