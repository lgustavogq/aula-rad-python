import tkinter as tk
from tkinter import messagebox

tela = tk.Tk()
filename = "cadastros.txt"

def iniciarTela():
    tela.title("Sistema de Cadastro")
    tela.geometry("800x600")

def divNome():
    rotuloNome = tk.Label(tela, text="Digite o nome a cadastrar:")
    rotuloNome.pack()

def divIdade():
    rotuloIdade = tk.Label(tela, text="Digite a idade a cadastrar:")
    rotuloIdade.pack()

def divProfissao():
    rotuloProfissao = tk.Label(tela, text="Digite a profissão a cadastrar:")
    rotuloProfissao.pack()

def submitDados():
    nome = (entradaNome.get()).strip()
    nome = (nome.lower()).capitalize()
    idade = entradaIdade.get().strip()
    profissao = entradaProfissao.get().strip()
    profissao = (profissao.lower()).capitalize()

    if not nome or not idade or not profissao:
        messagebox.showerror("Erro no cadastro", "Todos os campos devem ser preenchidos")
        return
    
    if int(idade) < 0 or int(idade) >= 150:
        messagebox.showerror("Erro", "Insira uma idade válida")
        return


    with open(filename, "a") as file:
        file.write(f"{nome}-{idade}-{profissao}\n")
    messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

def showList():
    quantRegistro = 0
    arrayProfissao = []
    with open(filename, "r") as file:
        for row in file:
            if row != "": 
                arrayIndividuo = row.split("-")
                tk.Label(tela, text=f"{arrayIndividuo[0].strip()}, {arrayIndividuo[1].strip()}, {arrayIndividuo[2].strip()}").pack()
                quantRegistro += 1
                arrayProfissao.append(arrayIndividuo[2])
    tk.Label(tela, text=f"Quantidade total de registros: {quantRegistro}").pack()
    maiorValor = 0
    maisProfissao = ""
    for i in range(len(arrayProfissao)):
        if maiorValor < arrayProfissao.count(arrayProfissao[i]):
            maisProfissao = arrayProfissao[i]
    tk.Label(tela, text=f"Profissão mais repetida: {maisProfissao}").pack()

def createBinFile():
    with open(filename, "rb") as binFile:
        contentBin = binFile.read()

    with open("cadastros_backup.bin", "wb") as binFile:
        binFile.write(contentBin)

    tk.Label(tela, text="Arquivo binário criado").pack()

iniciarTela()

divNome()
entradaNome = tk.Entry(tela)
entradaNome.pack()

divIdade()
entradaIdade = tk.Entry(tela)
entradaIdade.pack()

divProfissao()
entradaProfissao = tk.Entry(tela)
entradaProfissao.pack()

submitButton = tk.Button(tela, text="Enviar", command=submitDados)
submitButton.pack()

showListButton = tk.Button(tela, text="Exibir Lista", command=showList)
showListButton.pack()

createBinFile()

tela.mainloop()