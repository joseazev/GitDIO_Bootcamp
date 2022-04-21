def quantidade_numeros_positivos():
  counter = 0
  for _ in range(6):
      number = float(input())
      if number > 0:
        counter += 1 
  print("{} valores positicos".format(counter))

