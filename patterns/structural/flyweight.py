'''
flyweight is a structural design pattern that lets us fit more 
objects in the memory by reusing the intrensic stae of the object

'''

class Carflyweight(object):
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color

    def __str__(self):
        return ' '.join([self.make,self.model,self.color])

class CarFlyweightFactory(object):
    flyMap={}
    
    def getCarFlyweight(self,make,model,color):
        key=make+model+color
        if key not in self.flyMap:
            self.flyMap[key]=Carflyweight(make,model,color)
        return self.flyMap[key]
       

    def listCarFlywights(self):
        retult=[]
        for car in self.flyMap.values():
            retult.append(str(car))
        return retult
    
pdb=[]    
def addCarToPoliceDb(flyfac,name,num,make,model,color):
    car=flyfac.getCarFlyweight(make,model,color)
    pdb.append((name,num,car))



if __name__ == "__main__":
    flyFac=CarFlyweightFactory()
    addCarToPoliceDb(flyFac,"mohan","abc123","Chevrolet", "Camaro2018", "pink")
    addCarToPoliceDb(flyFac,"ram","abc2345","Mercedes Benz", "C300", "black")
    addCarToPoliceDb(flyFac,"guru","fgh123","Mercedes Benz", "C500", "red")
    addCarToPoliceDb(flyFac,"divya","xyz342","BMW", "M5", "red")
    addCarToPoliceDb(flyFac,"kappu","123asw","BMW", "X6", "white")
    addCarToPoliceDb(flyFac,"thanu","73bws","Chevrolet", "Camaro2018", "pink")
    addCarToPoliceDb(flyFac,"gayu","23nuxs","Mercedes Benz", "C300", "black")
    addCarToPoliceDb(flyFac,"sarasa","njks234","Mercedes Benz", "C500", "red")
    addCarToPoliceDb(flyFac,"malar","95fdcd","BMW", "M5", "red")
    addCarToPoliceDb(flyFac,"jag","463ncjd","BMW", "X6", "white")

    print(f'length of pdb {len(pdb)}')
    print(f'length of flyfac {len(flyFac.listCarFlywights())}')

    print('*'*30)
    print(flyFac.listCarFlywights())

    