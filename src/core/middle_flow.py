"""Middle Flow Engine — Pendulum physics & damping"""
class MiddleFlowEngine:
    def __init__(self, center: float = 0.0, sensitivity: float = 0.1, damping: float = 0.05, clamp: float = 5.0):
        self.center = center
        self.sensitivity = sensitivity
        self.damping = damping
        self.clamp = clamp
        self.position = center

    def step(self, push: float, pull: float, dt: float = 0.1) -> float:
        net = (push - pull) * self.sensitivity * dt
        self.position += net
        self.position += (self.center - self.position) * self.damping
        if self.position > self.clamp:
            self.position = self.clamp
        elif self.position < -self.clamp:
            self.position = -self.clamp
        return self.position
