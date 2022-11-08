import matplotlib.pyplot as plot
import numpy as np
edades = [1.679	,1.187,	0.234,	1.78,	1.458,	2.628,	0.504,	0.951,	1.383,	0.486,
0.561,	0.494,	4.923,	0.635,	0.504,	2.606,	0.382,	1.38,	2.7,	0.468,
2.771,	3.141,	1.019,	2.516,	1.182,	2.258,	0.161,	8.055,	0.464,	2.312,
2.327,	0.761,	1.876,	1.506,	2.451,	0.831,	5.715,	0.699,	1.45,	3.582,
0.684,	3.192,	1.427,	0.518,	2.198,	0.922,	1.597,	2.66,	2.933,	4.518,
]
arreglo = np.asfarray(edades)
intervalos = range(int(min(edades)), int(max(edades)) + 2) #calculamos los extremos de los intervalos

plot.hist(x=arreglo, bins=intervalos, color='#F2AB6D', rwidth=0.85)
plot.title('Histograma ejercicio 4 - matplotlib - codigopiton.com')
plot.xlabel('x')
plot.ylabel('y')
plot.xticks(intervalos)

plot.show() #dibujamos el histograma