print("-----UNIVERSIDADE-----\n1-PUCPR\n2-UNICAMP")
uni=int(input("DIGITE O NÚMERO DA SUA UNIVERSIDADE: "))
nota1=float(input("DIGITE SUA NOTA PRIMEIRO BIMESTRE: "))
nota2=float(input("DIGITE SUA NOTA DO SEGUNDO BIMESTRE: "))
media=(nota1+nota2)/2
if uni==1:
    if media>=7:
        print("APROVADO!")
    elif media<7 and media>=4:
        print("RECUPERAÇÃO")  
    else:
        print("REPROVADO")      
elif uni==2: 
    if media>=5:
        print("APROVADO!")
    else:
        print("REPROVADO")       
else:
    print("ERRO")  
print("----------------------")  