frase = "\n     Testando diferentes funções de manipulação de string em Python.     \n\n"
lista_frase = ["Teste", "de", "manipulações"]

frase_strip = frase.strip()

print(f"Frase original:\n'{frase}'")

print(f"Frase com o método strip:\n'{frase_strip}'\n")

print("Usando 'count' para contar elementos em uma string:")
print(f"Quantas vezes a palavra 'Python' aparece: {frase.count("Python")}")
print(f"Quantas letras 'a' existem na frase: {frase.count("a")}\n")

print(f"Dividindo a frase em uma lista:\n{frase.split()}\n")

print(f"Juntando uma lista para formar uma palavra:\nFrase original: {lista_frase}\nFrase junta: {" ".join(lista_frase)}\n")

print(f"Texto em maiúsculo: {frase_strip.upper()}")
print(f"Texto em minúsculo: {frase_strip.lower()}\n")

print(f"Tamanho da frase: {len(frase_strip)}\n")

print(f"Alterando 'Python' por 'C':\n{frase_strip.replace("Python", "C")}")