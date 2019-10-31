import zmq
import threading


class SeverType:
    STRING = 0,
    PICKLE = 1


class ReplayServer(threading.Thread):

    def __init__(self, topic, callback, server_type=SeverType.PICKLE, url=None):
        threading.Thread.__init__(self)
        self.daemon = True

        if url is None:
            url = "ipc:///tmp/" + topic

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.bind(url)
        self._stop_event = threading.Event()
        self.callback = callback
        self.server_type = server_type
        self.start()

    def stop(self):
        self._stop_event.set()

    def _stopped(self):
        return self._stop_event.is_set()

    def _send(self):
        msg = self.socket.recv()
        response = self.callback(msg)
        self.socket.send(response)

    def _send_pyobj(self, protocol=2):
        msg = self.socket.recv_pyobj()
        response = self.callback(msg)
        self.socket.send_pyobj(response, flags=0, protocol=protocol)

    def run(self):
        while not self._stopped():
            if self.server_type == SeverType.STRING:
                self._send()
            else:
                self._send_pyobj()
