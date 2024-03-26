def soma (a,b):
    return a+b

def quadrado (a):
    return a**2

def hipotenusa(cat1,cat2):
    return soma(quadrado(cat1),quadrado(cat2)) **(1/2)

def simples(cor):
    if cor == "azul":
        return 'escolheu certo'
    
def medio(cor):
    if cor == "azul":
        return "escolheu certo"
    else:
        return "escolha outra cor"
    
def completo(cor):
    if cor == "azul":
        return "escolheu certo"
    elif cor == "marrom":
        return "não tem salvação"
    else:
        return "tente outra cor"

contador=0
while contador <10:
    print (contador)
    contador += 1

for i in range(10):
    print (i)
    
for item in [1,45,78,"a", [3,5]]:
    print (item)
    
for letra in 'minha string':
    print(letra)
    
def triangulo (x):
    for i in range(x):
        print((i + 1) * "*")
