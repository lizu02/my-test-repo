# --- Player, Character, Class

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.health = 100
        self.attack_power = 10
        self.defense = 10
        self.character_class.setupCharacter(self)
    
    def setHealth(self, health):
        self.health = health
    
    def attack(self):
        print("Attack!")
        
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} ist verstorben")
            
    def __str__(self):
        return f"Hallo ich heisse {self.name} ich bin ein {self.character_class.class_name} ich habe eine Angriffskraft von {self.attack_power}"

class PlayerCharacter(Character):
    def __init__(self, name, character_class, player):
        super().__init__(name, character_class)
        self.player = player
        self.inventory = [] 
        
class NpcCharacter(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.dropList = []
      
class WarriorNpcCharacter(NpcCharacter):
    def __init__(self, name):
        super().__init__(name, WarriorClass())
        
    
class CharacterClass:
    def __init__(self, class_name):
        self.class_name = class_name
        
    def setupCharacter(self, character):
        raise Exception ("Not Implemented")
    
class WarriorClass(CharacterClass):
    def __init__(self):
        super().__init__("Warrior")
        
    def setupCharacter(self, character):
        character.health = 150
        character.defense = 200
        character.attack_power = 150

class MageClass(CharacterClass):
    def __init__(self):
        super().__init__("Mage")   
    
    def setupCharacter(self, character):
        character.attack_power = 300 
        
class RogueClass(CharacterClass):
    def __init__(self):
        super().__init__("Rogue")
    
    def setupCharacter(self, character):
        character.health = 10
        
c1 = NpcCharacter("Horst", WarriorClass())
c2 = NpcCharacter("Werner", RogueClass())
p1 = PlayerCharacter("Hansli", MageClass(), "Player1")

cc1 = WarriorNpcCharacter("Fritz")

print(cc1)