from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        opened_file = csv.DictReader(file)
        return list(opened_file)


def get_unique_job_types(path: str) -> List[str]:
    all_jobs = read(path)
    return list(set([job["job_type"] for job in all_jobs]))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type
