class Operation :
    def __init__ (self, nombre1 = 5, nombre2 = 8) :
        self.nombre1 = nombre1
        self.nombre2 = nombre2



Operation = Operation ()
print ("Le nombre1 est " + str (Operation.nombre1))
print ("Le nombre2 est " + str (Operation.nombre2))