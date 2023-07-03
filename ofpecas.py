def peca():
    import os
    while True:
        print("Bem vindo ao cadastro de peças!!! ;-)")
        a=int(input("1- Cadastro/ 2- Exclusão/ 3- Alteração/ 4- Relátorio"))
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
                    os.system("cls")
                    print("Digite somente números!!!")
                    os.system("pause")
                    continue
                else:
                    break
            lnome_peca.append(nome_peca)
            lcod_peca.append(cod_peca)
            lpreco_peca.append(preco_peca)
            lqntd_peca.append(qntd_peca) 
            os.system("cls") 
            print("Nome da peça:", nome_peca)
            print("Código da peça:", cod_peca)
            print("Preço da peça:", preco_peca)
            print("Quantidade:", qntd_peca)
            continue
        elif a == 2:
            print("Você escolheu a opção de exclusão do cadastro de peça ")
            while True:
                try:
                    exclusão = input("Digite o Nome da peça para a exclusão: ")
                except:
                    print("A peça indicada para a exclusão não está cadastrada")
                else:
                    break
                if exclusão in lnome_peca:
                    index=lnome_peca.index(exclusão)
                    lnome_peca[index]=[]
                    lcod_peca[index]=[]
                    lpreco_peca[index]=[]
                    lqntd_peca[index]=[]
                else:
                    print("Este item não está cadastro")
                    continue
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
                if alteração in lnome_peca:
                    index=lnome_peca.index(alteração)
                    lnome_peca[index]=[nome_peca]
                    lcod_peca[index]=[cod_peca]
                    lpreco_peca[index]=[preco_peca]
                    lqntd_peca[index]=[qntd_peca]
                else:
                    print("Este item não está cadastro")
                    continue
                print(lnome_peca)
        elif a == 4:
            print(lnome_peca)

peca()