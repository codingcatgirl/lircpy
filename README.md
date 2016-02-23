# lircpy
accessing the LIRC socket interface using Python 3

## Installation

Python 3 is required.

No dependencies, just run `pip install lircpy` or clone the repository and run `python setup.py install`.

## Example usage
```python
from lircpy import LircPy
lirc = LircPy()
lirc.send_once('logi', 'KEY_POWER')
```

For more details, execute `pydoc lircpy.LircPy`.
