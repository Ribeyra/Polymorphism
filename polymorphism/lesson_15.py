class TcpConnectionError(Exception):
    pass


class TcpConnection:
    # BEGIN (write your solution here)
    def __init__(self, ip, port):
        self.connect_states = {
            'connect': ConnectedState,
            'disconnect': DisconnectedState
        }
        self.ip = ip
        self.port = port
        self.connect_state = self.connect_states['disconnect']

    def get_current_state(self):
        return self.connect_state.get_state()

    def write(self, data):
        self.connect_state.sent(self, data)

    def connect(self):
        self.connect_state.connect(self)

    def disconnect(self):
        self.connect_state.disconnect(self)

    def sent(self, data):
        return 'Data sent to IP via port'
    # END


class ConnectedState:
    # BEGIN (write your solution here)
    @staticmethod
    def get_state():
        return 'connected'

    @staticmethod
    def connect(TcpConnInst):
        raise TcpConnectionError('Connection already connected')

    @staticmethod
    def disconnect(TcpConnInst):
        TcpConnInst.connect_state = TcpConnInst.connect_states['disconnect']

    @staticmethod
    def sent(TcpConnInst, data):
        TcpConnInst.sent(data)
    # END


class DisconnectedState:
    # BEGIN (write your solution here)
    @staticmethod
    def get_state():
        return 'disconnected'

    @staticmethod
    def connect(TcpConnInst):
        TcpConnInst.connect_state = TcpConnInst.connect_states['connect']

    @staticmethod
    def disconnect(TcpConnInst):
        raise TcpConnectionError('Connection already disconnected')

    @staticmethod
    def sent(TcpConnInst, data):
        raise TcpConnectionError(
            'It is not possible write to closed connection'
        )
    # END


connection = TcpConnection('132.223.243.88', 2342)
connection.connect()
