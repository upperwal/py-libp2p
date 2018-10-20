from .stream_interface import IStream
import asyncio

class Stream(IStream):

    def __init__(self, context, peer_id):
        self.context = context
        self.peer_id = peer_id

        peer_store = context.peer_store
        peer_addr = peer_store.get(peer_id)

        # look up peer_id -> multiaddr in peer store
        # parse multiaddr and set_protocol based on it
        # open connection to multiaddr
        # save connection to stream's state
        self.open_connection(ip, port)

    async def open_connection(self, ip, port):
        self.reader, self.writer = await asyncio.open_connection(ip, port)

    def protocol(self):
        """
        :return: protocol id that stream runs on
        """
        return self.protocol_id

    def set_protocol(self, protocol_id):
        """
        :param protocol_id: protocol id that stream runs on
        :return: true if successful
        """
        self.protocol_id = protocol_id

    def read(self):
        """
        read from stream
        :return: bytes of input
        """
        pass

    def write(self, _bytes):
        """
        write to stream
        :return: number of bytes written
        """
        pass

    def close(self):
        """
        close stream
        :return: true if successful
        """
        pass