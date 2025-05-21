print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-PESQUISADOR DE MULTIFUNÇÕES EM MATEMATICA-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

import math

def linha():
    print("-" * 60)

from time import sleep
while True: 
    linha()
    escolha = int(input(
    "-=-=-=-=-FAÇA SUA EXCOLHA DE QUAL OPERAÇÃO DESEJA-=-=-=-=-\n"
    "\n[1] - calculadora de soma\n"
    "[2] - calculdora de subtração\n" 
    "[3] - caculadora de multiplicação\n" 
    "[4] - calculadora de divisão\n" 
    "[5] - calculadora de expondenciação\n" 
    "[6] - ver a tabuada de um numero\n" 
    "[7] - calcular a porcentagem\n" 
    "[8] - calcular a potenciação\n"
    "[9] - calcular a area, perimetro e o volume de alguma forma geometrica\n" 
    "[10] - calcular a radicação\n"
    "[11] - calcular o fatorial de um número\n"
    "[12] - verificar se um número é primo\n"
    "[13] - calcular o (MDC) ou (MMC) de um numero\n"
    "[14] - resolver equações de 2º grau\n"
    "[15] - resolver equação de 1º grau\n"
    "[16] - calcular logaritmos (base 10 ou base e)\n"
    "[17] - calcular seno, cosseno e tangente de um ângulo\n"
    "[18] - converter unidades de medida\n"
    "[19] - calcular juros e desconto\n"
    "[20] - simular financiamento ou parcelamento\n"
    "[21] - converter horas em minutos e segundos\n"
    "[22] - calcular a diferença entre dois horários\n"
    "[23] - jogo de perguntas de matemática\n"
    "[24] - teste de conhecimentos básicos\n"
    "[25] - sair\nEscolha: "
    ))


    if escolha == 1:

            print("\n-=-=-=-CALCULADORA DE SOMA-=-=-=-\n")
            
            soma = 0

            while True:
                numero = float(input("Digite um número para somar: "))
                soma += numero

                continuar = input("Deseja adicionar mais um número? (sim ou nao): ").strip().lower()
                if continuar == 'nao':
                    break

            print("Calculando...")
            sleep(1.5)

            print(f"\nO resultado da soma é: {soma}\n")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

            sair = input("Deseja voltar ao menu principal? (sim ou nao): ").strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break




    if escolha == 2:

            print("\n-=-=-CALCULADORA DE SUBTRAÇÃO-=-=-\n")

            numero1 = float(input("Digite o primeiro número: "))
            resultado = numero1

            while True:
                continuar = input("Deseja subtrair outro número? (sim ou nao): ").strip().lower()
                if continuar == 'nao':
                    break

                numero = float(input("Digite o número que será subtraído: "))
                resultado -= numero

            print("calculando...")
            sleep(1.5)

            print(f"\nO resultado da subtração é: {resultado}\n")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

            sair = input("Deseja voltar ao menu principal? (sim ou nao): ").strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break



    if escolha == 3:

            print("\n-=-=-CALCULADORA DE MULTILICAÇÃO-=-=-\n")

            numero1 = float(input("Digite o primeiro número: "))
            resultado = numero1

            while True:
                continuar = input("Deseja subtrair outro número? (sim ou nao): ").strip().lower()
                if continuar == 'nao':
                    break

                numero = float(input("Digite o número que será subtraído: "))
                resultado *= numero

            print("calculando...")
            sleep(1.5)

            print(f"\nO resultado da subtração é: {resultado}\n")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

            sair = input("Deseja voltar ao menu principal? (sim ou nao): ").strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break




    if escolha == 4:

            print("\n-=-=-CALCULADORA DE DIVISÃO-=-=-\n")

            numero1 = float(input("Digite o primeiro número (de onde a subtração vai começar): "))
            resultado = numero1

            while True:
                continuar = input("Deseja subtrair outro número? (sim ou nao): ").strip().lower()
                if continuar == 'nao':
                    break

                numero = float(input("Digite o número que será subtraído: "))
                resultado /= numero

            print("calculando...")
            sleep(1.5)

            print(f"\nO resultado da subtração é: {resultado}\n")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

            sair = input("Deseja voltar ao menu principal? (sim ou nao): ").strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break




    if escolha == 5:

        print("\n-=-=-CALCULADORA DE EXPONDENCIAÇÃO-=-=-\n")
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite o segundo numero: "))
        expondenciação = numero1 ** numero2
        print("calculando...")
        sleep(1.5)

        print(f"o resultado dessa coonta é igual: {expondenciação}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
        if sair == 'sim':
            continue
        if sair == 'nao':
            break



    if escolha == 6:

        print("\n-=-=-VER A TABUADA DE UM NUMERO-=-=-\n")
        numero1 = int(input("digite um numero para ver sua tabuada completa: \n"))
        for i in range(1, 11):
            print(f"|{numero1} X {i} = {numero1 * i}|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    
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
            print("calculando...")
            sleep(1.5)

            print(f"o resultado de {porcentagem}% de {valor} é {resultado}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break



        if escolha2 == 2:

            Produto = int(input("digite o valor do produto desejado: "))
            taxa = int(input("digite a taxa de juros do produto: "))
            tempo = int(input("digite a o tempo (em meses) de atraso: "))

            print("\n-=-juros de mes em mes-=-\n")

            for mes in range(1, tempo + 1):
                juros = Produto * taxa * tempo
                resultado = Produto + juros 
            print("calculando...")
            sleep(1.5)

            print(
                f"\nMês {mes}: Juros = R${juros:.2f} | Montante = R${resultado:.2f}\n"
                )
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break



        if escolha2 == 3:
            valorInicial = int(input("digite o valor do produto desejado: "))
            taxa = int(input("digite a taxa de juros do produto: "))
            tempo = int(input("digite a o tempo (em meses) de atraso: "))

            desconto = valorInicial * taxa * tempo
            valorFinal = valorInicial - desconto 
            print("calculando...")
            sleep(1.5)

            print(
                  f"O desconto é de R${desconto:.2f}"
                  )
            
            print(
                f"o valor total do jusos é: R${valorFinal:.2f}"
                )
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break



    if escolha == 8:
        linha()
        print("\n-=-=-=-CALCULADORA DE POTENCIAÇÃO-=-=-=-\n")
        base = int(input("digite o numero base: "))
        expoente = int(input("degite o que sera o expoente: "))
        resultado = base ** expoente
        print("calculando...")
        sleep(1.5)

        print(f"\no resultado da sua conta é: {resultado}\n") 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
        if sair == 'sim':
            continue
        if sair == 'nao':
            break



    if escolha == 9:
        linha()
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
            print("calculando...")
            sleep(1.5)

            print(f"a area estimada do triangulo é: {area}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break


        
        if escolha3 == 2:

            base = int(input("digite o valor da base: "))
            altura = int(input("digite o valor da altura: "))
            area = base * altura
            print("calculando...")
            sleep(1.5)

            print(f"a area estimada do quadrado é: {area}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower
            if sair == 'sim':
                continue
            if sair == 'nao':
                break


        if escolha3 == 3:

            baseMenor = int(input("digite o valor da base menor: "))
            baseMaior = int(input("digite o valor da base maior: "))
            altura = int(input("digite o valor da altura: "))
            area = (baseMenor + baseMaior) * altura / 2
            print("calculando...")
            sleep(1.5)

            print(f"a area estimada do lozangulo é: {area}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break
        

        if escolha3 == 4:
            constantePI = 3.14
            raio = float(input("digite o valor do raio: "))
            area = constantePI * raio ** 2
            print("calculando...")
            sleep(1.5)

            print(f"o a area estimado do circulo é: {area:.2f}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break


        if escolha3 == 5:

            diagonalMenor = int(input("digite o valor da diagonal menor: "))
            diagonalMaior = int(input("digite o valor da diagonal maior: "))
            area = diagonalMenor * diagonalMaior / 2
            print("calculando...")
            sleep(1.5)
    
            print(f"a area estimada do lozangolo é: {area}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break

    

    if escolha == 10:
        linha()
        print("\n-=-=-=-CALCULAR A RAIZ DE UM NUMERO-=-=-=-\n")

        numero = int(input("digite o numero desejado: "))
        indice = int(input("digite o indice desejado (2 para quadrada e 3 para cubica)"))

        raiz = numero ** (1 / indice)

        print("calculando...")
        sleep(1.5)

        print(f"a raiz do numero desejado é: {raiz}")

        sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
        if sair == 'sim':
            continue
        if sair == 'nao':
            break



    if escolha == 11:
        linha()
        print("\n-=-=-=-CALCULAR O FATORIAL DE UM NUMERO-=-=-=-\n")

        numero = int(input("digite um numero: "))
        fatorial= 1
        for i in range(1, numero + 1):    
            fatorial *= i

        print("calculando...")
        sleep(1.5)

        print(f"o resultado para o numero digitado é: {fatorial}")

        sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
        if sair == 'sim':
            continue
        if sair == 'nao':
            break

    

    if escolha == 12:
        linha()
        print("\n-=-=-=-VERIFICADOR DE NUMEROS PRIMOS-=-=-=-\n")
        escolha = int(input(
            "[1] - descobrir se é impar"
            "[2] - descorir se é par"
        ))
        
        if escolha == 1:

            num = int(input(
                "digite um numero: "
            ))

            if num / 2 != 0:
                print(f"o numero {num} é inpar")
            else:
                print("o numero é par")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break

        if escolha == 2: 

            num = int(input(
                "digite um numero: "
            ))

            if num / 2 == 0:
                print(f"o numero {num} é par") 
            else:
                print("o numeor é impar")
            
            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break

    if escolha == 13:

        linha()
        print("\n-=-=-=-CALCULADOR DE MMC E MDC-=-=-=-\n")
        escolha5 = int(input(
            "[1] - calcular o MMC\n"
            "[2] - calcular o MDC\nEscolha: "
        ))
        
        if escolha5 == 1:
            print("calcular o MMC")

            numero = int(input(
                "digite o numero: "
            ))

            numero2 = int(input(
                "digite o segundo numro: "
            ))

            mmc = numero * numero2 // math.gcd(numero, numero2)

            print("calculando...")
            sleep(1.5)

            print(f"\no mmc do numero desejado é igual à: {mmc}\n")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break

        elif escolha5 == 2:
        
            print("calcular o MDC")
            
            a = int(input(
                "digite o numero: "
            ))

            b = int(input(
                "digite o segundo numro: "
            ))

            while b != 0:

                resto = a % b
                a = b
                b = resto

            print("calculando...")
            sleep(1.5)

            print(f"o MDC se resulta em: {a}")

            sair = str(input("deseja continuar sim ou nao? ")).strip().lower()
            if sair == 'sim':
                continue
            if sair == 'nao':
                break
