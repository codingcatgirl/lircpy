# lircpy
accessing the LIRC socket interface using Python 3

## Example usage
```python
from lircpy import LircPy
lirc = LircPy()
lirc.send_once('logi', 'KEY_POWER')
```

For more details, execute `pydoc lircpy.LircPy`.
