monstros = ["monstro", "Rei", "monstro", "monstro", "Rei"]

def atacar():
    print("Atacar monstro")


def defender():
    print("Defender rei")

for n in monstros:
    if n == "monstro":
        atacar()
    elif n == "Rei":
        defender()