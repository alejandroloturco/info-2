y={}

class personas:
    def __init__(self) -> None:
        self.__name = "" #se privatizo
        self.height = 0.0
        self.age = 0

    def comer(self,comida):
        print (f"Esta comiendo {comida}")
    
    def dormir(self,):
        print (f"Esta comiendo {comida}")
    
    def comer(self,comida):
        print (f"Esta comiendo {comida}")


class casco:
    def __init__(self):
        self.tam = 0
        self.ne = 0
        self.ub = ""

    def __str__(self) -> str:
        return f"Aqui estamos {self.tam}"


    def registrar(self,u):
        self.ub = u
        print(f"El casco quedo registrado en  {self.ub}")
c=0
while True:
    x=casco()
    x1=casco()
    x2=casco()
    x3=casco()
    x4=casco()
    x3.registrar("23")
    y[c]=x
    c+=1