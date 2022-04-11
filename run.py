import os, sys, shutil
from src import loz as x


try: shutil.rmtree('data/__pycache__')
except: pass
try: shutil.rmtree('src/__pycache__')
except: pass

for filename in os.listdir('data'):
	if filename[-3:] == 'pyc':
		try: os.remove('data/'+filename)
		except: pass

for filename in os.listdir('src'):
	if filename[-3:] == 'pyc':
		try: os.remove('src/'+filename)
		except: pass

wkwkskkkwwk = x.moch_yayan()
wkwkskkkwwk.start()
