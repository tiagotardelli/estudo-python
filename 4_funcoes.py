nome = "H"
vida = 10
gravidade = 9.8
vivo = True

def ataque():
    print("Atacar")


def pulo():
    print("Pular")


def defesa():
    print("Defender")


def ataque_dano(valor):
    print("Dano: ",valor)


ataque()
pulo()
defesa()
ataque_dano(10)

if nome == "H":
    ataque()
