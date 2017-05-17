import numpy as np


Qsa=100
Qsb=500*0.5+0*0.5
print('DP ( Dynamic Programming ): '+' Qsa= %d;' % Qsa + '      ' + 'Qsb= %d' % Qsb)


Qsa=0
Qsb=0
sum_ra = 0
sum_rb = 0
for i in range(0, 1):
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
for i in range(0, 1):
        ra = 100
        rb = 500  if i % 2 else 0
        print(ra ,rb)       
        Qsa = Qsa + alph * ( ra - Qsa)
        Qsb = Qsb + alph * ( rb - Qsb)
        print(Qsa ,Qsb)
        
print('TD ( Temporal Difference ): '+' Qsa= %d;' % Qsa + '      ' + 'Qsb= %d' % Qsb)



base=1# no base,alph must be small;large i need small alph
alph=0.0001
Hsa=0
Hsb=0
pia=100
pib=100
bs=0
num_random=0
for i in range(0, 500):
        pia=np.exp(Hsa)/(np.exp(Hsa)+np.exp(Hsb))
        pib=np.exp(Hsb)/(np.exp(Hsa)+np.exp(Hsb))
	num_random =  np.random.uniform (0,1,1)       
        action = 0 if num_random < pia else 1  
        print(' pia= %f;' % pia + '      ' + 'pib= %f' % pib) 
        print(' action = %d;' % action + '     ' + 'np.random.uniform = %f' % num_random)
     
        if (action == 0):
        	ra = 100 
		print(' ra= %d;' % ra )
		bs += ra

 
	if (action == 1) :        
		rb = 500 if np.random.uniform() < 0.5 else 0
		print('rb= %d' % rb) 
        	bs += rb 



        bs = bs/(i+1) if (base==1) else 0               
        Hsa = Hsa + alph * (ra - bs ) * (1-pia)if (action==0) else Hsa + alph * (rb - bs ) * (0-pib)
        Hsb = Hsb + alph * (ra- bs ) * (0-pia)if (action==0) else Hsb + alph * (rb - bs ) * (1-pib)
        print(' Hsa= %f;' % Hsa + '      ' + 'Hsb= %f' % Hsb)    
        
pia=np.exp(Hsa)/(np.exp(Hsa)+np.exp(Hsb))
pib=np.exp(Hsb)/(np.exp(Hsa)+np.exp(Hsb))
print('PG ( Policy Gradients ): '+' pia= %f;' % pia + '      ' + 'pib= %f' % pib) 




#############
#############
#Hsa Hsb  pia  pib  action reward Hsa   Hsb  pia  pib
#0    0   0.5  0.5    1     200   0      0   0.5  0.5
#0    0   0.5  0.5    1     200   0      0   0.5  0.5
#0    0   0.5  0.5    0     100   -3.3   3.3  ?  ? 



