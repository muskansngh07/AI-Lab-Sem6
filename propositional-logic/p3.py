from pyDatalog import pyDatalog

pyDatalog.create_terms('parent, grandparent, X,Y,Z')

+ parent('John','Mary')
+ parent('Mary','Sam')
+ parent('Sam','Lilly')

grandparent(X,Z) <= parent(X,Y) & parent(Y,Z)

print(grandparent("John",Z))

