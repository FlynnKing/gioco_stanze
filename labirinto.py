import random

class Labirinto:
    nomi = ['Parcheggio','Atrio','Area relax','Segreteria','Aula Azzurra','Aula Gialla','Presidenza']
    esplorate = []
    
    x= -1
    y = -1
    labirinto = [
        ['.','.','.','x','.'],
        ['.','.','x','x','.'],
        ['.','x','x','.','.'],
        ['.','x','x','.','.'],
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
                    if p!= -1:
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
        self.mappa[self.x][self.y] = '!'
        for riga in self.mappa:
            print(riga)
                        
    def move(self,place):
        place = place.upper()
        if place not in ['S','N','O','E']:
            cond = False
            while cond==False:
                print("\n Non puoi andare lì, sciocchino. Scegli una direzione valida \n")
                place = input()
                place = place.upper()
                if place in ['S','N','O','E']:
                    cond= True
        self.mappa[self.x][self.y] = 'x'
        if place=='N':
            
            self.x-=1
        elif place == 'S':
            self.x +=1
        elif place == 'E':
            self.y+=1
        else:
            self.y-=1
        self.esplorate.append([self.x,self.y])
        self.mappa[self.x][self.y] = '!'
        
            
    def show(self):
        for riga in self.mappa:
            print(riga)
            
    
    def vite(self):
        return 11-len(self.esplorate)
    

