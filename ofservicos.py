#def (servic)
lcadastro = []
lpreco=[]
while True:
    print ("="*25,"\n","\ CADASTRO DE SERVIÇO /\n  \  OFICINA EDERSON  /\n","="*23)
    try:
        menu = (input("\nAperte: \n [ 1 ] para Cadastro \n [ 2 ] para Exclusão \n [ 3 ] para Alteração \n [ 4 ] Relatório\n"))
        if menu == '1':
            try:
                print ("-"*25,"\n"," BEM - VINDO AO CADASTRO\n", "="*24)
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
            print ("-"*25,"\n"," BEM - VINDO A EXCLUSÃO\n", "="*24)
            for i in lcadastro:
        elif menu == '3':
            print ("-"*25,"\n"," BEM - VINDO A ALTERAÇÃO\n", "="*24)
        elif menu == '4':
            print ("-"*25,"\n"," BEM - VINDO AO RELATORIO\n", "="*24)
            print (lcadastro)
            print(lpreco)
    except ValueError:
            print ("Escreva um número legitimo")
    except:
            print ("Erro desconhecido")
