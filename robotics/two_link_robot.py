import numpy as np

Deg2Rad = 0.0174533


class Robot:

    def __init__(self, lengths=np.array([4, 3, 2]), thetas=np.array([10., 20., 30.])):
        self.lengths = lengths
        self.thetas = np.array(thetas * Deg2Rad)
        self.jacobian = np.ones((3, 3))
        self.link1 = np.zeros((2, 2))
        self.link2 = np.zeros((2, 2))
        self.link3 = np.zeros((2, 2))
        self.update()

    def command(self, thetas):
        self.thetas = np.copy(thetas)

    def get_wrist(self):
        return np.array([self.link3[1, 0], self.link3[1, 1], self.thetas[2]])

    def update(self):

        length1 = self.lengths[0]
        length2 = self.lengths[1]
        length3 = self.lengths[2]

        angle1 = self.thetas[0]
        angle2 = self.thetas[1]
        angle3 = self.thetas[2]

        # link 1
        dir1 = np.array([np.cos(angle1), np.sin(angle1)])
        dir1 /= np.linalg.norm(dir1)
        self.link1[1, :] = dir1 * length1

        # link 2
        self.link2[0, :] = np.copy(self.link1[1, :])
        dir2 = np.array([np.cos(angle1 + angle2), np.sin(angle1 + angle2)])
        dir2 /= np.linalg.norm(dir2)
        self.link2[1, :] = self.link2[0, :] + length2 * dir2

        # link 3
        self.link3[0, :] = np.copy(self.link2[1, :])
        dir3 = np.array([np.cos(angle1 + angle2 + angle3), np.sin(angle1 + angle2 + angle3)])
        dir3 /= np.linalg.norm(dir3)
        self.link3[1, :] = self.link3[0, :] + length3 * dir3

        s1 = np.sin(self.thetas[0])
        s12 = np.sin(self.thetas[0] + self.thetas[1])
        s123 = np.sin(self.thetas[0] + self.thetas[1] + self.thetas[2])

        c1 = np.cos(self.thetas[0])
        c12 = np.cos(self.thetas[0] + self.thetas[1])
        c123 = np.cos(self.thetas[0] + self.thetas[1] + self.thetas[2])

        L1 = self.lengths[0]
        L2 = self.lengths[1]
        L3 = self.lengths[2]

        self.jacobian[0][0] = -L1*s1 - L2*s12 - L3*s123
        self.jacobian[0][1] = -L2*s12 - L3*s123
        self.jacobian[0][2] = -L3*s123

        self.jacobian[1][0] = L1*c1 + L2*c12+L3*c123
        self.jacobian[1][1] = L2*c12 + L3*c123
        self.jacobian[1][2] = L3*c123


class Visualise:

    def __init__(self, robot):
        self.robot = robot
        self.line1 = None
        self.line2 = None
        self.line3 = None
        self.pts1 = np.zeros((2, 2))
        self.pts2 = np.zeros((2, 2))
        self.pts3 = np.zeros((2, 2))

    def draw(self, ax):
        link1 = self.robot.link1
        link2 = self.robot.link2
        link3 = self.robot.link3
        self.line1 = ax.plot(link1[:, 0], link1[:, 1])
        self.line2 = ax.plot(link2[:, 0], link2[:, 1])
        self.line3 = ax.plot(link3[:, 0], link3[:, 1])


def resolve_rate_controller(v_c, J, thetas, dt):
    Jinv = np.linalg.inv(J)
    dtheta_c = np.dot(Jinv, v_c)
    return thetas + dtheta_c*dt, dtheta_c
