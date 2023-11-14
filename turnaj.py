import random


class Rytir:
    
    def __init__(self, jmeno, HP, ATK, DEF, zbran, puvod):
        self.jmeno = jmeno
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.zbran = zbran
        self._puvod = puvod
    
    def zautoc(self, protivnik):
        return self.ATK + self.zbran.ATK - protivnik.DEF

    @property
    def puvod(self):
        if self._puvod == "king":
            return self._puvod
        if self._puvod == "pawn":
            return "Lets not care about my parents..."

    @puvod.setter
    def puvod(self, value):
        if value == "king":
            self._puvod = "king"
        if value != "king":
            self.puvod == "Lets not care about my parents..."
        if self._puvod == "pawn":
            self.puvod == "Lets not care about my parents..."


    def __str__(self):
            return f"Jmeno: {self.jmeno}, HP: {self.HP}, Zbran: {self.zbran.jmeno} Puvod: {self.puvod}"



class Zbran:
    
    def __init__(self, jmeno, ATK):
        self.jmeno = jmeno
        self.ATK = ATK


class Husta_zbran(Zbran):
    def __init__(self, jmeno, ATK, magic):
        super().__init__(jmeno, ATK)
        self.magic = magic
        magic = magic + ATK


class Turnaj:
    
    def __init__(self):
        self.seznam_rytiru = []
    
    def registrace(self, rytir):
        self.seznam_rytiru.append(rytir)
    
    def duel(self):
        r1 = random.choice(self.seznam_rytiru)
        r2 = random.choice(self.seznam_rytiru)
        while r1 == r2:
            r2 = random.choice(self.seznam_rytiru)
        while r1.HP >= 0 and r2.HP >= 0:
            r2.HP -= r1.zautoc(r2)
            r1.HP -= r2.zautoc(r1)
        if r1.HP or r2.HP == 0:
            print(r1)
            print(r2)
        if r1.HP >= r2.HP:
            print("král: Vážený bojovník nahoře vyhrál")
        if r2.HP >= r1.HP:
            print("král: Vážený bojovník dole vyhrál")


turnaj = Turnaj()
dragon_slayer = Zbran("Dragonslayer", 50)
excalibur = Zbran("Excalibur", 30)
magicky_klacek1 = Husta_zbran("hustý klacek", ATK = 100, magic = 60)
magicky_klacek2 = Husta_zbran("magický klacek", ATK = 200, magic = 60)


richard = Rytir("Richard", HP = 100, ATK = 20, DEF = 10, zbran = dragon_slayer, puvod = "king")
pepa = Rytir("Pepík", HP = 180, ATK = 25, DEF = 25, zbran = excalibur, puvod = "pawn")


arthur = Rytir("Arthur", HP = 300, ATK = 30, DEF = 20, zbran = excalibur, puvod = "king")
merlin = Rytir("Merlin", HP = 200, ATK = 50, DEF = 20, zbran = magicky_klacek1, puvod = "pawn")
brumbal = Rytir("Albus", HP = 600, ATK = 63, DEF = 60, zbran = magicky_klacek2, puvod = "hustý cápek")


richard.puvod = "king"
brumbal.puvod = "king"


turnaj.registrace(richard)
turnaj.registrace(pepa)
turnaj.registrace(arthur)
turnaj.registrace(merlin)
turnaj.registrace(brumbal)
turnaj.duel()
