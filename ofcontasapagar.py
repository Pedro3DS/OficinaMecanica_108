def contasapagar():
    import os
    lnome_conta = []
    ltipo_conta = []
    ldata_conta = []
    lvalor_conta = []
    inicio = 1
    while True:
        try:
            print("+"+"="*39+"+")
            print("I| Bem Vindo ao Menu de Contas a Pagar |I")
            print("-"*41)
            inicio = int(input("I| Digite Qual Opção Deseja:\n(1) >> Cadastro de Conta\n(2) >> Alterar Conta\n(3) >> Exclusão de Conta\n(4) >> Relatório\n(0) >> Sair\n>> "))
        except ValueError:
            print("-"*33)
            print("I| Erro | Escolha uma das Opções|")
        
        if inicio == 1:
            while True:
                try:
                    print("-"*23)
                    print("I| Cadastro de Conta I|")
                    print("-"*23)
                    nome_conta = input("I| Digite o Nome do Responsável pela Conta: ")
                    tipo_conta = input("I| Digite o Tipo da Conta: ")
                    data_conta = input("I| Digite a Data de Vencimento: ")
                    valor_conta = float(input("I| Digite o Valor da Conta: "))
                except ValueError:
                    print("-"*27)
                    print("I| Erro | Dados Invalidos |")
                    print("I| Tente Novamente |")
                else:
                    lnome_conta.append(nome_conta)
                    ltipo_conta.append(tipo_conta)
                    ldata_conta.append(data_conta)
                    lvalor_conta.append(valor_conta)
                    print("-"*36)
                    print("I| Cadastro Realizado com Sucesso I|")
                    print("-"*36)
                    os.system("pause")
                    os.system("cls")
                    break

        elif inicio == 2:
            try:
                print("-"*19)
                print("I| Alterar Conta I|")
                print("-"*19)
                nome_conta = input("I| Digite o Nome do Responsável pela Conta: ")
            except ValueError:
                print("-"*43)
                print("I| Erro | Dados Informado de Forma Errada |")
                print("I| Tente Novamente |")
            except:
                print("-"*29)
                print("I| Cadastro não Encontrado I|")
                print("I| Tente Novamente |")
            else:
                if nome_conta in lnome_conta:
                    i = lnome_conta.index(nome_conta)
                    while True:
                        try:
                            print("-"*40)
                            print("I| Informe os Dados a Serem Alteradas I|")
                            nome_conta = input("I| Digite o Nome do Responsável pela Conta: ")
                            tipo_conta = input("I| Digite o Tipo da Conta: ")
                            data_conta = input("I| Digite a Data de Vencimento: ")
                            valor_conta = float(input("I| Digite o Valor da Conta: "))
                        except ValueError:
                            print("-"*43)
                            print("I| Erro | Dados Informado de Forma Errada |")
                            print("I| Tente Novamente |")
                        else:
                            lnome_conta[i] = nome_conta
                            ltipo_conta[i] = tipo_conta
                            ldata_conta[i] = data_conta
                            lvalor_conta[i] = valor_conta
                            print("-"*39)
                            print("I| Alterações Realizadas com Sucesso I|")
                            print("-"*39)
                            os.system("pause")
                            os.system("cls")
                            break
                else:
                    print("-"*40)
                    print("I| Nome do Responsável não Encontrado I|")
                    os.system("pause")
                    os.system("cls")
        
        elif inicio == 3:
            try:
                print("-"*23)
                print("I| Exclusão de Conta I|")
                print("-"*23)
                nome_conta = input("I| Digite o Nome do Responsável pela Conta: ")
            except ValueError:
                print("-"*43)
                print("I| Erro | Dados Informado de Forma Errada |")
                print("I| Tente Novamente |")
            except:
                print("-"*29)
                print("I| Cadastro não Encontrado I|")
                print("I| Tente Novamente |")
            else:
                if nome_conta in lnome_conta:
                    i = lnome_conta.index(nome_conta)  
                    lnome_conta[i] = []
                    ltipo_conta[i] = []
                    ldata_conta[i] = []
                    lvalor_conta[i] = []
                    print("-"*39)
                    print("I| Exclusão Realizadas com Sucesso I|")
                    print("-"*39)
                    os.system("pause")
                    os.system("cls")          
                else:
                    print("-"*40)
                    print("I| Nome do Responsável não Encontrado I|")
                    os.system("pause")
                    os.system("cls")
        
        elif inicio == 4:
            try:
                print("-"*24)
                print("I| Relatório de Conta I|")
                print("-"*24)
                nome_conta = input("I| Digite o Nome do Responsável pela Conta: ")
            except ValueError:
                print("-"*43)
                print("I| Erro | Dados Informado de Forma Errada |")
                print("I| Tente Novamente |")
            except:
                print("-"*29)
                print("I| Cadastro não Encontrado I|")
                print("I| Tente Novamente |")
            else:
                if nome_conta in lnome_conta:
                    i = lnome_conta.index(nome_conta)  
                    print(f"I| Nome do Responsável: {lnome_conta[i]}")
                    print(f"I| Tipo de Conta: {ltipo_conta[i]}")
                    print(f"I| Data de Vencimento: {ldata_conta[i]}") 
                    print(f"I| Valor da Conta: R${lvalor_conta[i]}")
                    print("-"*39)
                    os.system("pause")
                    os.system("cls")          
                else:
                    print("-"*40)
                    print("I| Nome do Responsável não Encontrado I|")
                    os.system("pause")
                    os.system("cls")  
        
        elif inicio == 0:
            print("-"*42)
            print("I| Obrigado por Utilizar Contas a Pagar I|")
            print("I| Volte Sempre")
            break
        
        else:
            print("-"*20)
            print("I| Opção Invalida I|")
            os.system("pause")
            os.system("cls")  