a= float(input("insira o primeiro numero"))
b= float(input("insira o segundo numero"))
c= float(input("insira o terceiro numero"))
if a>b and a>c and b>c:
    print(a,b,c)
elif a>b and a>c and c>b:
    print(a,c,b)
elif b>a and b>c and a>c:
    print(b,a,c)
elif b>a and b>c and c>a:
    print(b,c,a)
elif c>b and c>a and a>b:
    print(c,a,b)
elif c>b and c>a and b>a:
    print(c,b,a)