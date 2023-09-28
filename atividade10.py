peso = float(input("digite o seu peso:"))
altura =float(input("digitea sua altura"))
imc = peso/(altura*altura)

if(imc<18.5):
    print("você esta abaixo do peso")
if(imc>= 18.5)and(imc<25):
    print("seu peso está normal")
if(imc>=25)and(imc<30):
    print("você está acima do peso")
else:
    print("você esta obeso")