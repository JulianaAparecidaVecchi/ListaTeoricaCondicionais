print("-----ELEITOR-----")
ida=int(input("DIGITE SUA IDADE: "))
if ida<16:
    print("Não eleitor")
elif ida>=16 and ida<18:
    print("Eleitor facultativo") 
else:
    print("Eleitor obrigatório") 
print("----------------------")
