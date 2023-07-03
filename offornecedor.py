def fornece():
    from os import system
    lnome_forn=[]
    lcnpj_forn=[]
    lend_forn=[]
    ltel_forn=[]
    lmail_forn=[]

    while True:
        menu=input("BEM VINDO AO MENU DE FORNECEDORES -------------------\n1. CADASTRO\n2. ALTERAÇÃO\n3. EXCLUSÃO\n4. RELATÓRIO\n0. SAIR\n")
        if menu=="1":
            system("cls")
            print("BEM VINDO AO CADASTRO")
            try:
                nome_forn=input("Nome do Fornecedor: ")
                cnpj_forn=int(input("CNPJ: "))
                end_forn=input("Endereço: ")
                tel_forn=int(input("Telefone: "))
                mail_forn=input("Email: ")
            except ValueError:
                system("cls") 
                print("Dados inválidos.")
                system("pause")
                system("cls")
            except:
                system("cls")
                print("Erro desconhecido")
                system("pause")
                system("cls")
            else:
                system("cls")
                lnome_forn.append(nome_forn)
                lcnpj_forn.append(cnpj_forn)
                lend_forn.append(end_forn)
                ltel_forn.append(tel_forn)
                lmail_forn.append(mail_forn)
                print("Cadastro realizado com sucesso.")
                system("pause")
                system("cls")

        elif menu=="2":
            system("cls")
            print("BEM VINDO A ALTERAÇÃO\n")
            try:
                nome_forn=input("Nome do Fornecedor para ser alterado: ")
            except ValueError:
                system("cls")
                print("Digite somente nomes.")
                system("pause")
                system("cls")
            except:
                system("cls")
                print("Nome inexistente.")
                system("pause")
                system("cls")
            else:
                system("cls")
                if nome_forn in lnome_forn:
                    index=lnome_forn.index(nome_forn)
                    try:
                        print("INSIRA AS INFORMAÇÕES A SEREM ALTERADAS.\n")
                        nome_forn=input("Nome do Fornecedor: ")
                        cnpj_forn=int(input("CNPJ: "))
                        end_forn=input("Endereço: ")
                        tel_forn=int(input("Telefone: "))
                        mail_forn=input("Email: ")
                    except ValueError:
                        system("cls")
                        print("Dados inválidos.")
                        system("pause")
                        system("cls")
                    except: 
                        system("cls")
                        print("Erro desconhecido.")
                        system("pause")
                        system("cls")
                    else:
                        system("cls")
                        lnome_forn[index]=nome_forn
                        lcnpj_forn[index]=cnpj_forn
                        lend_forn[index]=end_forn
                        ltel_forn[index]=tel_forn
                        lmail_forn[index]=mail_forn
                        print("Alterações feitas com sucesso.")
                        system("pause")
                        system("cls")
                else:
                    system("cls")
                    print("O nome não está na lista de fornecedores.")
                    system("pause")
                    system("cls")
        elif menu=="3":
            system("cls")
            print("BEM VINDO A EXCLUSÃO")
            try:
                nome_forn=input("Nome do Fornecedor para serem excluidas as informações: ")
            except ValueError:
                system("cls")
                print("Digite somente nomes.")
                system("pause")
                system("cls")
            except:
                system("cls")
                print("Nome inexistente.")
                system("pause")
                system("cls")
            else:
                system("cls")
                if nome_forn in lnome_forn:
                    index=lnome_forn.index(nome_forn)
                    lnome_forn[index]=[]
                    lcnpj_forn[index]=[]
                    lend_forn[index]=[]
                    ltel_forn[index]=[]
                    lmail_forn[index]=[]
                    print("O Fornecedor foi excluido com sucesso.")
                    system("pause")
                    system("cls")
                else:
                    system("cls")
                    print("O nome não está na lista de fornecedores.")
                    system("pause")
                    system("cls")
        elif menu=="4":
            system("cls")
            print("BEM VINDO AO RELATÓRIO\n")
            menu=input("1. IMPRIMIR TUDO\n2. SELECIONAR FORNECEDOR.\n")
            if menu=="1":
                print("Nomes dos Fornecedores em ordem:\n")
                for i in lnome_forn:
                    print(i)
                print("\n\nCNPJ dos Fornecedores em ordem:\n")
                for i in lcnpj_forn:
                    print(i)
                print("\n\nEndereço dos Fornecedores em ordem:\n")
                for i in lend_forn:
                    print(i)
                print("\n\nTelefone dos Fornecedores em ordem:\n")
                for i in ltel_forn:
                    print(i)
                print("\n\nEmail dos Fornecedores em ordem:\n")
                for i in lmail_forn:
                    print(i)
                system("pause")
                system("cls")
            elif menu=="2":
                try:
                    nome_forn=input("Nome do Fornecedor a ser consultado as informações: ")
                except ValueError:
                    system("cls")
                    print("Digite somente nomes.")
                    system("pause")
                    system("cls")
                except:
                    system("cls")
                    print("Nome inexistente")
                    system("pause")
                    system("cls")
                else:
                    if nome_forn in lnome_forn:
                        index=lnome_forn.index(nome_forn)
                        print(lnome_forn[index],lcnpj_forn[index],lend_forn[index],ltel_forn[index],lmail_forn[index])
                        system("pause")
                        system("cls")
                    else:
                        system("cls")
                        print("O nome não está na lista de fornecedores.")
                        system("pause")
                        system("cls")
            else:
                system("cls")
                print("Opção inexistente.")
                system("pause")
                system("cls")
        elif menu=="0":
            system("cls")
            print("Obrigado por utilizar o MENU DE FORNECEDORES.")
            system("pause")
            system("cls")
            break
        else:
            system("cls")
            print("Opção inexistente.")
            system("pause")
            system("cls")