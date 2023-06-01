# clientes.py

class Cliente:
    def __init__(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

def adicionar_cliente(cliente):
    with open('clientes.txt', 'a') as arquivo:
        arquivo.write(f'{cliente.id},{cliente.nome},{cliente.endereco},{cliente.telefone}\n')

def listar_clientes():
    with open('clientes.txt', 'r') as arquivo:
        clientes = []
        for linha in arquivo:
            id, nome, endereco, telefone = linha.strip().split(',')
            cliente = Cliente(id, nome, endereco, telefone)
            clientes.append(cliente)
        return clientes

def buscar_cliente(id):
    with open('clientes.txt', 'r') as arquivo:
        for linha in arquivo:
            cliente = linha.strip().split(',')
            if cliente[0] == id:
                return Cliente(cliente[0], cliente[1], cliente[2], cliente[3])
        return None

def atualizar_cliente(cliente):
    clientes = listar_clientes()
    with open('clientes.txt', 'w') as arquivo:
        for c in clientes:
            if c.id == cliente.id:
                arquivo.write(f'{cliente.id},{cliente.nome},{cliente.endereco},{cliente.telefone}\n')
            else:
                arquivo.write(f'{c.id},{c.nome},{c.endereco},{c.telefone}\n')

def remover_cliente(id):
    clientes = listar_clientes()
    with open('clientes.txt', 'w') as arquivo:
        for cliente in clientes:
            if cliente.id != id:
                arquivo.write(f'{cliente.id},{cliente.nome},{cliente.endereco},{cliente.telefone}\n')
