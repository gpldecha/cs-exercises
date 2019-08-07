import cv2
import signal

import sys
sys.path.append('../')
from zmq_publisher import Publisher


class GracefulKiller:

    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, _, __):
        self.kill_now = True


if __name__== "__main__":
    print('Start camera publisher')
    publisher = Publisher(topic='camera', url='ipc:///tmp/zmqtest')

    cap = cv2.VideoCapture(0)

    killer = GracefulKiller()
    i=0
    while not killer.kill_now:
        i += 1
        ret, frame = cap.read()
        publisher.publish(frame, protocol=2)
        print('Sent frame {}'.format(i))
