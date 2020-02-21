# https://www.alura.com.br/artigos/precisao-numeros-decimais-python

# Números sem precisão
from decimal import Decimal, getcontext
ganhos_julho = 99.91 * 5
print(ganhos_julho)

gastos_julho = 110.1 * 3
print(gastos_julho)

# Números com precisão
getcontext().prec = 10

ganhos_julho = Decimal(99.91) * 5
print(ganhos_julho)

gastos_julho = Decimal('110.1') * 3
print(gastos_julho)
