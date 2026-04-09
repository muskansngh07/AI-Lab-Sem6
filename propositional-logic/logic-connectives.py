from sympy import symbols
from sympy.logic.boolalg import And,Or,Not

P,Q=symbols('P Q')

expr1=And(P,Q)
expr2=Or(P,Q)
expr3=Not(P)

print("P AND Q =",expr1)
print("P OR Q =",expr2)
print("NOT P =",expr3)

print("\nEvaluate (P AND Q) when P=True, Q=False")
print(expr1.subs({P:True,Q:False}))