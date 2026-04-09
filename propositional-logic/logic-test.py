from kanren import run,var,Relation,facts
from kanren.core import lall

parent=Relation()
facts(parent,("John","Mary"),("Mary","Sam"),("Sam","Lilly"))

x=var()
result=run(0,x,parent("John",x))
print("Children of John: ",result)

y=var()
result1=run(0,x,lall(parent("John",y),parent(y,x)))
print("Grandchildren of John: ",result1)