print("Calculadora melhorada ")
while True:#Condição de repetição, enquanto a resposta do usuário for 'S' o codigo se repetirá.
  num1=input(" Digite o primeiro número ")#Usado para solicitar que o usuário defina o primeiro número.
  num2=input(" Digite o segundo número ")#Usado para solicitar que o usuário defina o segundo número.
  operacao=input("Qual operacao deseja fazer ? \n 1-Somar \n 2-Subtrair \n 3-Multiplicar \n 4-Dividir \n ")#Para o usuário definir qual operação deseja realizar.
  if operacao == "1":#Condições criadas para reagir de acordo com a resposta do usuário.
    print('Você escolheu a opção 1, então a soma dos números escolhido é igaul a:')
  elif operacao == "2":  
    print('Você escolheu a opção 2, então a subtração dos números escolhido é igaul a:') 
  elif operacao == "3":
    print('Você escolheu a opção 3, então a Multiplicação dos números escolhido é igaul a:')
  elif operacao == "4":
    print('Você escolheu a opção 4, então a Divisão dos números escolhido é igaul a:')
  somar=float (num1) + float(num2)        #Operação para somar duas variáveis            #Converte o número definido pelo usuário em números fracinados também.
  subtrair=float (num1) - float(num2)        #Operação para subitrair duas variáveis
  multiplicar=float (num1) * float(num2)        #Operação para multiplicar duas variáveis
  dividir=float (num1) / float(num2)        #Operação para dividir duas variáveis
  if operacao == "1":#Condições criadas para mostrar no terminal a operação desejada pelo usuário.
    print(somar)
  elif operacao == "2":  
    print(subtrair) 
  elif operacao == "3": 
    print(multiplicar)
  elif operacao == "4":
    print(dividir)
  else:#Condição criada em caso de que nenhuma das opçoes seja validas, indicando no terminal
    print("Alternativa escolhida invalida!")
  reset=input('Deseseja fazer outra operação? \n S-SIM \n N-NÃO \n')#Estrutura para resetar o código, caso o usuário deseja fazer outra operação.
  if reset.upper() != "S":
    break#Usado para quebrar a repetição.
  

