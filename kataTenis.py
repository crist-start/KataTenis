class KataTenis:
    def __init__(self):
        self.num=0
        self.jug=[{'nombre':"",'puntaje':0},{'nombre':"",'puntaje':0}]

    def addJugador(self,nombre,puntaje):
        if (self.num<2):
            self.jug[self.num]['nombre']=nombre
            self.jug[self.num]['puntaje']=puntaje
            self.num=self.num+1
        else:
            print('no se puede ingresar mas jugadores')

    def obtenerP(self):
        punt=["love","fifteen","thirty","forty"]
        cad=""
        p1,p2=self.jug[0]['puntaje'],self.jug[1]['puntaje']
        dif=abs(p1-p2)
        if p1<p2:
            if p2<=3:
                cad=punt[p1]+','+punt[p2]
            elif dif<2:
                cad="advantage for "+self.jug[1]['nombre']
            else:
                cad="Gana "+self.jug[1]['nombre']
        elif p1==p2:
            if (p1< 3 and p2<3):
                cad=punt[p1]+" both"
            else:
                cad="deuce"
        else:
            if p1<=3:
                cad=punt[p1]+','+punt[p2]
            elif dif<2:
                cad="advantage for "+self.jug[0]['nombre']
            else:
                cad="Gana "+self.jug[0]['nombre']
                
        return cad

