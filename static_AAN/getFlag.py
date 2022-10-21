import os
import stat
import subprocess as sp
os.chmod('static', stat.S_IRWXU)
p = sp.Popen(['strings', '-d', '-t', 'x', 'static'], stdout=sp.PIPE )
b = sp.run(['grep','pico.*'], stdin=p.stdout)
