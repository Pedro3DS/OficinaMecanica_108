def servic():
    from os import system
    lcadastro = [] 
    lpreco=[]
    while True:
        print ("="*25,"\n","\ CADASTRO DE SERVIÇO /\n  \  OFICINA EDERSON  /\n","="*23)
        try:
            menu = (input("\nAperte: \n [ 1 ] para Cadastro \n [ 2 ] para Exclusão \n [ 3 ] para Alteração \n [ 4 ] Relatório\n [ 0 ] Sair\n")) #menu
            if menu=="0":
                system("cls")
                print("Obrigado por utilizar o MENU DE SERVIÇOS.")
                system("pause")
                system("cls")
                break
            if menu == '1':
                try:
                    print ("-"*25,"\n"," BEM - VINDO AO CADASTRO\n", "="*24) #menu cadastro
                    servico = str(input("Descreva o serviço: "))
                    preco = float(input("Informe o preço: "))
                except ValueError:
                    print ("Informe um número válido")
                except:
                    print("erro desconhecido")
                else:
                    lcadastro.append(servico)
                    lpreco.append(preco)
            elif menu == '2':
                print ("-"*25,"\n"," BEM - VINDO A EXCLUSÃO\n", "="*24) #menu exclusão
                try:
                    servico=input("Nome do serviço a ser excluído: ")
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
                    if servico in lcadastro:
                        index=lcadastro.index(servico)
                        lpreco[index]=[]
                        lcadastro[index]=[]
                        print("O cadastro foi excluido com sucesso.")
                        system("pause")
                        system("cls")
                    else:
                        system("cls")
                        print("O nome não está na lista de fornecedores.")
                        system("pause")
                        system("cls")
            elif menu == '3':
                print ("-"*25,"\n"," BEM - VINDO A ALTERAÇÃO\n", "="*24) #menu alteração de serviço
                try:
                    servico=input("Nome do serviço a ser alterado: ")
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
                    if servico in lcadastro:
                        index=lcadastro.index(servico)
                        try:
                            print("INSIRA AS INFORMAÇÕES REFERENTES AO SERVIÇO A SEREM ALTERADAS.\n")
                            servico=input("Serviço novo: ")
                            preco=float(input("Preço novo: "))
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
                            lcadastro[index]=servico
                            lpreco[index]=preco
                            print("Alterações feitas com sucesso.")
                            system("pause")
                            system("cls")
                    else:
                        system("cls")
                        print("O nome não está na lista de fornecedores.")
                        system("pause")
                        system("cls")
            elif menu == '4':
                print ("-"*25,"\n"," BEM - VINDO AO RELATORIO\n", "="*24)  #menu relatório
                print (lcadastro)
                print(lpreco)
        except ValueError:
                print ("Escreva um número legitimo")
        except:
                print ("Erro desconhecido")