import random

class Labirinto:
    nomi = ['Parcheggio','Atrio','Area relax','Segreteria','Aula Azzurra','Aula Gialla','Presidenza']
    esplorate = []
    places = {}
    x= 0
    y = 3
    vite = 10
    go_on = True
    winner = ''
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
                                self.winner = (riga,colonna)
                                #self.x = riga
                                #self.y = colonna
                                #self.esplorate.append((riga,colonna))
                                self.esplorate.append((0,3))
                                self.places[self.esplorate[-1]] = self.nomi[0]
                                self.nomi.remove(self.nomi[0])
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
            print(riga,'\n')
                        
    def move(self,place,mosse_valide):
        place = place.upper()
        if place not in mosse_valide:
            cond = False
            while cond==False:
                print("\n Non puoi andare lì, sciocchino. Scegli una direzione valida \n")
                place = input()
                place = place.upper()
                if place in mosse_valide:
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
        self.esplorate.append((self.x,self.y))
        self.mappa[self.x][self.y] = '!'
        self.vite -=1
        if self.vite <5 :
            print("Attento, la salute è importante! A te ne rimane poca, esattamente ne hai ancora , ",self.vite)
            if self.vite ==0:
                print("Peccato, hai finito le vite!")
                return False
        if self.esplorate[-1] not in self.places:
            self.places[self.esplorate[-1]] = self.nomi[0]
            self.nomi.remove(self.nomi[0])
        return True
            
    def show(self):
        print("Questa è la situazione corrente \n")
        for riga in self.mappa:
            print(riga)
    def mosse_valide(self):
        mosse_valide = []
        if self.labirinto[self.x-1][self.y] == 'x':
            mosse_valide.append('N')
        if self.labirinto[self.x+1][self.y] == 'x':
            mosse_valide.append('S')
        if self.labirinto[self.x][self.y+1] == 'x':
            mosse_valide.append('E')
        if self.labirinto[self.x][self.y-1] == 'x':
            mosse_valide.append('O')
        print("\n puoi spostarti qui, \n " ,mosse_valide)
        return mosse_valide
    def watch(self):
        print("\n attualmente ti trovi qui: ",self.places[self.esplorate[-1]])
        if self.esplorate[-1] == self.winner:
            print("\n Complimenti, " ,self.nome, " hai vinto! \n")
            print("Ti erano rimaste " ,self.vite, ' vite!')
            return False
        else:
            print("no, il manoscritto non è qui... ci muoviamo? \n")
            return True
        
        
        
    def esci(self):
        print("Peccato, hai perso!")
        return False
    

