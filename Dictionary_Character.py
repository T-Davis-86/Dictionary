from Dictionary_Class import Dictionary
class Character():
    def __init__(self,name):
        self._name = name
        self.health_pt = 100
        self.mana_pt = 100
        self.exper = 1
        self.speed = 1
        self._char = []
        self.add_player()
    
    def add_player(self):
        self._char.append(Dictionary(self._name))

    def _get_player(self, x = 0):
        if x == len(self._char):
            return  
        character = self._char[x]
        for key, value in character._data.items():
            print(key, ":", value)
        print()
        self._get_player(x + 1)
 
    def cast_spell(self, x = 0):
        character = self._char[x]
        if character._data["Mana"] >= 10:
            character._data["Mana"] -= 10
            self.exp_incr()
        else:
            print("Mana too low!")

    def take_hit(self,x = 0):
        character = self._char[x]
        if character._data["Health"] <= 25: 
            print("Player has Died!")
            self._char.pop(x)
        else:
            character._data["Health"] -= 25
            self._get_player()

    def exp_incr(self, x = 0):
        character = self._char[x]
        character._data["Experience"] += 2
        character._data["Speed"] += .5
        self._get_player()