"""Examples showing how to do symbolic quantum manipulations."""

from sympy import I, symbols, expand

from sympy.physics.quantum import (
    Operator, Ket, Bra,
    Commutator, AntiCommutator,
    InnerProduct, OuterProduct,
    KroneckerDelta, Dagger,
    apply_operators, represent,
    TensorProduct, tensor_product_simp
)

# Create abstract bras and kets and perform basic operators on them.

psi = Ket('psi')
psi

Dagger(psi)

Dagger(psi)*psi
type(_)

psi*Dagger(psi)
type(_)

phi = Ket('phi')
alpha, beta = symbols('alpha beta', complex=True)

e = alpha*psi + beta*phi
e

Dagger(e)*e
apply_operators(expand(_))

# Now create operators and commutators

A = Operator('A')
B = Operator('B')
C = Operator('C')

A*B == B*A

(A+B)**2
_.expand()

Commutator(A,B)
_.doit()

Commutator(A*B,B+C)
_.expand(commutator=True)
_.doit().expand()
Dagger(_)

# Create some tensor products

TensorProduct(I*A,B)
Dagger(_)

TensorProduct(A,B+C)*TensorProduct(psi, phi)
tensor_product_simp(_)
_.expand(tensorproduct=True)
