import numpy as np


def set_2d_inv_rotation(R, angle):
    R[0][0] = np.cos(angle)
    R[0][1] = np.sin(angle)
    R[1][0] = -np.sin(angle)
    R[1][1] = np.cos(angle)
    R[2][2] = 1


class DynamicSolver:

    def __init__(self):
        self.I = []  # list of moments computed at the center of mass of each link
        self.P = []  # list of center of masses of each link

    def solve(self):
        pass

    def iter_newton_euler(P, Pc, omega, domega, theta, dtheta, ddtheta, dv, m, Ic):
        R = np.array([[np.cos(theta), np.sin(theta), 0.], [-np.sin(theta), np.cos(theta), 0.], [0., 0., 1.0]])
        new_omega = np.dot(R, omega) + np.array([0., 0, dtheta])
        new_domega = np.dot(R, domega) + np.cross(np.dot(R, domega), np.array([0., 0., dtheta])) + np.array([0., 0., ddtheta])

        new_dv = np.cross(domega, P) + np.cross(omega, np.cross(omega, P)) + dv
        new_dv = np.dot(R, new_dv)

        dv_c = np.cross(new_domega, Pc) + np.cross(new_omega, np.cross(new_omega, Pc)) + new_dv

        F = m * dv_c
        N = np.dot(Ic, domega) + np.cross(omega, np.dot(Ic, omega))

        return new_omega, new_domega, new_dv, F, N


if __name__ == "__main__":
    R = np.zeros((3, 3))

    Pc1 = np.array([0.5, 0., 0.])
    Pc2 = np.array([0.5, 0., 0.])
    m1 = 4.6
    m2 = 2.3
    g = 9.8
    thetas = np.array([30.0, 30.0])*np.pi/180.0

    omega = np.zeros(3)
    domega = np.zeros(3)

    dtheta = 0.0
    ddtheta = 0.0

    dv = 0.0

    m = 0

    iter_newton_euler(np.zeros(3), np.zeros(3), omega, domega, thetas[0], dtheta, ddtheta, dv, m, np.zeros((3, 3)))

    set_2d_inv_rotation(R, np.pi/2)
    print('R {}', np.round(R, 2))