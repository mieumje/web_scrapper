from indeed import get_jobs as get_ineed_jobs
from so import get_jobs as get_so_jobs

indeed_jobs = get_ineed_jobs()
so_jobs = get_so_jobs()

jobs = so_jobs + indeed_jobs

print(jobs)
