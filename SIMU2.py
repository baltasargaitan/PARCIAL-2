def abrir():
    x=open("entrada.txt","rt")
    texto=x.read()
    x.close()
    return(texto)

def esletra(letra):
    if "A"<=letra<="Z" or "a"<=letra<="z":
        return True
    return False
def es_vocal(letra):
    if letra in ("aAeEiIoOuU"):
        return True
def es_consonante(letra):
    if esletra(letra) and not es_vocal(letra):
        return True
def es_digito(letra):
    if "0"<=letra<="9":
        return True
def procesar(texto):
    cp=clp=cp1=cp2=cp3=cv=cc=cp4=0
    cl3_total=0
    nop=True
    digito=False
    mayor=aux=None
    ese=False
    banderafinal=banderafinal2=False


    for car in texto:
        if car != " " and car != ".":
            clp+=1
            if es_consonante(car):
                car=car.lower()
                cc += 1
                if car =="S" or car == "s":
                    ese=True
            elif es_vocal(car):
                car=car.lower()
                cv += 1
                if clp<=2:
                    banderafinal2=True
            if car == "p" or car =="P":
                nop=False
            if es_digito(car):
                digito=True
            if (car =="a" or car=="A") and (aux =="r" or aux =="R"):
                banderafinal=True

        else:
            if clp>=0:
                cp += 1
                if cc==cv and clp%2==0:
                        cp1+=1
                if nop and digito:
                    if mayor==None or clp > mayor :
                        mayor = clp
                if clp>2 and not ese:
                    cp3 += 1
                    cl3_total+=clp
                if banderafinal and banderafinal2:
                    cp4+=1
            cv=cc=0
            clp=0
            nop=True
            digito=False
            ese=False
            banderafinal=banderafinal2=False
        aux=car

    print(cp1)
    print(mayor)
    print(cl3_total//cp3)
    print(cp4)



def main():
    texto=abrir()
    procesar(texto)




if __name__ == "__main__":
    main()
