"""
Problema: Alocação de turnos

Individuo:

Matriz 7xN onde N é o número de funcionários a serem alocados
Valores a serem inseridos:
0 - Folga
1 - Turno do dia
2 - Turno da tarde
3 - Turno da noite

Exemplo
    | D | S | T | Q | Q | S | S |
F1  | 1 | 1 | 1 | 0 | 0 | 2 | 2 |
F2  | 2 | 2 | 2 | 1 | 1 | 0 | 0 |
F3  | 3 | 3 | 3 | 0 | 0 | 1 | 1 |
F4  | 0 | 0 | 0 | 3 | 3 | 3 | 3 |
F5  | 1 | 1 | 1 | 0 | 0 | 1 | 1 |

O alocamento deve ser feito de acordo com uma segunda tabela, que
determina o número mínimo de funcionário por turno em cada dia da semana

Exemplo tabela de requisitos
        | D | S | T | Q | Q | S | S |
0(dia)  | 3 | 3 | 2 | 2 | 2 | 3 | 3 |
1(tarde)| 1 | 1 | 2 | 2 | 2 | 1 | 1 |
2(noite)| 0 | 1 | 1 | 1 | 1 | 1 | 0 |

Entradas do usuário: número de funcionários e tabela de requisitos

Cálculo do fitness
Para cada dia da semana:

|Numero de funcionarios necessarios - numero de funcionarios alocados|

O fitness será a somatória desse cálculo para os 3 dias da semana, quando
o fitness do individuo é igual a 0, a solução é aceita.



"""

def gerar():

    #Eric

def mutar():

    #Tamie

def cruzar():

    #Douglas

def avaliar():

    #Vinicius
