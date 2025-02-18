class Message:
    def __init__(self, destinatario, mittente):
        self._destinatario = destinatario
        self._mittente = mittente
        self.testo = ""
    def append(self, riga):
        """Aggiungi una riga in fondo al testo del messaggio"""
        self.testo = self.testo + riga + "\n" #self.testo += riga + "\n"
    def toString(self):
        """Restituisce il testo del messaggio"""
        return "Mittente: " + self._mittente + "\nDestination: " + self._destinatario + "\n" + self.testo

m = Message("io","tu")
m.append("Ciao")
m.append("Come va?")
print(m.toString())















    




