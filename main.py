# menu.py

from motocicletas import *
from clientes import *

def exibir_menu():
    print("----- MENU -----")
    print("1. Adicionar motocicleta")
    print("2. Listar motocicletas")
    print("3. Buscar motocicleta")
    print("4. Atualizar motocicleta")
    print("5. Remover motocicleta")
    print("6. Adicionar cliente")
    print("7. Listar clientes")
    print("8. Buscar cliente")
    print("9. Atualizar cliente")
    print("10. Remover cliente")
    print("0. Sair")

def executar_opcao(opcao):
    if opcao == "1":
        id = input("Digite o ID da motocicleta: ")
        marca = input("Digite a marca da motocicleta: ")
        modelo = input("Digite o modelo da motocicleta: ")
        ano = input("Digite o ano da motocicleta: ")
        motocicleta = Motocicleta(id, marca, modelo, ano)
        adicionar_motocicleta(motocicleta)
        print("Motocicleta adicionada com sucesso!")
    elif opcao == "2":
        motocicletas = listar_motocicletas()
        if not motocicletas:
            print("Nenhuma motocicleta cadastrada.")
        else:
            for motocicleta in motocicletas:
                print(f"ID: {motocicleta.id}, Marca: {motocicleta.marca}, Modelo: {motocicleta.modelo}, Ano: {motocicleta.ano}")
    elif opcao == "3":
        id = input("Digite o ID da motocicleta: ")
        motocicleta = buscar_motocicleta(id)
        if motocicleta:
            print(f"ID: {motocicleta.id}, Marca: {motocicleta.marca}, Modelo: {motocicleta.modelo}, Ano: {motocicleta.ano}")
        else:
            print("Motocicleta não encontrada.")
    elif opcao == "4":
        id = input("Digite o ID da motocicleta: ")
        motocicleta = buscar_motocicleta(id)
        if motocicleta:
            marca = input("Digite a nova marca da motocicleta: ")
            modelo = input("Digite o novo modelo da motocicleta: ")
            ano = input("Digite o novo ano da motocicleta: ")
            motocicleta.marca = marca
            motocicleta.modelo = modelo
            motocicleta.ano = ano
            atualizar_motocicleta(motocicleta)
            print("Motocicleta atualizada com sucesso!")
        else:
            print("Motocicleta não encontrada.")
    elif opcao == "5":
        id = input("Digite o ID da motocicleta: ")
        motocicleta = buscar_motocicleta(id)
        if motocicleta:
            remover_motocicleta(id)
            print("Motocicleta removida com sucesso!")
        else:
            print("Motocicleta não encontrada.")
    elif opcao == "6":
        id = input("Digite o ID do cliente: ")
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        cliente = Cliente(id, nome, endereco, telefone)
        adicionar_cliente(cliente)
        print("Cliente adicionado com sucesso!")
    elif opcao == "7":
        clientes = listar_clientes()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(f"ID: {cliente.id}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, Telefone: {cliente.telefone}")
    elif opcao == "8":
        id = input("Digite o ID do cliente: ")
        cliente = buscar_cliente(id)
        if cliente:
            print(f"ID: {cliente.id}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, Telefone: {cliente.telefone}")
        else:
            print("Cliente não encontrado.")
    elif opcao == "9":
        id = input("Digite o ID do cliente: ")
        cliente = buscar_cliente(id)
        if cliente:
            nome = input("Digite o novo nome do cliente: ")
            endereco = input("Digite o novo endereço do cliente: ")
            telefone = input("Digite o novo telefone do cliente: ")
            cliente.nome = nome
            cliente.endereco = endereco
            cliente.telefone = telefone
            atualizar_cliente(cliente)
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")
    elif opcao == "10":
        id = input("Digite o ID do cliente: ")
        cliente = buscar_cliente(id)
        if cliente:
            remover_cliente(id)
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado.")
    elif opcao == "0":
        print("Encerrando o programa...")
        exit()
    else:
        print("Opção inválida. Por favor, tente novamente.")

def iniciar_aplicacao():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        executar_opcao(opcao)

if __name__ == '__main__':
    iniciar_aplicacao()

        
        
        
    








