import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

def equation(y0, t):
    R, u = y0
    return u, (P_g-P_0-70000*np.sin(2*np.pi*31700*t)-2*sigma/R- 4*miu*u/R+(2*sigma/R_0+P_0-P_g)*(R_0/R)**(3*k))/(R*rho)-3*u**2/(2*R)

R_0 = 0.0000055
u_0 = 0
rho = 1000
sigma = 0.0728
miu = 8.9*10**(-4)
P_g = 2330
P_0 = 10000
k = 1.33

time1 = np.arange(0, 0.00005, 0.00000000025)
R_1 = odeint(equation, [R_0, u_0], time1)
V1 = R_1[:,1]
R1 = R_1[:,0]*10**6
x = time1*10**6

plt.xlabel('time / $\mu$s')
plt.ylabel('Radius of the bubble / $\mu$m')
plt.plot(x,R1, 'b')
plt.show()