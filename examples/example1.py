"""Basic operations."""
import errno
import os

from broadlinkhacktools import (
    PacketDecryptor,
    PacketFactory,
    PacketPrinter,
    PersistenceHandler
)
from broadlinkhacktools.protocol.const import DEFAULT_IV, DEFAULT_KEY


# Make packets from bytes.
packets = [
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xe4\x07:\x13\x14\x05\x07\x02\x00\x00\x00\x00\xc0\xa8\x01P\xc4\xdb\x00\x00\xff\xd3\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9fG0\xd36_j\x01\xa8\xc0\xf8\x9cz\xa7\xdf$\xe6\x99\xba\xe8\x83\xbd\xe9\x81\xa5\xe6\x8e\xa7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00',
    b'Z\xa5\xaaUZ\xa5\xaaU\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\xda\x00\x00*\'\xe9\x03\xb6\xb5\xf8\x9cz\xa7\xdf$\x00\x00\x00\x00\xe0\xc7\x00\x00\xee\x97g\x82\xf2\xfeEu>\xbf\x03K\x0e/\xe1e\x0c\x963\x03\xb6e\xdc\xff\x84r\xc4\xe44W\x8b"',
    b"Z\xa5\xaaUZ\xa5\xaaU\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xd3\xfb\xff*'\xee\x03\xb7\xb5\xf8\x9cz\xa7\xdf$\x01\x00\x00\x00\xaf\xbe\x00\x00\xc2a\x10qT%\xaf\x8eW\x80DU)\x19\xeb\xee",
    b"Z\xa5\xaaUZ\xa5\xaaU\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\xd3\xfb\xff*'\xee\x03\xb8\xb5\xf8\x9cz\xa7\xdf$\x01\x00\x00\x00\xaf\xbe\x00\x00\xc2a\x10qT%\xaf\x8eW\x80DU)\x19\xeb\xee"
]
packets = [PacketFactory.from_bytes(packet) for packet in packets]

# Decrypt packets using default key.
decryptor = PacketDecryptor(DEFAULT_KEY, DEFAULT_IV)
decryptor.decrypt(packets)

# Create 'example1' folder.
try:
    os.makedirs('example1')
except OSError as error:
    if error.errno != errno.EEXIST:
        raise

# Print packets to a file.
printer = PacketPrinter()
with open('example1/packets.txt', 'w+') as file:
    for packet in packets:
        printer.print(packet, file=file)

# Store packets into binary files.
dest_folder = 'example1/bin'
PersistenceHandler.store_packets(packets, dest_folder)
