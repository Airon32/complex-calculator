print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-PESQUISADOR DE MULTIFUNÇÕES EM MATEMATICA-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

while True:
    escolha = int(input(
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
        "-=-=-=-=-FAÇA SUA EXCOLHA DE QUAL OPERAÇÃO DESEJA -=-=-=-=-\n"
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
        "\n[1] - calculadora de soma\n"
        "[2] - calculdora de subtração\n" 
        "[3] - caculadora de multiplicação\n" 
        "[4] - calculadora de divisão\n" 
        "[5] - calculadora de expondenciação\n" 
        "[6] - ver a tabuada de um numero\n" 
        "[7] - calcular a porcentagem\n" 
        "[8] - calcular a potenciação\n" 
        "[9] - calcular a radicação\nEscolha: "
    ))
    

    if escolha == 1:

        print("\n-=-=-=-CALCULADORA DE SOMA-=-=-=-\n")
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("degite um segundo numero: "))
        soma = numero1 + numero2
        print(f"\no resultado da sua conta é: {soma}\n") 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")



    if escolha == 2:

        print("\n-=-=-CALCULADORA DE SUBTRAÇÃO-=-=-\n")
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite o segundo numero: "))
        subtração = numero1 - numero2
        print(f"o resultado dessa coonta é igual: {subtração}")
        


    if escolha == 3:

        print("\n-=-=-CALCULADORA DE MULTIPLICAÇÃO-=-=-\n")
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite o segundo numero: "))
        multiplicação = numero1 * numero2
        print(f"o resultado dessa coonta é igual: {multiplicação}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    


    if escolha == 4:

        print("\n-=-=-CALCULADORA DE DIVISÃO-=-=-\n")
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite o segundo numero: "))
        divisão = numero1 / numero2
        print(f"o resultado dessa coonta é igual: {divisão}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")



    if escolha == 5:

        print("\n-=-=-CALCULADORA DE EXPONDENCIAÇÃO-=-=-\n")
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite o segundo numero: "))
        expondenciação = numero1 ** numero2
        print(f"o resultado dessa coonta é igual: {expondenciação}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")



    if escolha == 6:

        print("\n-=-=-VER A TABUADA DE UM NUMERO-=-=-\n")
        numero1 = int(input("digite um numero para ver sua tabuada completa: \n"))
        for i in range(1, 11):
            print(f"|{numero1} X {i} = {numero1 * i}|")


    
    if escolha == 7:

        print("\n-=-=-CALCUALAR A PORCENTAGEM-=-=-\n")
        escolha2 = int(input(
            "[1] - cacualar apenas a porcentagem de um numero\n" \
            "[2] - calcular o desconto de um valor\n" \
            "[3] - calcular o jusos de um valor\nEscolha:"
        ))



        if escolha2 == 1:

            valor = int(input("digite o valor desejado: "))
            porcentagem = int(input("digite a porcentagem desejada: "))

            resultado = (porcentagem / 100) * valor
            print(f"o resultado de {porcentagem}% de {valor} é {resultado}")



        if escolha2 == 2:

            Produto = int(input("digite o valor do produto desejado: "))
            taxa = int(input("digite a taxa de juros do produto: "))
            tempo = int(input("digite a o tempo (em meses) de atraso: "))

            print("\n-=-juros de mes em mes-=-\n")

            for mes in range(1, tempo + 1):
                juros = Produto * taxa * tempo
                resultado = Produto + juros 

            print(
                f"Mês {mes}: Juros = R${juros:.2f} | Montante = R${resultado:.2f}"
                )



        if escolha2 == 3:
            valorInicial = int(input("digite o valor do produto desejado: "))
            taxa = int(input("digite a taxa de juros do produto: "))
            tempo = int(input("digite a o tempo (em meses) de atraso: "))

            desconto = valorInicial * taxa * tempo
            valorFinal = valorInicial - desconto 

            print(
                  f"O desconto é de R${desconto:.2f}"
                  )
            
            print(
                f"o valor total do jusos é: R${valorFinal:.2f}"
                )