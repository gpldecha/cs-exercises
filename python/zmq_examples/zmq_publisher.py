import zmq
import pickle


class Publisher:

    def __init__(self, topic, url="ipc:///tmp/zmqtest"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(url)
        self.topic = topic

    def publish(self, data, protocol=pickle.HIGHEST_PROTOCOL):
        self.socket.send_string(self.topic, zmq.SNDMORE)
        self.socket.send_pyobj(data, protocol=protocol)
