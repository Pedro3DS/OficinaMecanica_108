
def notasf():
    ltotal_nota = []
    menu_nota = 0
    while menu_nota != 5:
        try: 
            menu_nota = int(input("DIgite: ( 1 ) Nota fiscal ( 2 ) Exclusão ( 3 ) Alteração ( 4 ) Relatorio ( 5 ) Sair\n-> "))  
        except:
            print("DIgite um numero!")
        if menu_nota == 1:
            def notaf2222():
                try:
                    n_nota = int(input("DIgite o numero da nota: "))
                    descricao_nota = input("Descrição da nota: ")
                    valorBruto_nota = float(input("Digite o valor bruto: "))
                    imposto_nota = ((valorBruto_nota*12)/100)
                    valorLiquido_nota = valorBruto_nota-imposto_nota
                    print (f"O valor do imposto é {imposto_nota}")
                    print("Valor liquido: %.2f " % valorLiquido_nota)
                    ltotal_nota.append(n_nota)
                    ltotal_nota.append(descricao_nota)
                    ltotal_nota.append(valorBruto_nota)
                    ltotal_nota.append(imposto_nota)
                    ltotal_nota.append(imposto_nota)
                    ltotal_nota.append(valorLiquido_nota)
                except:
                    print ("Favor digitar corretamente!")
            notaf2222()
        elif menu_nota == 2:
            try:  
                print ("Apagaremos todos os dados!")
                del (ltotal_nota)
            except:
                print ("Lista vazia")
        elif menu_nota == 3:
            ltotal_nota = []
            print ("Por Favor refaça o seu cadastro!")
            notaf2222()
        elif menu_nota == 4:
           try:
                print ("Aqui está o relatorio:")
                for i in ltotal_nota:
                    print (i)
           except:
                print("A lista está vazia, volte.")
