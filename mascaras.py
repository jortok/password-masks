import collections
with open("contras.txt","r") as f:
    i=0;
    datos=[]
    conteo=[]
    for line in f:
        linea = line.replace("\n","") 
        #datos[largo,máscara,contraseña]
        mascara=""
        for t in linea:
            if t.isupper(): mascara+="U"
            elif t.islower(): mascara+="L"
            elif t.isdigit(): mascara+="D"
            else: mascara+="S"
        datos.append([i,len(linea),linea,mascara])
        conteo.append(mascara)
        i+=1
#print(collections.Counter(conteo).most_common())
max_pass=i
print("Passwords loaded:",max_pass)
mascaras=collections.Counter(conteo).most_common()
print("TOP 20 MASK\n===========\n")
sum_porcentaje=0
for i in range(0,20):
    porcentaje=round(100*(mascaras[i][1]/max_pass),2)
    sum_porcentaje+=porcentaje
    print(i+1,")",mascaras[i][0],"- Lenght:",len(mascaras[i][0]),"-",mascaras[i][1],"times -",porcentaje,"%")
print("\n============\nSUM:",round(sum_porcentaje,2),"%")
