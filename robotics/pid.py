

class PID:

    def __init__(self):
        self.Kp = 0.0
        self.Kd = 0.0
        self.Ki = 0.0

        self.target = 0.0
        self.error = 0.0
        self.error_prev = 0.0
        self.integral = 0.0
        self.derivative = 0.0

    def update(self, current, dt):
        self.error = self.target - current
        print(self.error)
        self.integral += self.error*dt
        self.derivative = (self.error - self.error_prev)/dt
        return self.Kp*self.error + self.Ki*self.integral + self.Kd*self.derivative

    def set_target(self, target):
        self.target = target
        self.integral = 0.0
        self.derivative = 0.0
