num = int

lista = []


try: 
    num = int(input("Digite a quantidade de números a ser digitados: "))

    if num  > -1:
        lista = [int(input(f"Digite o {i}º numero: ")) for i in range(1,(num + 1))]


        x = int(input("\nDigite o número a ser verificado: "))

        if x in lista:
            print(f"{x} está presente na lista")
        else:
            print(f"{x} Não esta na lista")


    else: 
        print("A quantidade de números a ser digitados precisa ser positiva")

except:
    print("Por favor digite um número inteiro!")
