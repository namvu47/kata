# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# https://pyformat.info/
# https://realpython.com/python-string-formatting/

_error = 50159747054
_name = "Nam"

# Old style % operator
print('Hey %s, there is a 0x%x error!' %(_name, _error))
print ('Hey %(a)s, there is a 0x%(b)x error!' % {'a': _name, 'b':_error})
print('----------')

# New style str.format()
print('Hey {name:s}, there is a 0x{error:x} error!'.format(name= _name, error=_error))
print('----------')

#String Interpolation f-Strings
print(f'Hey{_name:s}, there is a 0x{_error:x} error!')
