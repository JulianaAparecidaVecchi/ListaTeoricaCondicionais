print("-----EQUAÇÃO QUADRÁTICA-----")
a=float(input("DIGITE UMA VALOR PARA a: "))
b=float(input("DIGITE UMA VALOR PARA b: "))
c=float(input("DIGITE UMA VALOR PARA c: "))
delta=b**2-4*a*c
if a!=0:
    if delta>0:
        print("Existem duas raízes reais distintas")
    elif delta==0:
        print("Existem duas raízes reais iguais") 
    else:
        print("Existem duas raízes imaginárias conjugadas")              
else:
    print("O a DEVE SER DIFERENTE DE ZERO!")   
print("----------------------")
