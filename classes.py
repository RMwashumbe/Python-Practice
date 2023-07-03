class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.capacity=capacity
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.capacity)
#create an object
myobj=Magari("Toyota","white",2016,"1500cc")
myobj.onyesha()
