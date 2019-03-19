import pybullet as p
import time
import math
from datetime import datetime
from time import sleep


if __name__ == "__main__":

	p.connect(p.GUI)
	p.setRealTimeSimulation(1)
	p.setGravity(0, 0, -9.81)

	p.setAdditionalSearchPath("./data")
	p.loadURDF("plane.urdf", [0, 0, 0])
	wallId = p.loadURDF("wall/wall.urdf", [0, 0, 1])

	p.addUserDebugLine([0, 0, 0])

	while 1:
		p.stepSimulation()

		sleep(0.1)
