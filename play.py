from labirinto import Labirinto
#istanziando l'oggetto, il gioco parte
player = Labirinto()
go_on = True
while go_on == True:
    scelta = int(input("Cosa vuoi fare? \n    Premi 1 per guardarti intorno, 2 per cercare, 3 per muoverti e 4 per uscire \n --->"))
    if scelta == 4:
        go_on = player.esci()
    elif scelta ==1:
        player.show()
    elif scelta == 2:
        go_on = player.watch()
    elif scelta == 3:
        mosse = player.mosse_valide()
        muoviti_qui = input("\n In che direzione andare? \n --->")
        go_on = player.move(muoviti_qui,mosse)
    
    