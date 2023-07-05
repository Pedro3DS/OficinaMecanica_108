def veic():
    import os
    lplaca_veic = []
    lrena_veic =  []
    lcor_veic =   []
    lano_veic =   []
    lmod_veic =   []
    while True:
        print(     '|I        Bem vindo a Veículos       I|')
        menu=input("|I Digite o numero da opção desejada I|\n|I Cadastro -  [1]\n|I Exclusão -  [2]\n|I Alteração - [3]\n|I Relatorio - [4]\n|I Sair -      [0]\n|I>>")
        if menu == '1':
            os.system("cls")
            print('|I   Bem vindo a cadastro   I|')
            while True:
                placa_cad=input("|I Informe a placa do veiculo I|\n|I>>")
                if placa_cad in lplaca_veic:
                    print("|I >> Placa ja esta cadastrada << I|")
                    os.system("pause")
                    os.system("cls")
                else:
                    break
            while True:
                try:
                    rena_cad=int(input("|I Informe o renavam do veiculo I|\n|I>>"))
                except ValueError:
                    print("|I >> Digite apenas numeros inteiros << I|")
                except:
                    print("|I >> Erro indefinido << I|")
                else:
                    break
            cor_cad=input("|I Informe a cor do veiculo I|\n|I>>")
            while True:
                try:
                    ano_cad=int(input("|I Informe o ano do veiculo I|\n|I>>"))
                except ValueError:
                    print("|I >> Digite apenas numeros inteiros << I|")
                except:
                    print("|I >> Erro indefinido << I|")
                else:
                    break
            mod_cad=input("|I Informe o modelo do veiculo I|\n|I>>")

            lplaca_veic.append(placa_cad)
            lrena_veic.append(rena_cad)
            lcor_veic.append(cor_cad)
            lano_veic.append(ano_cad)
            lmod_veic.append(mod_cad)
            print(">> Cadastro concluido <<")
            os.system("pause")
            os.system("cls")
        elif menu == '2':
            print('|I   Bem vindo a Exclusão   I|')
            veic_excl=input('|I Informe a placa do veiculo que deseja excluir I|\n|I>>')
            if veic_excl in lplaca_veic:
                veic_excl=lplaca_veic.index(veic_excl)
                lplaca_veic[veic_excl] = []
                lrena_veic[veic_excl] = []
                lcor_veic[veic_excl] = []
                lano_veic[veic_excl] = []
                lmod_veic[veic_excl] = []
                print(">> Exclusão concluida <<")
            else:
                print(">> Veiculo não cadastrado <<")
        elif menu == "3":
            print('|I   Bem vindo a Alteração  I|')
            placa_veic = input("Informe a placa do cadastro que deseja alterar:")
            alt_veic = lplaca_veic.index(placa_veic)
            if placa_veic in lplaca_veic:
                print("Faça as alterações:")
                placa_cad=input("Informe a placa do veiculo\n>>")
                while True:
                    try:
                        rena_cad=int(input("Informe o renavam do veiculo\n>>"))
                    except ValueError:
                        print("|I >> Digite apenas numeros inteiros << I|")
                    except:
                        print("|I >> Erro indefinido << I|")
                    else:
                        break
                cor_cad=input("Informe a cor do veiculo:")
                while True:
                    try:
                        ano_cad=int(input("Informe o ano do veiculo\n>>"))
                    except ValueError:
                        print("|I >> Digite apenas numeros inteiros << I|")
                    except:
                        print("|I >> Erro indefinido << I|")
                    else:
                        break
                mod_cad=input("Informe o modelo do veiculo\n>>")
                lplaca_veic[alt_veic] = placa_cad
                lrena_veic[alt_veic] = rena_cad
                lcor_veic[alt_veic] = cor_cad
                lano_veic[alt_veic] = ano_cad
                lmod_veic[alt_veic] = mod_cad
            else:
                print(">> Veiculo não cadastrado <<")
        elif menu == "4":
            print("""|I   Bem vindo ao relatorio   I|
|I Todos relatorios   - [1]
|I Escolher Relatorio - [2]""")
            while True:
                try:
                    relat_veic = int(input(">>"))
                except ValueError:
                    print("|I >> Digite apenas o que é pedido << I|")
                except:
                    print("|I >> Erro indefinido << I|")
                else:
                    break
            if relat_veic == 1:
                if lplaca_veic == [] and lrena_veic == [] and lcor_veic == [] and lano_veic == [] and lmod_veic == []:
                    print("Não a nenhum relatorio para ser impresso")
                else:
                    print("Placa >> ",end="")
                    for i in lplaca_veic:
                        print(i,end="|")
                    print("")
                    print("Renavam >> ",end="")
                    for i in lrena_veic:
                        print(i,end="|")
                    print("")
                    print("Cor >> ",end="")
                    for i in lcor_veic:
                        print(i,end="|")
                    print("")
                    print("Ano >> ",end="")
                    for i in lano_veic:
                        print(i,end="|")
                    print("")
                    print("Modelo >> ",end="")
                    for i in lmod_veic:
                        print(i,end="|")
                    print("")
                    os.system("pause")
                    os.system("cls")
            elif relat_veic == 2:
                placa_rela = input("Digite a placa do veiculo a ser consultado\n>>")
                if placa_rela in lplaca_veic:
                    index=lplaca_veic.index(placa_rela)
                    print(f"{lplaca_veic[index],lrena_veic[index],lcor_veic[index],lano_veic[index],lmod_veic[index]}")
                else:
                    print("Veiculo não cadastrado")
        elif menu == "0":
            break
        elif menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "0":
            print(" >>Escolha indisponivel<< ")
            os.system("pause")
            os.system("cls")

veic()