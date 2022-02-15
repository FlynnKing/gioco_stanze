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
    mappa = []
    def __init__(self):
        
        p = random.randint(0,6)
        c = 0
        for riga in range(len(self.labirinto)):
            num = self.labirinto[riga].count('x')
            if c+num < p and p!=-1:
                c+=num
            else:
                for colonna in range(len(self.labirinto[riga])):
                    if self.labirinto[riga][colonna] == 'x':
                        
                        if c==p:
                            self.x = riga
                            self.y = colonna
                            self.esplorate.append([riga,colonna])
                            p = -1
                        c+=1
        nome = input("Come ti chiami? \n")
        self.nome = nome
        for x in range(len(self.labirinto)):
            riga = []
            for y in range(len(self.labirinto[x])):
                riga.append('.')
            self.mappa.append(riga)
        print("Benvenuto, ",self.nome," ,ti trovi qui \n \n")
        self.mappa[self.x][self.y] = 'x'
        for riga in self.mappa:
            print(riga)
                        
                        
    def show(self):
        for riga in self.labirinto:
            print(riga)
            
    
    def vite(self):
        return 11-len(self.esplorate)
    

