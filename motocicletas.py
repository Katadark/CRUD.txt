# motocicletas.py

class Motocicleta:
    def __init__(self, id, marca, modelo, ano):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

def adicionar_motocicleta(motocicula):
    with open('motocicletas.txt', 'a') as arquivo:
        arquivo.write(f'{motocicula.id},{motocicula.marca},{motocicula.modelo},{motocicula.ano}\n')

def listar_motocicletas():
    with open('motocicletas.txt', 'r') as arquivo:
        motocicletas = []
        for linha in arquivo:
            id, marca, modelo, ano = linha.strip().split(',')
            motocicleta = Motocicleta(id, marca, modelo, ano)
            motocicletas.append(motocicleta)
        return motocicletas

def buscar_motocicleta(id):
    with open('motocicletas.txt', 'r') as arquivo:
        for linha in arquivo:
            motocicleta = linha.strip().split(',')
            if motocicleta[0] == id:
                return Motocicleta(motocicleta[0], motocicleta[1], motocicleta[2], motocicleta[3])
        return None

def atualizar_motocicleta(motocicula):
    motocicletas = listar_motocicletas()
    with open('motocicletas.txt', 'w') as arquivo:
        for motocicleta in motocicletas:
            if motocicleta.id == motocicula.id:
                arquivo.write(f'{motocicula.id},{motocicula.marca},{motocicula.modelo},{motocicula.ano}\n')
            else:
                arquivo.write(f'{motocicleta.id},{motocicleta.marca},{motocicleta.modelo},{motocicleta.ano}\n')

def remover_motocicleta(id):
    motocicletas = listar_motocicletas()
    with open('motocicletas.txt', 'w') as arquivo:
        for motocicleta in motocicletas:
            if motocicleta.id != id:
                arquivo.write(f'{motocicleta.id},{motocicleta.marca},{motocicleta.modelo},{motocicleta.ano}\n')
