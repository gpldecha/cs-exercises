import signal
import time
import sys
sys.path.append('../')
from reply_server import ReplayServer


class GracefulKiller:

    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, _, __):
        self.kill_now = True


def callback(msg):
    print('Received:')
    print(msg)
    return dict({'Server': 'Thanks!'})


def str_callback(msg):
    print('Received:')
    print(msg)
    return 'Server: Thanks'.encode('ascii')


if __name__ == "__main__":
    interrupter = GracefulKiller()

    _type = 'py'

    if _type == "str":
        server = ReplayServer(topic='request_reply', callback=str_callback)
    elif _type == 'py':
        server = ReplayServer(topic='request_reply', callback=callback)

    while not interrupter.kill_now:
        time.sleep(0.1)
    server.stop()
    print('Exit')
