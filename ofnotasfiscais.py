
def notasf():
    total_nota = []
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
                    imposto = ((valorBruto_nota*12)/100)
                    valorLiquido_nota = valorBruto_nota-imposto
                    print (f"O valor do imposto é {imposto}")
                    print("Valor liquido: %.2f " % valorLiquido_nota)
                    total_nota.append(n_nota)
                    total_nota.append(descricao_nota)
                    total_nota.append(valorBruto_nota)
                    total_nota.append(imposto)
                    total_nota.append(valorLiquido_nota)
                except:
                    print ("Favor digitar corretamente!")
            notaf2222()
        elif menu_nota == 2:
            try:  
                print ("Apagaremos todos os dados!")
                del (total_nota)
            except:
                print ("Lista vazia")
        elif menu_nota == 3:
            total_nota = []
            print ("Por Favor refaça o seu cadastro!")
            notaf2222()
        elif menu_nota == 4:
            try:
                print ("Aqui está o relatorio:")
                print (total_nota)
            except:
                print("A lista está vazia, volte.")
                return

                
            
notasf()