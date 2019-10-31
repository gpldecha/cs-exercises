import zmq


class RequestClient:

    def __init__(self, topic, url=None):
        if url is None:
            url = "ipc:///tmp/" + topic

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect(url)

    def send(self, msg):
        self.socket.send(msg.encode('ascii'))
        msg = self.socket.recv()
        print(msg)

    def send_pyobj(self, msg, protocol=2):
        self.socket.send_pyobj(msg, flags=0, protocol=protocol)
        replay = self.socket.recv_pyobj()
        print(replay)
