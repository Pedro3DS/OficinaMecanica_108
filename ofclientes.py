#def clientes():
from os import system
lcpf_cliente=[]
lrg_cliente=[]
lnome_cliente=[]
lfone_cliente=[]
lend_cliente=[]
lemail_cliente=[]
while True:
    menu=input("1-Registrar\n2-Excluir o cadastro de cliente\n3-alteração o cadastro\n4-Relatório\n0-sair\ndigite:")
    system('cls')
    if menu=='1':    
        system("cls")
        print("BEM VINDO AO CADASTRO DO CLIENTE")
        try: 
            cpf_cliente=int(input("digite seu cpf: "))
            rg_cliente=int(input("digite seu rg: "))
            nome_cliente=input("digite seu nome: ")
            fone_cliente=int(input("digite seu telefone: "))
            end_cliente=input("digite seu endereço: ")
            email_cliente=input("digite seu email: ")
        except ValueError:
            system("cls") 
            print("valor invalido, digite numeros inteiros sem ponto, virgula etc...")
            system("pause")
            system("cls")
        else: 
            system("cls")
            print("O usuário foi registrado com sucesso.")
            lcpf_cliente.append(cpf_cliente)
            lrg_cliente.append(rg_cliente)
            lnome_cliente.append(nome_cliente)
            lfone_cliente.append(fone_cliente)
            lend_cliente.append(end_cliente)
            lemail_cliente.append(email_cliente)
            system("pause")
    elif menu=='2':
            system("cls")
            print("BEM VINDO A EXCLUSÃO DO CLIENTE")
            cpf_cliente=input("CPF para ser excluido: ")
            if cpf_cliente in lcpf_cliente:
                print("O cliente foi excluido com sucesso.")
                index=lcpf_cliente.index(cpf_cliente)
                lcpf_cliente[index]=[]
                lrg_cliente[index]=[]
                lnome_cliente[index]=[]
                lfone_cliente[index]=[]
                lend_cliente[index]=[]
                lemail_cliente[index]=[]
                system('pause')
                system('cls')
            else:
                 system("cls")
                 print("CPF inexistente.")
                 system("pause")
                 system("cls")
    elif menu=='3':
       system("cls")
       print("BEM VINDO A ALTERAÇÃO DO CLIENTE\n")
       cpf_cliente=input("CPF do cliente a ser alterado: ")
       if cpf_cliente in lcpf_cliente:
            index=lcpf_cliente.index(cpf_cliente) 
            try:
                cpf_cliente=int(input("digite seu cpf:"))
                rg_cliente=int(input("digite seu rg: "))
                nome_cliente=input("digite seu nome: ")
                fone_cliente=int(input("digite seu telefone: "))
                end_cliente=input("digite seu endereço: ")
                email_cliente=input("digite seu email: ")
                system('pause')
                system('cls')
            except ValueError: 
                system("cls")
                print("valor invalido, digite numeros inteiros sem ponto, virgula etc...")
                system("pause")
                system("cls")
            else:
                system("cls")
                print("O cliente foi alterado com sucesso.")
                lcpf_cliente[index]=cpf_cliente
                lrg_cliente[index]=rg_cliente
                lnome_cliente[index]=nome_cliente
                lfone_cliente[index]=fone_cliente
                lend_cliente[index]=end_cliente
                lemail_cliente[index]=email_cliente
                system("pause")
                system("cls")
       else:
            system("cls")
            print("CPF inexistente.")
            system("pause")
            system("cls")
    elif menu=='4':
        system("cls")
        menu2=int(input("BEM VINDO AO RELATÓRIO DE CLIENTES\n1. Escolher Cliente\n2. Relatório Geral.\nDigite: "))
        if menu2==1:
            cpf_cliente=input("CPF do Cliente a ser consultado: ")
            if cpf_cliente in lcpf_cliente:
                index=lcpf_cliente.index(cpf_cliente)
                print(' seu cpf',lcpf_cliente[index],'\n','seu rg',lrg_cliente[index],'\n','seu nome',lnome_cliente[index],'\n','seu telefone',lfone_cliente[index],'\n','seu endereço',lend_cliente[index],'\n','seu email',lemail_cliente[index])
                system('pause')
                system('cls')
            else:
                system("cls")
                print("CPF inexistente.")
                system("pause")
                system("cls")
        elif menu2==2:
            print("\nCPF dos Clientes em Ordem: ")
            for i in lcpf_cliente:
                print(i)
            print("\nRG dos Clientes em Ordem: ")
            for i in lrg_cliente:
                print(i)
            print("\nNome dos Clientes em Ordem: ")
            for i in lnome_cliente:
                print(i)
            print("\nTelefone dos Clientes em Ordem: ")
            for i in lfone_cliente:
                print(i)
            print("\nEndereço dos Clientes em Ordem: ")
            for i in lend_cliente:
                print(i)
            print("\nEmail dos Clientes em Ordem: ")
            for i in lemail_cliente:
                print(i)
            system("pause")
            system("cls")
    elif menu=='0':
            system("cls")
            print("obrigado por utilizar o menu de cliente.")
            system("pause")
            system("cls")
            break
    else:
         system("cls")
         print("Opção inexistente.")
         system("pause")
         system("cls")