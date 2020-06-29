import collections
with open("contras.txt",encoding="utf8",errors="ignore") as f:
    i=0;
    datos=[]
    conteo=[]
    for line in f:
        linea = line.replace("\n","") 
        #datos[largo,máscara,contraseña]
        mascara=""
        for t in linea:
            if t.isupper():
                mascara+="U"
            elif t.islower():
                mascara+="L"
            elif t.isdigit():
                mascara+="D"
            else:
                mascara+="S"
        datos.append([i,len(linea),linea,mascara])
        conteo.append(mascara)
        i+=1
    archivo=f.name

max_pass=i
print("Passwords loaded:",max_pass)
mascaras=collections.Counter(conteo).most_common()
print("TOP 20 MASK\n===========\n")
sum_porcentaje=0

with open(archivo+".hcmask","w") as f:
    with open(archivo+".csv","w") as g:
        cadena="NUM,MASK,HASHCAT MASK,LENGTH,OCURENCES,PERCENT\n"
        g.write(cadena)
        for i in range(0,20):
            porcentaje=round(100*(mascaras[i][1]/max_pass),2)
            sum_porcentaje+=porcentaje
            hashcat=""
            cadena=""
            for t in mascaras[i][0]:
                if t=="U":
                    hashcat+="?u"
                elif t=="L":
                    hashcat+="?l"
                elif t=="D":
                    hashcat+="?d"
                else:
                    hashcat+="?s"
            print(i+1,")",mascaras[i][0],"-",hashcat,"- Lenght:",len(mascaras[i][0]),"-",mascaras[i][1],"times -",porcentaje,"%")
            cadena=str(i+1)+","+mascaras[i][0]+","+hashcat+","+str(len(mascaras[i][0]))+","+str(mascaras[i][1])+","+str(porcentaje)+"\n"
            f.write(hashcat+"\n")
            g.write(cadena)
print("\n============\nSUM:",round(sum_porcentaje,2),"%")
