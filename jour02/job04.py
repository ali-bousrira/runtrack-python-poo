class Student :
    def __init__ (self, nom, prenom, num) :
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num
        self.__credit = 0
        self.__level = self.__studentEval ()

    def add_credits (self, mut) :
        try :
            float (mut)
            if mut > 0 :
                self.__credit += mut
                self.__level = self.__studentEval ()
            else :
                print ("le mutateur doint etre superieur a 0")
        except :
            print ("le mutateur doint etre superieur a 0")

    def info (self) :
        print ("Le nombre de credit de " + self.__nom + " " + self.__prenom + "est de " + str (self.__credit) + "point")
    
    def __studentEval (self) :
        if self.__credit >= 90 :
            return "Excellent"
        elif self.__credit >= 80:
            return "Trés bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60 :
            return "Passable"
        else :
            return "Insufisant"
    
    def studentInfo (self):
        print ("Nom = " + self.__nom + "\n" + "Prénom = " + self.__prenom + "\n" + "id = " + str (self.__num_etudiant) + "\n" + "Niveau = " + self.__level) 

student = Student ("Jhon", "Doe", 145, )

student.info()

student.add_credits(10)

student.info()

student.add_credits(10)

student.info()

student.add_credits(10)

student.info()

student.add_credits(45)

student.studentInfo ()