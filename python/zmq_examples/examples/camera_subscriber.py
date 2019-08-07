import cv2
import signal

import sys
sys.path.append('../')
from zmq_subscriber import Subscriber


class GracefulKiller:

    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, _, __):
        self.kill_now = True


if __name__== "__main__":
    print('Start subscribing')
    subscriber = Subscriber(topic='camera', url="ipc:///tmp/zmqtest")

    killer = GracefulKiller()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    while not killer.kill_now:
        subscriber.update()
        if subscriber.data is not None:
           cv2.imshow('frame', subscriber.data)
           cv2.waitKey(2)
    cv2.destroyAllWindows()
