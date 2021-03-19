import math


def leitura():
    
    arq = input("Digite o nome do arquivo csv de entrada: ")

    f = open(arq+".csv", "r")

    coluna = 0
    missingIds = []
    i = 0
    valores = []
    nonMissing = 0

    while True:
        coluna = int(input("Digite o numero da coluna: "))
        if(coluna == 0 or coluna == 1 or coluna < 0 or coluna >= 5):
            print("Coluna inválida. Tente outra.")
        else:
            break

    for line in f:
        if i == 0:
            i = i+1
            continue
        
        s = line.replace("\n","")
        a = s.split(",")
        if(a[coluna] != '?'):
            valores.append(int(a[coluna]))
            nonMissing = nonMissing+1
        else:
            missingIds.append(i)
        i=i+1

    # Calculando moda
    if valores.count(0) >= valores.count(1) and valores.count(0) >= valores.count(2):
        moda = 0
    elif valores.count(1) >= valores.count(0) and valores.count(1) >= valores.count(2):
        moda = 1
    else:
        moda = 2

    #Calculando média
    media = math.ceil(sum(valores)/nonMissing)

    #Calculando mediana
    valores.sort()
    if len(valores)%2 == 0:
        meio = int(len(valores)/2)
        mediana = math.ceil( (valores[meio] + valores[meio+1])/2 )
    else:
        mediana = valores[int(len(valores)/2)]

    f.close()

    return {
        "media":media,
        "moda":moda,
        "mediana":mediana,
        "missing":missingIds,
        "coluna":coluna,
        "arq":arq
    }

def main():

    res = leitura()
    print("Selecione o tipo de substituição a ser utilizado: ( 1-Media | 2-Mediana | 3-Moda )")
    op = int(input())

    print("Mostrando os valores calculados para cada uma das 3 opções de substituição: ")
    print()
    print("Media = ",res["media"])
    print("Mediana = ",res["mediana"])
    print("Moda = ",res["moda"])
    print()

    if op == 3:
        val = res["moda"]
    elif op == 2:
        val = res["mediana"]
    else:
        val = res["media"]

    escrita(op,val,res["missing"],res["coluna"],res["arq"])



def escrita(op,val,missingIds,coluna,arq):


    f = open(arq+".csv", "r")
    f2 = open("result.csv", "w")

    i=0
    for line in f:
        if i == 0:
            f2.write(line)
            i=i+1
            continue
        
        if i in missingIds:
            s = line.replace("\n","")
            a = s.split(",")

            a[coluna] = str(val)

            wline = str(a[0])+''.join(","+j for j in a[1::])+'\n'
            f2.write(wline)
        else:
            f2.write(line)

        i = i+1


    f.close()
    f2.close()



main()