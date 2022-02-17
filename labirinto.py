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
            print("Attento, la salute è importante! A te ne rimane poca, esattamente ne hai ancora , ",self.vite," \n")
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
    
    def spawn(self):
        caso = random.randint(1,3)
        if caso==2:
            print("E' comparso un mostro! E' Davide che ti sfida a programmare \n")
            print(" [-]  [-]  [-] \n")
            print("Ci sono 3 pc, ma uno solo funziona! Quale scegli, 1 2 o 3?")
            vincente = random.randint(1,3)
            scelta = input("\n    ")
            if scelta != vincente:
                print("hai scelto il pc sbagliato, disonore!")
                print("\n Passi ore a cercare di aggiustare il pc, pentito. Ma Bruno ha installato Kali Linux e non ci capisci un ***** \n")
                if self.vite >4:
                    perse = random.randint(0,1)
                    if perse == 0:
                        self.vite -= 2
                        print("\n hai perso 2 vite! Te ne rimangono ",self.vite)
                    else:
                        self.vite -=4
                        print("\n Ti prende troppo a male e perdi 4 vite davanti al computer.\n Te ne rimangono ",self.vite," \n")
                elif self.vite > 2 and self.vite <=4:
                    self.vite -=1
                    print("Davide ti vede stanco e ti aiuta bruciando il pc. Perdi una vita per il calore, te ne rimangono ",self.vite," \n")
                else:
                    print("Già eri stanco, mo t'ammazzi. Hai perso.")
                    return False
            else:
                self.vite -=1
                print("\n Hai scelto il pc giusto, ma comunque ti stanchi e perdi una vita. Ne hai ancora ",self.vite," \n")
        elif caso ==1:
            self.vite +=2
            print("\n hai trovato una macchinetta del caffè. Ti ristori e recuperi 2 vite. Ne hai ancora ",self.vite," \n")
        
                
        