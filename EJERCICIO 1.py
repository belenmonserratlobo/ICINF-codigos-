lista=[]

f=str(input("Ingrese una palabra: "))
f=f.lower()

while f!= "":
    lista.append(f)
    f=str(input("Ingrese una palabra: "))
    f=f.lower()

 
for f in lista:
    voca=0
    con=0
    for caracter in f:
     if caracter in "aeiou" :
            voca=voca+1
     else:
            con=con+1
    print("La palabra",f , "tiene",voca ,"vocales y",con, "consonantes")
