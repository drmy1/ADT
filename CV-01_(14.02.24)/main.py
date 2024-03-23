import sys
import os
from typing import Final, Optional
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    surname: str
    birth_date: str
    salary: float


def load_data_file(file_path: str, wanted_year: Optional[int] = None, limit: Optional[int] = None):
    students = []
    with open(file_path, encoding="utf8") as file_desc:
        file_desc.readline()
        for line_num, line in enumerate(file_desc):
            line = line.strip()
            fields = line.split(";")
            _, _, name, surname, _, _, _, _, _, _, _, _, birth_year, _, salary = fields
            if len(fields) != 15:
                print(f"invalid line: {line}")
                continue
            if wanted_year is None or birth_year == wanted_year:
                students.append(
                    Person(name, surname, birth_year, float(salary)))
    return students


def count_average_salary(data: list[Person]):
    return 0


def count_median_salary(data: list[Person]):
    return 0


def main(input_path: str):
    YEAR: Final[int | None] = None
    LIMIT: Final[int] = 1000
    data = load_data_file(input_path, YEAR, LIMIT)
    avg = count_average_salary(data)
    print(f"Průměrný plat v roce {YEAR}  je  {avg}")

    median = count_median_salary(data)
    print(f"Medián v roce {YEAR}  je  {median}")


if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) < 2:
        print("Give me my file path!")
        exit(1)

    data_file_path = arguments[1]
    if not os.path.exists(data_file_path):
        print("Give me my file path!")
        exit(2)
    main(data_file_path)
