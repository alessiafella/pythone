class Employee:
    def __init__(self, nome, cognome, salario):
        self.nome = nome
        self.cognome = cognome
        self.salario = salario

class Manager(Employee):
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario)
        self.reparto = reparto

    def __repr__(self):
        return ("Il manager " + self.nome + " " + self.cognome +
            " del reparto " + self.reparto +
            " guadagna " + str(self.salario))
        

marcoRicci = Employee("Marco", "Bianchi", 1000)
andreaCormani = Manager("Luca", "Rossi", 3000, "Marketing")
print(lucaRossi)
