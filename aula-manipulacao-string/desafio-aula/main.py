with open("relatorio.txt", "r") as arquivo:
    raw_text = arquivo.read()
    clean_text = raw_text.strip()

with open("relatorio.txt", "w") as arquivo:
    arquivo.write(clean_text)

with open("relatorio.txt", "r") as arquivo:
    raw_text = arquivo.read()
    print(f"Quantidade de vezes que erro é mencionado: {raw_text.lower().count("erro")}")
    print(f"Quantidade de vezes que sucesso é mencionado: {raw_text.lower().count("sucesso")}")
    print(f"Quantidade de vezes que falha é mencionado: {raw_text.lower().count("falha")}")
    print(f"Quantidade de vezes que cliente é mencionado: {raw_text.lower().count("cliente")}")
    print(f"Quantidade de vezes que produto é mencionado: {raw_text.lower().count("produto")}")

with open("relatorio.txt", "r") as arquivo:
    raw_text = arquivo.readlines()
    for linhas in raw_text:
        linhas.capitalize()
        print(linhas)

