# aula-rad-python

**_arquivo_.read**: tipo string, retorna o conteúdo inteiro do arquivo

**_arquivo_.readline**: tipo string, retorna uma única linha do arquivo

**_arquivo_.readlines**: tipo lista, retorna cada linha como um índice em uma lista

> Esses métodos retornam o "\n", porém essa informação muitas vezes não é necesária, portanto usamos o método _strip_.

### Método Strip

Tipo string, usado para remover caracteres "invísiveis" como o "\n" e também para remover espaços em branco adicionais. 

O método strip remove caracteres do início e do final da linha

- strip: remove os caracteres extras no início e no fim
- lstrip: remove os caracteres extras no início
- rstrip: remove os caracteres extras no fim

### Método count

contar quantas vezes uma palavra ou letra aparece

recebe como parâmetro a palavra que deseja contar e retorna a quantidade em inteiro de instâncias que ela aparece

### Método split

quebrar uma string em palavras (lista)

### Método join

juntar uma lista de palavras em uma única string

sintaxe: string.join(iterable)

_string_ é o que vai ser usado para separar os elementos

_iterable_ é a variável com a lista a ser iterada

### Método Upper e Lower

upper deixa o texto em caixa alta

lower deixa o texto em caixa baixa

### Função len

retorna a quantidade de caracteres em uma string

### Função replace

substituir trechos de texto

sintaxe: frase.replace

### Função startswith() e endswith()

verifica se uma frase ou palavra começa com uma string, retorna um booleano
