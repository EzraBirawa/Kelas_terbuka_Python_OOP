class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower) #self dari sini masuk kedalam parameter "lawan" dalam fungsi diserang()

    def diserang(self, lawan, attackPower_lawan): #karena pada fungsi serang() selfnya sniper, masuk ke parameter lawan sebagai sniper
        print(f"{self.name} diserang oleh {lawan.name}")
        attack_diterima = attackPower_lawan/self.armorNumber
        print(f"serangan terasa: {str(attack_diterima)}")
        self.health -= attack_diterima
        print(f"darah {self.name} tersisa {self.health}")


sniper = Hero('sniper',100,10,5)
jupri = Hero("jupri",100,50,10)
rikimaru = Hero('rikimaru',100,20,10)

sniper.serang(jupri)