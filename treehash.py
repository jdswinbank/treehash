#!/usr/bin/env python

import sys
import hashlib

class TreeHash(object):
    def __init__(self, filename, algo=hashlib.sha256, bsize=1024*1024):
        self.filename = filename
        self.algo = algo
        self.bsize = bsize

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

        hashes = []
        with open(self.filename, 'rb') as my_file:
            while True:
                block = my_file.read(self.bsize)
                if not block:
                    break
                hashes.append(self.algo(block))

        return recursive_hash(hashes)

    def get_digest(self):
        return self._compute_hash().digest()

    def get_hexdigest(self):
        return self._compute_hash().hexdigest()

if __name__ == "__main__":
    for fname in sys.argv[1:]:
        print "%s: %s" % (fname, TreeHash(fname).get_hexdigest())
