# conver any input number to time format 'hh:mm:ss'
# not exceed 99:59:59

def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60
    return '{:02d}'.format(h) + ':' + '{:02d}'.format(m) + ':' + '{:02d}'.format(s)



