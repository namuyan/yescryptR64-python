# yescryptR64-python
yescryptR64 hesh generator for python.  
Yenten's alog is yescryptR64.

## compile
```commandline
git clone git+https://github.com/namuyan/yescryptR64-python.git
python setup.py build
python setup.py install
```
[For windows binary](https://github.com/namuyan/yescryptR64-python/releases/tag/1.0)

## check
```python
from binascii import hexlify, unhexlify
import yescryptr64
hash = b'2c581115e604b6027dfaf960c66943616588a5b328c92364e6aa49922a5fd75f'
header = b'0100000000000000000000000000000000000000000000000000000000000000000000002a67f93c'
header += b'1e533f3d383eda5c359496f703ee33f735732adeed2ca121724e8792687dd359ffff3f1e68930200'
header = unhexlify(yenten_height0_header)
create_hash = hexlify(yescryptr64.getPoWHash(header))
print('OK!' if create_hash == hash else 'NO..')
```

## author
[namuyan](http://twitter.com/namuyan_mine/)

## License
MIT
