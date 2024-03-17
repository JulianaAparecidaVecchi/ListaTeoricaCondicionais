print("-----APOSENTADORIA-----")
ida=int(input("DIGITE SUA IDADE EM ANOS: "))
tempt=int(input("DIGITE SEU TEMPO DE SERVIÇO EM ANOS: "))
if ida>=65 or tempt>=30 or (ida>=60 and tempt>=25):
    print("PODE SE APOSENTAR") 
else:
    print("NÃO PODE SE APOSENTAR AINDA")
print("----------------------")