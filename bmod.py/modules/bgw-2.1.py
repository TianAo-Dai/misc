import os
from sandbox import SandBox, get_mod_name


s = SandBox()
home = os.environ["HOME"]

s.set_mod(mod_name=get_mod_name())
s.set_mod("pkg", home+"/soft/dft/bgw-2.1")
s.reset("OMP_NUM_THREADS", 1)

s.echo_commands()