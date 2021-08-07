import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

for i in range(0,3):                            #loops through code 3 times to cycle through rho values
    # Lorenz paramters and initial conditions
    sigma, beta, = 10, 2.667                    #sigma and beta values (stays the same)
    u0, v0, w0 = 0, 1, 1.05                     #initial u,v,w values
    if (i == 0):                                #first loop rho is 10
        rho = 10
    if (i == 1):                                #second loop rho is 20
        rho = 20
    if (i == 2):                                #third loop rho is 25
        rho = 25

    # Maximum time point and total number of time points
    tmax, n = 100, 10000

    def lorenz(X, t, sigma, beta, rho):
        """The Lorenz equations."""
        u, v, w = X
        up = -sigma*(u - v)
        vp = rho*u - v - u*w
        wp = -beta*w + u*v
        return up, vp, wp

    # Integrate the Lorenz equations on the time grid t
    t = np.linspace(0, tmax, n)
    f = odeint(lorenz, (u0, v0, w0), t, args=(sigma, beta, rho))
    x, y, z = f.T

    # Plot the Lorenz attractor using a Matplotlib 3D projection
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the line multi-coloured by plotting it in segments of length s which
    # change in colour across the whole time series.
    s = 10
    c = np.linspace(0,1,n)
    for i in range(0,n-s,s):
        ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=(1,c[i],0), alpha=0.4)

    # Remove all the axis clutter, leaving just the curve.
    ax.set_axis_off()

    plt.show()

   #plots 2-D graph of t and x
    plt.title("x(t) Test")      #title             
    plt.xlabel("T")             #x-axis title
    plt.ylabel("X")             #y-axis title
    plt.plot(t,x)               #plots t and x
    plt.show()                  #shows graph

   #plots 2-D graph of t and y
    plt.title("y(t) Test")      #title      
    plt.xlabel("T")             #x-axis title
    plt.ylabel("Y")             #y-axis title
    plt.plot(t,y)               #plots t and y
    plt.show()                  #shows graph

   #plots 2-D graph of t and z 
    plt.title("z(t) Test")      #title
    plt.xlabel("T")             #x-axis title
    plt.ylabel("Z")             #y-axis title
    plt.plot(t,z)               #plots t and z
    plt.show()                  #shows graph
