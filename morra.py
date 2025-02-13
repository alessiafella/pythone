import random
def scelta_computer():
    return random.choice(["sasso", "carta", "forbici"])
def deteremina_vincitore(giocatore, computer):
    if giocatore == computer:
        return "Pareggio!"
    elif (giocatore == "sasso" and computer == "forbici") or \
         (giocatore == "forbici" and computer == "carta") or \
         (giocatore == "carta" and computer "sasso"):
        return "Hai vinto!"
    else:
        return "Hai perso!" 


         















