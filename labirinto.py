import random

class Labirinto:
    nomi = ['Parcheggio','Atrio','Area relax','Segreteria','Aula Azzurra','Aula Gialla','Presidenza']
    esplorate = []
    x= -1
    y = -1
    labirinto = [
        ['.','.','.','x','.'],
        ['.','.','x','x','.'],
        ['.','x','x','x','.'],
        ['.','.','x','.','.'],
        ['.','.','.','.','.']
        ]
    def __init__(self,nome):
        self.nome = nome
        p = random.randint(0,6)
        c = 0
        for riga in range(len(self.labirinto)):
            num = self.labirinto[riga].count('x')
            if c+num < p:
                c+=num
            else:
                for colonna in range(len(self.labirinto[riga])):
                    if self.labirinto[riga][colonna] == 'x':
                        
                        if c==p:
                            self.x = riga
                            self.y = colonna
                            self.esplorate.append([riga,colonna])
                            print("Benvenuto, ",nome,' ti trovi in ',self.nomi[p])
                            self.nomi.remove(self.nomi[p])
                            return None
                        c+=1
                        
    def show(self):
        for riga in self.labirinto:
            print(riga)
            
    
    