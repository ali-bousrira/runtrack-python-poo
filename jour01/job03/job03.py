class Operation :
    def __init__ (self, nombre1 = 5, nombre2 = 8) :
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition (self) :
        print (str (self.nombre1) + " + " + str (self.nombre2) + " = " + str (self.nombre1 + self.nombre2))



Operation = Operation ()

Operation.addition ()