from read_options import read_options
from batch_management import *
import datetime
import time

options = read_options('options.yml')
job = BatchScript.from_dict( options = options )
job.duration = 36000
job.ncores = 64
job.nnodes = 4
job.create()
job.submit_job()
print job.job_id
print job.is_submitted()
while not job.is_running():
    print( 'Job waiting' )
    time.sleep(5)
else:
    time.sleep(60)
    print( 'Job Running. Cancel')
    job.cancel()
print job.cancelled
print job.is_submitted()

