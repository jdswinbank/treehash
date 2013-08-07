import sys
import hashlib
from io import BytesIO

MEGABYTE=1024**2

class TreeHash(object):
    def __init__(self, data=b"", algo=hashlib.sha256, block_size=MEGABYTE):
        self.algo = algo
        self.block_size = block_size
        self.pending = BytesIO()
        self.hashes = []
        self.update(data)

    def _compute_hash(self):
        def recursive_hash(hashlist):
            output = []
            for h1, h2 in zip(hashlist[::2], hashlist[1::2]):
                output.append(self.algo(h1.digest() + h2.digest()))
            if len(hashlist) % 2:
                output.append(hashlist[-1])
            if len(output) > 1:
                return recursive_hash(output)
            else:
                return output[0]

        to_recurse = self.hashes[:]
        self.pending.seek(0)
        extra = self.pending.read()
        if extra:
            to_recurse.append(self.algo(extra))
        return recursive_hash(to_recurse)

    def update(self, data):
        self.pending.write(data)
        self.pending.seek(0)
        new_buffer = BytesIO()
        while True:
            block = self.pending.read(self.block_size)
            if len(block) == self.block_size:
                self.hashes.append(self.algo(block))
            else:
                new_buffer.write(block)
                break
        self.pending = new_buffer

    def digest(self):
        return self._compute_hash().digest()

    def hexdigest(self):
        return self._compute_hash().hexdigest()
