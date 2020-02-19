# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# Não há nada mais chato na programação quando um erro acontece.
# O Python tem como filosofia não deixar o erro passar em branco.
# Porem há erros que podem ocorrer mas não por nossa 
# responsabilidade.

# Exemplos: 
# - Alguem apagou o arquivo que seria de leitura.
# - Caiu a rede na hora de comunicar e salvar dados no banco de
# dados.
# - Alguem por acidente executou o script sql errado e apagou o 
# banco de dados.
# - Em Web Scraping, um dos sites que vocês querem coletar dados
# saiu fora do ar.
# - No campo: "Digite quantos filhos você tem?" a pessoa escreveu:
# "Tenho uma menina e um menino" quando deveria digitar somente o
# número 2!

# ATENÇÃO! Silenciar o erro não deve ser uma pratica para incubrir
# código ruin! 

# Por que silenciar o código?
# Todo erro do python causa interrupção imediata do código e
# esta interrupção encerra o programa. Ao silenciar o erro, o 
# programa passa a tratar este erro de forma diferente conforme 
# o programador queira.


# Quando usar?
# Quando uma parte do código funciona, mas em determinada condição
# ele pode aparecer um erro. Exemplo: Digitar uma string ao inves
# de um valor inteiro.

# Quando um erro pode finalizar um processo, porem o arquivo ou
# conecção não foi fechada. ( arquivo.close() )

# Quais erros existem?
# Pode ser encontrado os erros e seus significados no site:
# https://docs.python.org/3.7/library/exceptions.html

# Aqui em baixo está a arvore de erros do Python 3.7: 

#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError 
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


# Quais as formas de executar a excessão?
# 

try:
    #digitar um código
except:
    # O que fazer se um erro aparecer.

# Neste caso, o except não possui uma indicação do erro.
# ISSO NÂO É INDICADO FAZER! 
# > KeyboardInterrupt (interrupção pelo teclado. quando digita Ctrl+c 
# na execução do código)
# > MemoryError (Quando não há mais memória livre