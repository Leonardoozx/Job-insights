from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    all_jobs = read(path)
    all_salaries = []
    for job in all_jobs:
        try:
            all_salaries.append(int(job["max_salary"]))
        except ValueError:
            all_salaries.sort()

    return max(all_salaries)


def get_min_salary(path: str) -> int:
    all_jobs = read(path)
    all_salaries = []
    for job in all_jobs:
        try:
            all_salaries.append(int(job["min_salary"]))
        except ValueError:
            all_salaries.sort()

    return min(all_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        if min_salary > max_salary:
            raise ValueError
        return min_salary <= int(salary) <= max_salary
    except Exception:
        raise ValueError
        print('leonardo')


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    all_jobs_filtered_by_salary = []
    try:
        for job in jobs:
            max_salary = int(job["max_salary"])
            min_salary = int(job["min_salary"])
            if min_salary <= int(salary) <= max_salary:
                all_jobs_filtered_by_salary.append(job)
    except Exception:
        all_jobs_filtered_by_salary.sort()
    return all_jobs_filtered_by_salary
