# aula-rad-python

## Métodos de leitura de arquivo

**_arquivo_.read**: tipo string, retorna o conteúdo inteiro do arquivo

**_arquivo_.readline**: tipo string, retorna uma única linha do arquivo

**_arquivo_.readlines**: tipo lista, retorna cada linha como um índice em uma lista

> Esses métodos retornam o "\n", porém essa informação muitas vezes não é necesária, portanto usamos o método _strip_.

## Método Strip

Tipo string, usado para remover caracteres "invísiveis" como o "\n" e também para remover espaços em branco adicionais.

O método strip remove caracteres do início e do final da linha

_sintaxe: string.strip(caracteres)_

caracteres: Opcional. Um conjunto de caracteres a remover como caracteres iniciais/finais

- strip: remove os caracteres extras no início e no fim
- lstrip: remove os caracteres extras no início
- rstrip: remove os caracteres extras no fim

## Método count

Contar quantas vezes uma palavra ou letra aparece

Recebe como parâmetro a palavra que deseja contar e retorna a quantidade em inteiro de instâncias que ela aparece

_sintaxe: string.count("_palavra ou letra a ser analisada_")_

## Método split

quebrar uma string em palavras (lista)

_sintaxe: string.split(separator, maxsplit)_

separator: Opcional. Especifica o separador a ser usado ao dividir a string. Por padrão, qualquer espaço em branco é um separador.
maxsplit: Opcional. Especifica quantas divisões devem ser feitas. O valor predefinido é -1, que é "todas as ocorrências"

## Método join

juntar uma lista de palavras em uma única string

sintaxe: string.join(iterable)

_string_: Obrigatótio. O caractere ou string que será usado como separador

_iterable_: Obrigatório. Uma lista com strings.

## Método Upper e Lower

upper deixa o texto em caixa alta

lower deixa o texto em caixa baixa

## Função len

retorna a quantidade de caracteres em uma string

## Função replace

substituir trechos de texto

sintaxe: frase.replace

## Função startswith() e endswith()

verifica se uma frase ou palavra começa com uma string, retorna um booleano
