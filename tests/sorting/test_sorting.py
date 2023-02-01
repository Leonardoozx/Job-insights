from src.pre_built.sorting import sort_by
import pytest

mock = [
    {
        "job_title": "1",
        "min_salary": "1",
        "max_salary": "4",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "2",
        "min_salary": "2",
        "max_salary": "5",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "3",
        "min_salary": "3",
        "max_salary": "6",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-06",
    },
]
criteria_min_salary_mock = [
    {
        "job_title": "1",
        "min_salary": "1",
        "max_salary": "4",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "2",
        "min_salary": "2",
        "max_salary": "5",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "3",
        "min_salary": "3",
        "max_salary": "6",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-06",
    },
]
criteria_max_salary_mock = [
    {
        "job_title": "3",
        "min_salary": "3",
        "max_salary": "6",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "2",
        "min_salary": "2",
        "max_salary": "5",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "1",
        "min_salary": "1",
        "max_salary": "4",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-06",
    },
]
criteria_date_posted_mock = [
    {
        "job_title": "1",
        "min_salary": "1",
        "max_salary": "4",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "3",
        "min_salary": "3",
        "max_salary": "6",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-06",
    },
    {
        "job_title": "2",
        "min_salary": "2",
        "max_salary": "5",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-06",
    },
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == criteria_min_salary_mock
    sort_by(mock, "max_salary")
    assert mock == criteria_max_salary_mock
    sort_by(mock, "date_posted")
    assert mock == criteria_date_posted_mock
    with pytest.raises(ValueError):
        sort_by(mock, "xx")
