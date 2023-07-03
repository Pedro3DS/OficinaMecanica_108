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
    if menu==1:    
        system("cls")
        print("BEM VINDO AO CADASTRO DO CLIENTE")
        try: 
            cpf_cliente=(input("digite seu cpf: "))
            lcpf_cliente.append(cpf_cliente)
            rg_cliente=(input("digite seu rg: "))
            lrg_cliente.append(rg_cliente)
            nome_cliente=input("digite seu nome: ")
            lnome_cliente.append(nome_cliente)
            fone_cliente=int(input("digite seu telefone: "))
            lfone_cliente.append(fone_cliente)
            end_cliente=input("digite seu endereço: ")
            lend_cliente.append(end_cliente)
            email_cliente=input("digite seu email: ")
            lemail_cliente.append(email_cliente)
            system('pause')
            system('cls')
        except ValueError: 
            print("valor invalido...")
    if menu==2:
            system("cls")
            print("BEM VINDO A EXCLUSÃO DO CLIENTE")
            if cpf_cliente in lcpf_cliente:
                index=lcpf_cliente.index(cpf_cliente)
                lcpf_cliente[index]=[]
                lrg_cliente[index]=[]
                lnome_cliente[index]=[]
                lfone_cliente[index]=[]
                lend_cliente[index]=[]
                lemail_cliente[index]=[]
                system('pause')
                system('cls')
    if menu==3:
       system("cls")
       print("BEM VINDO A ALTERAÇÃO DO CLIENTE\n")
       if cpf_cliente in lcpf_cliente:
            index=lcpf_cliente.index(cpf_cliente) 
            try:
                cpf_cliente=float(input("digite seu cpf:"))
                rg_cliente=float(input("digite seu rg: "))
                nome_cliente=input("digite seu nome: ")
                fone_cliente=int(input("digite seu telefone: "))
                end_cliente=input("digite seu endereço: ")
                email_cliente=input("digite seu email: ")
                system('pause')
                system('cls')
            except ValueError: 
                print("valor invalido...")
    if menu==4:
        system("cls")
        print("BEM VINDO AO RELATÓRIO DO CLIENTE\n")
        if cpf_cliente in lcpf_cliente:
            index=lcpf_cliente.index(cpf_cliente)
            print(' seu cpf',lcpf_cliente[index],'\n','seu rg',lrg_cliente[index],'\n','seu nome',lnome_cliente[index],'\n','seu telefone',lfone_cliente[index],'\n','seu endereço',lend_cliente[index],'\n','seu email',lemail_cliente[index])
            system('pause')
            system('cls')
    if menu==0:
            system("cls")
            print("obrigado por utilizar o menu de cliente.")
            system("pause")
            system("cls")
            break