print("Manipulação com Strings em Python")

texto = input("Digite um texto qualquer: ")

texto_limpo = texto.strip()

print(texto_limpo)

print(f"\nTEXTO EM MAIUSCULO: {texto_limpo.upper()}")
print(f"texto em minusculo: {texto_limpo.lower()}")

print(f"Quantidade de palavras: {len(texto_limpo.split())}")

print(f"Quantidade de 'a': {texto_limpo.lower().count("a")}")

print(f"Primeira palavra: {texto_limpo.split()[0]}")
print(f"Última palavra: {texto_limpo.split()[len(texto_limpo.split()) - 1]}")

print(f"Texto invertido: {texto_limpo[::-1]}")

print(f"Texto com 'a' substituído por '@': {texto_limpo.lower().replace("a", "@")}")