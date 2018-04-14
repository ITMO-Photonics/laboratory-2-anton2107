import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m

g=9.8
losses=0.1
tx=0.
ty=0.
x0=10.
y0=100.
v0x=20.
v0y=0.
x=x0
y=y0
vx=0.
vy=0.
x_dir=1

fig, ax = plt.subplots()
circle, = ax.plot([], [], 'bo', ms=5)
coord = np.array([x0,y0,x,y,v0x,v0y,vx,vy,tx,ty,x_dir])

def init():
    ax.set_xlim([0., 110.])
    ax.set_ylim([0., 110.])
    return circle,

def updatefig(frame):
    coord[8] += 0.05
    coord[9] += 0.05

    if coord[10]:
        if coord[2] <= 110:
            coord[6] = coord[4]
        else:
            coord[8] -= coord[8] - 0.05
            coord[4] = - coord[4]
            coord[6] = coord[4]
            coord[0] = 110
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
        coord[7] = coord[5] - g*coord[9]
    else:
        coord[9] -= coord[9] - 0.05
        coord[1] = coord[3] + 2
        coord[5] = - coord[7]*(1 - losses)
        coord[7] = coord[5] - g*coord[9]
        
    coord[2] = coord[6]*coord[8] + coord[0]
    coord[3] = coord[5]*coord[9]-g*coord[9]*coord[9]/2+coord[1]
    
    circle.set_xdata(coord[2])
    circle.set_ydata(coord[3])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=2000, init_func=init, interval=1, blit=True, repeat=False)

plt.show()
