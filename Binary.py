from IPython.display import clear_output 

def main():
  clear_output()
  print("Escreva o número para converter")
  num = str(input("Número: "))
  print("Escreva a base do número exemplo: decimal -> '10'")
  base = int(input("base: "))
  converterDecPTodos(converterPDec(num, base))
  continuarPrograma()

def converterPDec(num, base):
  if base == 10: return num
  print("\n Conversão para Decimal \n")
  #base -> decimal
  ind = len(num) - 1
  pos = 0
  result = 0
  while ind >= 0: 
    prod = int(hexNum(num[ind])) * (base**pos)
    print(num[ind] + " X " + str(base) + "^" + str(pos) + " = " + str(prod))
    result += prod
    pos += 1
    ind -= 1
  print("Resultado = " + str(result) + "\n")
  return result

def converterDecPTodos(num):
  #decimal -> bases
  bases = [2, 8, 16]
  indexbase = 0
  while indexbase <= len(bases) - 1:
    numero = int(num)
    base = bases[indexbase]
    print(
        "\n Convertendo o número em decimal para a base: " + str(base) + "\n"
    )
    parar = False
    stringNums = ""
    while parar == False:
      resto = numero % base
      print(
          "número -> "
           + str(numero) + " / " + str(base) + " | resto = " + str(resto)
      )
      stringNums += str(numHex(resto))
      numero = int(numero / base)
      #top 10 gambiarra
      if numero < base:
        resto = numero % base
        print(
            "número -> "
             + str(numero) + " / " + str(base) + " | resto = " + str(resto)
        )
        stringNums += str(numHex(resto))
        numero = int(numero / base)
        parar = True
    print("resultado = " + stringNums[::-1])
    indexbase += 1

def continuarPrograma():
  print("\n Continuar programa? escreva s para SIM")
  inp = input("resposta: ")
  if inp == 's':
    main()
  else: return

#nojeira
def hexNum(hex):
  if   hex == 'A': return 10
  elif hex == 'B': return 11
  elif hex == 'C': return 12
  elif hex == 'D': return 13
  elif hex == 'E': return 14
  elif hex == 'F': return 15
  else: return hex

def numHex(num):
  if   num == 10: return 'A'
  elif num == 11: return 'B'
  elif num == 12: return 'C'
  elif num == 13: return 'D'
  elif num == 14: return 'E'
  elif num == 15: return 'F'
  else: return num


main()
