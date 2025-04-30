# aula-rad-python

## Métodos de leitura de arquivo

**_arquivo_.read**: tipo string, retorna o conteúdo inteiro do arquivo

**_arquivo_.readline**: tipo string, retorna uma única linha do arquivo

**_arquivo_.readlines**: tipo lista, retorna cada linha como um índice em uma lista

> Esses métodos retornam o "\n", porém essa informação muitas vezes não é necesária, portanto usamos o método _strip_.

## Método Strip

Tipo string, usado para remover caracteres "invísiveis" como o "\n" e também para remover espaços em branco adicionais.

O método strip remove caracteres do início e do final da linha

    sintaxe: string.strip(caracteres)

caracteres: Opcional. Um conjunto de caracteres a remover como caracteres iniciais/finais

- strip: remove os caracteres extras no início e no fim
- lstrip: remove os caracteres extras no início
- rstrip: remove os caracteres extras no fim

## Método count

Contar quantas vezes uma palavra ou letra aparece

Recebe como parâmetro a palavra que deseja contar e retorna a quantidade em inteiro de instâncias que ela aparece

    sintaxe: string.count("palavra ou letra a ser analisada")

## Método split

quebrar uma string em palavras (lista)

    sintaxe: string.split(separator, maxsplit)

separator: Opcional. Especifica o separador a ser usado ao dividir a string. Por padrão, qualquer espaço em branco é um separador.

maxsplit: Opcional. Especifica quantas divisões devem ser feitas. O valor predefinido é -1, que é "todas as ocorrências"

## Método join

juntar uma lista de palavras em uma única string

    sintaxe: separator.join(list)

_separator_: Obrigatótio. O caractere ou string que será usado como separador

_list_: Obrigatório. Uma lista com strings.

## Método Upper e Lower

Upper transforma o texto inteiro em caixa alta

Lower transforma o texto inteiro em caixa baixa

    sintaxe: string.upper/lower()

## Função len

retorna a quantidade de caracteres em uma string

    sintaxe: len(string)

## Função replace

substituir trechos de texto

    sintaxe: string.replace("frase a ser substituída", "frase a qual quer adicionar")

## Função startswith() e endswith()

verifica se uma frase ou palavra começa com uma string, retorna um booleano

    sintaxe: string.startswith("palavra"): retorna True se a string começa com a palavra
    sintaxe: string.endswith("palavra"): retorna True se a string termina com a palavra
