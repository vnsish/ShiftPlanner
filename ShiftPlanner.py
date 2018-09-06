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

import random

class Cromossomo:
   def __init__(self, funcionarios, tabela = []):
      tabela = []
      self.taxa = 1
      self.fit = -1
      agenda = []
      for x in range(0, funcionarios):
         for y in range (0, 7):
            agenda.append(random.randint(0,3))
         tabela += [agenda]
         agenda = []
      self.tabela = tabela

   def avalia(self, req):

      mat = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
      self.fit = 0
      
      for i in range(len(self.tabela[0])):
        dia = 0
        tarde = 0
        noite = 0

        for j in range(len(self.tabela)):
            if self.tabela[j][i] == 1:
                dia = dia + 1
            if self.tabela[j][i] == 2:
                tarde = tarde + 1;
            if self.tabela[j][i] == 3:
                noite = noite + 1;

        mat[0][i] = dia
        mat[1][i] = tarde
        mat[2][i] = noite
    
      for i in range(len(mat)):
        for j in range(len(mat[0])):
            self.fit = self.fit + abs(req[i-1][j-1] - mat[i-1][j-1])
            
   def mutar(self):
      if(random.random() < self.taxa):
         self.tabela[random.randint(0, len(self.tabela)-1)][random.randint(0, 6)] = random.randint(0,3)

   def cruzar(self, c):
      filho = self
      
      a = random.randint(0, len(self.tabela)-1)
      b = random.randint(0, 6)

      filho.tabela[a][b] = c.tabela[a][b]

      return filho

      

def gerar():
   populacao = []
   workers = int(input("funcionarios: "))
   for z in range(0,200):
      c = Cromossomo(workers)
      populacao.append(c)
	
   return populacao            
        
def aleatorio(pop):
   
   
   random.shuffle(pop)
   return pop[0]
   
   
def main():

    populacao = gerar()
    
    print('Insira a tabela de requisitos: ')
          
    req = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    dias = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']

    for i in range(len(req)):
        for j in range(len(req[0])):
            req[i][j] = int(input('Turno {0} - {1}: '.format(i+1, dias[j])))

    found = 0
   
    while found == 0:
      for c in populacao:
          c.avalia(req)
          if (c.fit == 0):
             found = 1
             solucao = c

      populacao.sort(key = lambda x: x.fit)

      nova = []
      for i in range(len(populacao)):
         a = aleatorio(populacao)
         b = populacao[0]
         c = a.cruzar(b)
         c.mutar()
         nova.append(c)
      populacao = nova
      
    print(solucao.tabela)


main()
                
