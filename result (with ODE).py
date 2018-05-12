import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m
from scipy.integrate import odeint

g=9.8
losses=0.1
tx=0.
ty=0.
x0=5.
y0=70.
v0x=25.
v0y=10.
x=x0
y=y0
vx=0.
vy=0.
x_dir=1
time=([0,0])
sol=([0,0])

fig, ax = plt.subplots()
fig.set_size_inches(4., 3., forward=True)
circle, = ax.plot([], [], 'bo', ms=5)
coord = np.array([x0,y0,x,y,v0x,v0y,vx,vy,tx,ty,x_dir])

def init():
    ax.set_xlim([0., 50.])
    ax.set_ylim([0., 80.])
    return circle,

def updatefig(frame):
    def v(vopros, t, v0):
        return v0 - g * t
    
    coord[8] += 0.05
    coord[9] += 0.05

    if coord[10]:
        if coord[2] <= 50:
            coord[6] = coord[4]
        else:
            coord[8] -= coord[8] - 0.05
            coord[4] = - coord[4]
            coord[6] = coord[4]
            coord[0] = 50
            coord[10] = 0
    else:
        if coord[2] >= 0:
            coord[6] = coord[4]
        else:
            coord[8] -= coord[8] - 0.05
            coord[4] = - coord[4]
            coord[6] = coord[4]
            coord[0] = 0
            coord[10] = 1
        
    if coord[3] >= 0:
        coord[7] = v(0, coord[9], coord[5])
    else:
        coord[9] -= coord[9] - 0.05
        coord[1] = coord[3] + 2
        coord[5] = - coord[7]*(1 - losses)
        coord[7] = v(0, coord[9], coord[5])
        
    coord[2] = coord[6] * coord[8] + coord[0]
    time = ([0,coord[9]])
    sol = odeint(v, coord[1], time, args=(coord[5],))   
    coord[3] = sol[1]
    
    circle.set_xdata(coord[2])
    circle.set_ydata(coord[3])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=2000, init_func=init, interval=1, blit=True, repeat=False)

plt.show()
