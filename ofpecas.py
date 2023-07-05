def peca():
    from os import system as st
    while True:
        
        print("Bem vindo ao cadastro de peças!!! ;-)")
        a=int(input("1- Cadastro/ 2- Exclusão/ 3- Alteração/ 4- Relátorio\n"))
        if a == 1:
            lista = []
            lnome_peca = []
            lcod_peca = []
            lpreco_peca= []
            lqntd_peca= []
            nome_peca = input("Nome da peça: ")
            while True:
                try:
                    cod_peca = int(input("Código da peça: "))
                    preco_peca = float(input("Preço da peça: "))
                    qntd_peca = int(input("Quantidade de peças: "))
                except ValueError:
                    st("cls")
                    print("Digite somente números!!!")
                    st("pause")
                    continue
                else:
                    break
            lnome_peca.append(nome_peca)
            lcod_peca.append(cod_peca)
            lpreco_peca.append(preco_peca)
            lqntd_peca.append(qntd_peca) 
            lista.append(nome_peca)
            lista.append(cod_peca)
            lista.append(preco_peca)
            lista.append(qntd_peca) 
            st("cls") 
            print("Nome da peça:", nome_peca)
            print("Código da peça:", cod_peca)
            print("Preço da peça:", preco_peca)
            print("Quantidade:", qntd_peca)
            continue
        elif a == 2:
            while True:
                exclusão = input("Digite o Nome da peça para a exclusão: ")
                if exclusão in lnome_peca:
                    
                    index=lnome_peca.index(exclusão)
                    lnome_peca[index]=[]
                    lcod_peca[index]=[]
                    lpreco_peca[index]=[]
                    lqntd_peca[index]=[]
                
                else:
                    print("Este item não está cadastro")
                    break
        elif a == 3:
            print("Você está na opção de alteração do cadastro de peça ")
            while True:
                try:
                    alteração = input("Digite o Nome da peça para realizar a alteração desejada: ")
                except ValueError:
                    print("A peça indicada para realizar a alteração não está cadastrada")
                else:
                    break
                nome_peca = input("Nome da peça: ")
                alteração = lista.index(input("Digite o iten que deseja alterar ")) # pega o index do iten que vai ser substituido na lista
                if alteração in lista: # caso o indice for encontrado na lista
                    lista[alteração] = input("Digite o novo nome da peça ") # 
                    lista[alteração + 1] = input("Digite o novo código ") # index do item mais um já que o cadastrado é ordenado.
                    lista[alteração + 2] = input("Digite a nova quantidade ") # 
                    lista[alteração + 3] = input("Digite o novo Preço ")
                else:
                    print("Este item não está cadastro")
                    continue
                print(lnome_peca)
        elif a == 4:
            print(lista)
            