import signal
import sys
sys.path.append('../')
from request_client import RequestClient
import numpy as np


class GracefulKiller:

    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, _, __):
        self.kill_now = True


if __name__ == "__main__":
    client = RequestClient(topic='request_reply')
    # client.send('Hello')
    msg = dict({
        'Client': 'Hello',
        'vector1': np.zeros(shape=(1, 4), dtype=np.float32)
                })
    client.send_pyobj(msg)
