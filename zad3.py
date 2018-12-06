import os, os.path
fld = '/dev'
fil = len([f for f in os.listdir(fld) if os.path.isfile(os.path.join(fld, f))])
print(fil)