import subprocess
import pickle 
from multiprocessing import Pool
import os

processes = {}
step = 1
fork_id = os.fork
def g(i):
  processes[i] = subprocess.run(["python", "crawler.py", str(i), str(step)])
  print(" RUN ", i, " --- ", i+step)

with Pool(4) as pool:
    pool.map(g, range(6000, 6004))

pickle.dump(processes, open("proc.txt", "bw"))
