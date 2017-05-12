	
import numpy as np


Qsa=100
Qsb=500*0.5+0*0.5
print('DP ( Dynamic Programming ): '+' Qsa= %d;' % Qsa + '      ' + 'Qsb= %d' % Qsb)


Qsa=0
Qsb=0
sum_ra = 0
sum_rb = 0
for i in range(0, 10):
        ra = 100
        rb = 500  if i % 2 else 0
        print(ra ,rb)
        sum_ra += ra
        sum_rb += rb        
Qsa = sum_ra/(i+1)
Qsb = sum_rb/(i+1)        
print('MC ( Monte Carlo ): '+' Qsa= %d;' % Qsa + '      ' + 'Qsb= %d' % Qsb)



Qsa=0
Qsb=0
alph=0.01
for i in range(0, 1000):
        ra = 100
        rb = 500  if i % 2 else 0
        print(ra ,rb)       
        Qsa = Qsa + alph * ( ra - Qsa)
        Qsb = Qsb + alph * ( rb - Qsb)
        print(Qsa ,Qsb)
        
print('TD ( Temporal Difference ): '+' Qsa= %d;' % Qsa + '      ' + 'Qsb= %d' % Qsb)
