
#print("Olá", "mundo", sep="-") # Saída: Olá-mundo
#print("Olá", "Python", end="!\n") # Saída: Olá Python!


#print("18", "04", "2023", sep="/") 
# Saída: nome; sobrenome; email (útil em CSVs)
#print("nome", "sobrenome", "email", sep="; ") 


# Continuando impressões na mesma linha
#print("Loading", end=" |")
#print("[OK]") # Saída: Loading [OK]

#nome = input("Digite seu nome: ")
#print("Olá", nome)

#itens = input("Digite itens separados por vírgula: ")
#itens= itens.split(',')
#print("Itens:", itens)

# Convertendo a entrada para inteiro
#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")
# Convertendo a entrada para float
#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")

#def trinta_por_cento(): 
    #print("Digite números para adicionar à lista (digite 'done' para terminar):")
   # numeros = []
    #while True:
        #entrada = input()
        #if entrada.lower() == 'done':
          #  break
       # else:
           # numeros.append(int(entrada))
   # print("Números coletados:", numeros)

#def imprimir_informacoes (nome, idade, cidade):
    #print ("Nome:", nome, sep=" ", end=", ")
    #print ("Idade:", idade, sep=" ", end=" , ")
    #print ("Cidade:", cidade, sep=" ")
    # Exemplo de uso da função
#imprimir_informacoes("Mariana", 24, "Rio de Janeiro")

#def calcular ():
   #num1= float (input("Digite o primeiro número: "))
   # num2= float (input("Digite o segundo número: "))
   # operacao = input("Digite a operação desejada (+, -, *, /): ")
   # if operacao == '+':
       # resultado= num1 + num2
   # elif operacao == '*':
       # resultado = num1 * num2
    #elif operacao == '/':
     #   if num2 != 0:
          #  resultado = num1 / num2
       # else:
          #  print ("Erro: divisão por zero!")
          #  return
   # else:
           # print ("Operação inválida.")
           # return
   # print ("Resultado:", resultado)
    
#def lista_de_compras():
    #itens = input ("Digite os itens da lista de compras,separados por virgula: ")
   # lista = itens.split (",")
   # print ("Lista de compras:")
   # for item in lista:
       # print (item.strip())
      
#def celsius_para_fahrenheit():
  #  celsius = float (input("Digite a temperatura em graus Celsius: "))
   # fahrenheit = (celsius * 9/5) + 32
   # print("A temperatura em Fahrenheit é: ", fahrenheit)       
        
        
def digitar_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (digite 'sair' para sair): ")
        if nome.lower() == 'sair':
            break
        nomes.append (nome)
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)
        
