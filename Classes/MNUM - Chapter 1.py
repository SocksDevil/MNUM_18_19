import math
import pylab
from decimal import Decimal
import numpy as np

# valor = np.float32(math.exp(1)-1)
valor = math.exp(1)-1
i = 0
for i in range(1,26):
    valor=valor*i-1
    print(f'{valor:.9f}')

erro_abs = abs(valor - 73905327359.146500000000000000)
print("Erro Absoluto: ", erro_abs)

print("Erro Relativo", abs((erro_abs/valor)*100))

import matplotlib.pyplot as plt
x = np.linspace(-20,10,1000)
z = (np.sqrt(x+1) - np.sqrt(x))*((np.sqrt(x+1) + np.sqrt(x))/(np.sqrt(x+1) - np.sqrt(x)))
y= 1/(np.sqrt(x+1) - np.sqrt(x))
p = z-y
pylab.ylim(top=1e-15)
pylab.ylim(bottom=-1e-15)
pylab.plot(x,y)
pylab.plot(x,z)
pylab.plot(x,p)
pylab.show()
