from Ficha import *

class Tablero:
    #Defina aquí los atributos de Tablero
    CasillasT = 0
    F1 = ""
    F2 = ""
    F3 = ""
    F4 = ""

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno


    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self, CasillasT):
        self.F1 = Ficha("morado")
        self.F2 = Ficha("rosado")
        self.F3 = Ficha("celeste")
        self.F4 = Ficha("Cafe")
        self.CasillasT = CasillasT
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    def mover(self):
        pos = 0
        while(pos < self.CasillasT):
            print("\nSigue la ficha de color", self.F1.color)
            self.F1.avanzar()
            pos = self.F1.posicion
            if(pos >= self.CasillasT):
                break
            else:
                print("\nSigue la ficha de color", self.F2.color)
                self.F2.avanzar()
                pos = self.F2.posicion
                if(pos >= self.CasillasT):
                    break
                else:
                    print("\nSigue la ficha de color", self.F3.color)
                    self.F3.avanzar()
                    pos = self.F3.posicion
                    if(pos >= self.CasillasT):
                        break
                    else:
                        print("\nSigue la ficha de color", self.F4.color)
                        self.F4.avanzar()
                        pos = self.F4.posicion
        print("\nTermino el juego, ya una ficha llego al final")
    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
