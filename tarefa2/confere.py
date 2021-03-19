
def check():
    
    arq = input("Digite o nome do arquivo csv de entrada: ")

    f = open(arq+".csv", "r")

    coluna = 0
    missingIds = []
    i = 0


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
        if(a[coluna] == '?'):
            missingIds.append(i)
        i=i+1

    f.close()
    return [missingIds,coluna]

def main():

    res = check()
    if len(res[0]) == 0:
        print("O arquivo de entrada nao possui valores ausentes na coluna "+str(res[1]))
    else:
        print("Valores ausentes encontrados na coluna "+str(res[1]))
        print("posicoes ausentes : ",res[0])


main()