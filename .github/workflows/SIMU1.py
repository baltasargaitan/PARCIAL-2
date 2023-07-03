def abrir():
    x=open("entrada.txt","rt")
    texto=x.read()
    x.close()
    return(texto)
def esmayus(letra):
    if letra in ("ABCDEFGHIJKLMNÑOPQRSTUVXYZ"):
        mayus=True
        return(mayus)
def esvocal(letra):
    if letra in ("aAeEiIoOuU"):
        vocal=True
        return(vocal)
def esconsonante(letra):
    if letra in ("BbCcDdFfGgHhJjKkLlMmNnÑñPpQqRrSsTtVvXxZzWwYy"):
        consonante=True
        return(consonante)
def procesar(texto):
    clp=cp=cp1=cp2=cp3=cv=cltotal=cp4=cpd=cc=0
    primer=primer2=False
    minus=legal=True
    ban_b=False
    maslarga=None
    aux=None
    for car in texto:
        if car != " " and car != ".":
            clp+=1
            if clp<=1:
                if car in ("13579"):
                    primer=True
                if esvocal(car):
                    primer2=True

            else:
                if esmayus(car) or car.isdigit():
                    minus=False
                if car=="b" or car =="B":
                    ban_b=True
            if esvocal(car):
                cv+=1
                if aux=="D" or aux=="d":
                    cpd+=1
            if esconsonante(car):
                cc+=1
            if car in ("aAmM"):
                legal=False
            aux=car
        else:
            if clp>=1:
                cp+=1
                if primer and minus:
                    cp1+=1
                if (ban_b and primer2) :
                    if  maslarga==None or clp>maslarga:
                        maslarga=clp
                if cc>cv and legal:
                    cp3+=1
                    cltotal+=clp
                if cpd>=2 and esvocal(aux):
                    cp4+=1
            aux=None
            minus=True
            clp=cc=cv=cpd=0
            primer=ban_b=False
            legal=True
    prom=int(cltotal/cp3)
    print("Cantidad de palabras comienzan con un dígito impar, y el resto de sus caracteres son letras en minúsculas:",cp1)
    print("Longitud de la palabra más larga entre aquellas que comienzan con una vocal y contenga al menos una letra ‘b’ ",maslarga)
    print("Promedio entero de caracteres por palabra entre las palabras que tienen más consonantes que vocales, pero no contienen ninguna ‘m’ ni ‘a’:",prom)
    print("Palabras incluyen dos o más veces la expresión que conforman la letra “d” mas una vocal  termine  con una vocal:",cp4)

def main():
    entrada=abrir()
    procesar(entrada)



if __name__ == "__main__":
    main()

