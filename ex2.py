lista = []
num = 0

try:
    while num >= 0 :
        
        num = int(input("Digite um número: "))

        if num >= 0:
            lista.append(num)


    print(lista)

    x = int(input("Digite o número a ser verificado: "))


    if x in lista:
        print(f"{x} está presente na lista")

    else:
        print(f"{x} Não esta na lista")

except:
    print("Por favor digite um número inteiro!")