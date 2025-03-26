# --- Player, Character, Class
# Code funktioniert nicht weil bobby es nicht hinbekam

class Character:
    def __init__(self,name,character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.health = 100
        self. attack_power = 10
        self.defense = 10

    def setHealth(self,health):
        self.health = 100

    def attack(self):
        print ("attack")
    
    def take_damage(self,amount):
        self.health -= amount
        if self.health <=0:
            print(f"{self.name} ist tot.")
                   

class PlayerCharacter(Character):                                               #vererbung
    def __init__(self,name,character_class,player):
        super().__init__(name,character_class)  
        self.player = player                                         #superkonstrukor, damit INIT durchläuft
        self.inventory = []


class NPCCharacter(Character):
    def __init__(self,name,character_class):
        super().__init__(name, character_class)
        self.dropList = []



class CharacterClass:
    def __init__(self, className):
        self.className = className

    def setupCharacter(character):
        print("Abstract class no funtion")

class WarriorClass:
    def __init__(self):
        super().__init__("Warrior")

    def setupCharacter(character):
        character.health +=100

class MageClass(CharacterClass):
    def __init__(self):
        super().__init__("Mage")





c1 = Character ("Horst",WarriorClass())
p1 = PlayerCharacter("Willy",MageClass(),"Player1")


p1.take_damage(1000)





