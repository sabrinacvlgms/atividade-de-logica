a = float(input("digite sua altura")) 
b = input("digite seu sexo")
calc_masc =  (72.7 * a) - 58
calc_fem = (62.1 * a) - 44.7

if b == "F":
    print(calc_fem)
else:
    print(calc_masc)
