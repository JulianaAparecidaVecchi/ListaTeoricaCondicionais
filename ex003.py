print("-----TEMPERATURA-----")
temp=int(input("DIGITE A TEMPERATURA EM GRAUS CELSIUS: "))
if temp<15:
    print("Está frio!")
elif temp>=15 and temp<=25:
    print("Temperatura agradável")
else:
    print("Está calor!")   
print("----------------------")