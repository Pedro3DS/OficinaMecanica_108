def veic():
    import os
    lplaca_veic = []
    lrena_veic =  []
    lcor_veic =   []
    lano_veic =   []
    lmod_veic =   []
    while True:
        print('Bem vindo a Veículos')
        menu=input("|I Digite o numero da opção desejada I|\nCadastro - [1]\nExclusão - [2]\nAlteração - [3]\nRelatorio - [4]\nSair - [0]\n>>")
        if menu == '1':
            print('Bem vindo a cadastro')
            placa_cad=input("Informe a placa do veiculo:")
            rena_cad=input("Informe o renavam do veiculo:")
            cor_cad=input("Informe a cor do veiculo:")
            ano_cad=int(input("Informe o ano do veiculo:"))
            mod_cad=input("Informe o modelo do veiculo:")

            lplaca_veic.append(placa_cad)
            lrena_veic.append(rena_cad)
            lcor_veic.append(cor_cad)
            lano_veic.append(ano_cad)
            lmod_veic.append(mod_cad)
            print("Cadastro concluido")
        elif menu == '2':
            print('Bem vindo a Exclusão')
            veic_excl=input('Informe a placa do veiculo que deseja excluir:')
            if veic_excl in lplaca_veic:
                veic_excl=lplaca_veic.index(veic_excl)
                lplaca_veic[veic_excl] = []
                lrena_veic[veic_excl] = []
                lcor_veic[veic_excl] = []
                lano_veic[veic_excl] = []
                lmod_veic[veic_excl] = []
                print("Exclusão concluida")
            else:
                print("Veiculo não cadastrado")
        elif menu == "3":
            print('Bem vindo a Alteração')
            placa_veic = input("Informe a placa do cadastro que deseja alterar:")
            alt_veic = lplaca_veic.index(placa_veic)
            if placa_veic in lplaca_veic:
                print("Faça as alterações:")
                placa_cad=input("Informe a placa do veiculo:")
                rena_cad=input("Informe o renavam do veiculo:")
                cor_cad=input("Informe a cor do veiculo:")
                ano_cad=int(input("Informe o ano do veiculo:"))
                mod_cad=input("Informe o modelo do veiculo:")
                lplaca_veic[alt_veic] = placa_cad
                lrena_veic[alt_veic] = rena_cad
                lcor_veic[alt_veic] = cor_cad
                lano_veic[alt_veic] = ano_cad
                lmod_veic[alt_veic] = mod_cad
            else:
                print("Veiculo não cadastrado")
        elif menu == "4":
            print("""Bem vindo ao relatorio
Todos relatorios - [1]
Escolher Relatorio - [2]""")
            relat_veic = int(input(">>"))
            if relat_veic == 1:
                if lplaca_veic == [] and lrena_veic == [] and lcor_veic == [] and lano_veic == [] and lmod_veic == []:
                    print("Não a nenhum relatorio para ser impresso")
                else:
                    for i in lplaca_veic:
                        print(i)
                    for i in lrena_veic:
                        print(i)
                    for i in lcor_veic:
                        print(i)
                    for i in lano_veic:
                        print(i)
                    for i in lmod_veic:
                        print(i)
            elif relat_veic == 2:
                placa_rela = input("Digite a placa do veiculo a ser consultado\n>>")
                if placa_rela in lplaca_veic:
                    index=lplaca_veic.index(veic_excl)
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