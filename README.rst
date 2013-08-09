Tree Hash Calculator
====================

Calculates a SHA256 (or, potentially, any other ``hashlib`` supported function)
"tree" hash, as used by e.g. `Amazon Glacier
<http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`_.

Command line usage::

  $ treehash <filename> ...

As a library, we follow the ``hashlib`` conventions. That is::

  >>> from treehash import TreeHash
  >>> treehash = TreeHash()
  >>> treehash.update(b"Nobody inspects")
  >>> treehash.update(b" the spammish repetition")
  >>> treehash.digest()
  '\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
  >>> treehash.hexdigest()
  '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

Note that it is possible to specify the block size (Glacier uses 1 MB) and
hash algorithm used::

  >>> treehash = TreeHash(algo=hashlib.md5, block_size=2048*2048)
