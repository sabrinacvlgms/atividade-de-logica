numeroidentificacao = float(input("digite o numero de identificação: "))
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
me = float(input("digite a media dos exercicios: "))
ma = (nota1 + nota2*2 + nota3*3 + me)/7

print("numero do aluno: ", numeroidentificacao)
print("sua primeira nota foi: ", nota1)
print("sua segunda nota foi: ", nota2)
print("sua terceira nota foi: ", nota3)
print("sua media dos exercicios foi: ", me)
print("sua media de aproveitamento foi: ", ma)

if ma >= 90:
    print("seu conceito correspondente foi A")
    print("APROVADO")
elif ma >= 75 and ma < 90:
    print("seu conceito correspondente foi B")
    print("APROVADO")
elif ma >= 60 and ma < 75:
    print("seu conceito correspondente foi C")
    print("APROVADO")
elif ma >= 40 and ma < 60:
    print("seu conceito correspondente foi D")
    print("REPROVADO")
else:
    print("seu conceito correspondente foi E")
    print("REPROVADO")