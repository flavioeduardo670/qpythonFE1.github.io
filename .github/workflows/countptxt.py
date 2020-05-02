def counttxt(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Insira o nome do texto: ")
with open(filename) as f:
  texto = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * counttxt(texto, char) / len(texto)
  print("{0} - {1}%".format(char, round(perc, 2)))
