import zmq


class Subscriber:

    def __init__(self, topic, url="ipc:///tmp/zmqtest"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(url)
        self.socket.setsockopt(zmq.SUBSCRIBE, topic.encode('ascii'))
        self.topic = topic
        self.data = None
        self.recv_string = None

    def update(self):
        try:
            self.recv_string = self.socket.recv_string()
            self.data = self.socket.recv_pyobj()
        except zmq.ZMQError as e:
            self.data = None
            self.recv_string = None
            print(e)
