import numpy as np 
import matplotlib.pyplot as plt 

name=["molecular","cold HI","warm HIa","warm HIb","HII Regions","diffuse HII"]
N=1000.0
R=15000.0

def a(z,i):
	if (i==0): 
		return 0.58*np.exp(-(z/81.0)**2)
	if (i==1): 
		return 0.57*0.7*np.exp(-(z/127.0)**2)
	if (i==2): 
		return 0.57*0.18*np.exp(-(z/318.0)**2)
	if (i==3):
		return 0.57*0.11*np.exp(-z/403.0)
	if (i==4): 
		return 0.015*np.exp(-z/70.0)
	if (i==5): 
		return 0.025*np.exp(-z/1000.0)


r=np.arange(N/2)
r=r.astype(float)

for i in range(0,5):
	H05=a(R/2.0,i)
	H05=format(H05,'.2E')
	plt.plot(r,a(r,i),label=name[i]+" N(H=0.5)="+str(H05))

plt.legend()
plt.show()

