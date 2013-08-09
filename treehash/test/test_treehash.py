import unittest
import hashlib
from treehash import TreeHash

TEST_DATA = b"a"

class TreeHashTestCase(unittest.TestCase):
    def test_constructor(self):
        self.assertEqual(
            hashlib.sha256(TEST_DATA).hexdigest(),
            TreeHash(TEST_DATA).hexdigest()
        )

    def test_update(self):
        treehash = TreeHash()
        treehash.update(TEST_DATA)
        self.assertEqual(
            hashlib.sha256(TEST_DATA).hexdigest(),
            treehash.hexdigest()
        )

    def test_md5(self):
        self.assertEqual(
            hashlib.md5(TEST_DATA).hexdigest(),
            TreeHash(TEST_DATA, algo=hashlib.md5).hexdigest()
        )

    def test_digest(self):
        self.assertEqual(
            hashlib.md5(TEST_DATA).digest(),
            TreeHash(TEST_DATA, algo=hashlib.md5).digest()
        )

    def test_tree(self):
        hashlib_result = hashlib.sha256(
            hashlib.sha256(TEST_DATA).digest() +
            hashlib.sha256(TEST_DATA).digest()
        ).hexdigest()
        self.assertEqual(hashlib_result,
            TreeHash(2*TEST_DATA, block_size=1).hexdigest()
        )
