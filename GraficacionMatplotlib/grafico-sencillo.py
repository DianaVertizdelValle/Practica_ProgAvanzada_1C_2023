# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:23:09 2022

@author: javierdz
"""

import matplotlib.pyplot as plt
import math as m

N=100 # cantidad de datos
f=3 # frecuencia Hz
tiempo = [i/N for i in range(N) ]
serie1 = [m.sin(2*m.pi*f*t) for t in tiempo ]
serie2 = [m.cos(2*m.pi*f*t) for t in tiempo ]




# Gráfico PU
plt.subplot(2, 1, 1)    # 2 fila, 1 columnas, primer gráfico
plt.plot(tiempo,serie1, label="Google")
plt.grid()
plt.title('Series google')

plt.subplot(2, 1, 2)    # 2 fila, 1 columnas, segundo grafico
plt.plot(tiempo,serie2, label="Nike")
plt.title('Series nike')

plt.grid()
plt.legend()
plt.show()


