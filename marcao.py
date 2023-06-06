from funcoes import limparTela, esperarSegundos, soma, mudaCor
limparTela()
print( "Seja-Bem vindo ao sistema")
esperarSegundos(3)
while True:
    limparTela()
    print("(0)Sair")
    print("(1)Conversão em C")
    print("(2)Conversão em F")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        print ("Convertando F para C")
        fahrenheit = int(input("fahrenheit"))
        input("press enter to continue...")
    elif opcao == "2":
        cor = int(input("infrome o codigo da Cor:"))
        mudaCor(cor)
        print("Convertendo C para F")
        input("press enter to continue...")
    elif opcao =="3":
        n1 = int(input("numero1:"))
        n2 = int(input("numero2:"))
        print ("a soma é", soma (n1, n2))
        esperarSegundos()


    else:
        print("opcao Invalida!")
        esperarSegundos()
print("volte sempre!...")
