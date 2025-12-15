def main():
    brawler_aragorn = Brawler('Aragorn', 4, 4)
    brawler_gimli = Brawler('Gimli', 2, 7)
    brawler_legolas = Brawler('Legolas', 7, 7)
    brawler_frodo = Brawler('Frodo', 3, 2)
    fight(brawler_aragorn, brawler_gimli)
    fight(brawler_legolas, brawler_frodo)

# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(f1, f2):
    print(f"{f1.name}: {f1.power} power")
    print(f"{f2.name}: {f2.power} power")
    if f1.power > f2.power:
        print(f"{f1.name} wins!")
    elif f1.power < f2.power:
        print(f"{f2.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()
