import matplotlib.pyplot as plt
from pid import PID
import numpy as np

if __name__ == "__main__":

    dt = 0.01

    pid = PID()
    pid.Kp = 1.0*dt
    pid.Ki = 0.0001
    pid.Kd = 0.001
    pid.set_target(1.0)


    steps = int(10.0/dt)

    current = np.empty(shape=(steps, 2))
    current[0, 0] = 0.0
    current[0, 1] = 0.0
    v_prev = 0.0
    r_prev = 0.0
    r = 0.0
    k = 0.5
    for i in range(1, steps):

        a = pid.update(r, dt)/10.0
        v = a*(i*dt) + v_prev - k*v_prev
        r = r_prev + 0.5*(v + v_prev)*(i*dt)
        v_prev = v
        r_prev = r

        current[i, 0] = i*dt
        current[i, 1] = r

    plt.close('all')
    plt.figure()
    plt.plot(current[:, 0], np.ones(len(current)), '--r')
    plt.plot(current[:, 0], current[:, 1], '-b')
    plt.show()