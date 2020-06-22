OPTION 1
def noDupe(string):
  a = {} #vai criar um dicionário para armazenar as letras
  for char in string:
    if char in a: #se i está nas letras já capituradas, vamos encerrar o código
      #print(a)
      return False
    else: #caso contrário, vamos armazenar
      a[char] = 1
  #print(a)
  return True
 
 
 def noDupe(string):
  a = [] #vai criar uma lista armazenar as letras
  for char in string:
    if char in a: #se i está nas letras já capituradas, vamos encerrar o código
      print(a)
      return False
    else: #caso contrário, vamos armazenar
      a.append(char)
  print(a)
  return True
