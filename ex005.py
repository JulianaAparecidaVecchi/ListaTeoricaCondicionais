print("-----PESO IDEAL-----")
h=float(input("DIGITE SUA ALTURA EM METROS: "))
gen=str(input("DIGITE SEU GÊNERO (F=Feminino e M=Masculino): "))

if gen=="F" or gen=="f":
    pesof=(62.1*h)-44.7
    print(f"SEU PESO IDEAL EM KG É: {pesof:.2f}")
elif gen=="M" or gen=="m":
    pesom=(72.7*h)-58
    print(f"SEU PESO IDEAL É: {pesom:.2f}")   
else:
    print("ERRO")   
print("----------------------")      