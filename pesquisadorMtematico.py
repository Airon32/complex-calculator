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
        '[9] - calcular a area de alguma forma geometrica\n' 
        "[10] - calcular a radicação\nEscolha: "
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
                f"\nMês {mes}: Juros = R${juros:.2f} | Montante = R${resultado:.2f}\n"
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
    


    if escolha == 8:
       
        print("\n-=-=-=-CALCULADORA DE POTENCIAÇÃO-=-=-=-\n")
        base = int(input("digite o numero base: "))
        expoente = int(input("degite o que sera o expoente: "))
        resultado = base ** expoente

        print(f"\no resultado da sua conta é: {resultado}\n") 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
 


    if escolha == 9:
        
        print("\n-=-=-=-CALCULADORA DE FORMAS GEOMETRICAS-=-=-=-\n")
        escolha3 = int(input(
            "[1] - calcular a area de triangulo\n" \
            "[2] - calcular a area de um quadrado\n"
            "[3] - calcular a area de trapezio\n"
            "[4] - calcular a area de um circulo\n"
            "[5] - calcular a area de um lozangulo\nEscolha: "  
        ))

        if escolha3 == 1:

            base = int(input("digite o valor da base: "))
            altura = int(input("digite a altura: "))
            area = base * altura / 2

            print(f"a area estimada do triangulo é: {area}")

        
        if escolha3 == 2:

            base = int(input("digite o valor da base: "))
            altura = int(input("digite o valor da altura: "))
            area = base * altura

            print(f"a area estimada do quadrado é: {area}")


        if escolha3 == 3:

            baseMenor = int(input("digite o valor da base menor: "))
            baseMaior = int(input("digite o valor da base maior: "))
            altura = int(input("digite o valor da altura: "))
            area = baseMenor + baseMaior * altura / 2

            print(f"a area estimada do lozangulo é: {area}")
        

        if escolha3 == 4:
            constantePI = 3.14
            raio = float(input("digite o valor do raio: "))
            area = constantePI * raio ** 2

            print(f"o a area estimado do circulo é: {area:.2f}")


        if escolha3 == 5:

            diagonalMenor = int(input("digite o valor da diagonal menor: "))
            diagonalMaior = int(input("digite o valor da diagonal maior: "))
            area = diagonalMenor * diagonalMaior / 2
            
            print(f"a area estimada do lozangolo é: {area}")
