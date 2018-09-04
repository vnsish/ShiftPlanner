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
Para cada turno:

|Numero de funcionarios necessarios - numero de funcionarios alocados|

O fitness será a somatória desse cálculo para os 3 turnos, quando o fitness
do individuo é igual a 0, a solução é aceita.



"""

#def gerar():

    #Eric

#def mutar():

    #Tamie

#def cruzar():

    #Douglas

def avaliar(ind, req):

    mat = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    nota = 0
    
    for i in range(len(ind[0])):
        dia = 0
        tarde = 0
        noite = 0

        for j in range(len(ind)):
            if ind[j][i] == 1:
                dia = dia + 1
            if ind[j][i] == 2:
                tarde = tarde + 1;
            if ind[j][i] == 3:
                noite = noite + 1;

        mat[0][i] = dia
        mat[1][i] = tarde
        mat[2][i] = noite
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            nota = nota + abs(req[i-1][j-1] - mat[i-1][j-1])

    return nota
            
        
def testeavalia():        
    indi = [[1, 1, 1, 0, 0, 2, 2],
            [2, 2, 2, 1, 1, 0, 0],
            [3, 3, 3, 0, 0, 1, 1],
            [1, 0, 1, 3, 3, 3, 3]]
    
    requ = [[2, 1, 2, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]]


    print(indi)
    print(requ)

    print(avaliar(indi, requ))

def main():

    func = input('Numero de funcionarios: ')
    print('Insira a tabela de requisitos: ')
          
    req = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    dias = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    
    for i in range(len(req)):
        for j in range(len(req[0])):
            req[i][j] = input('Turno {0} - {1}: '.format(i+1, dias[j]))

    print(req)


main()
                
