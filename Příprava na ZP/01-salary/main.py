import sys
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    # // TODO  Class Person
    gender: str
    first_name: str
    last_name: str
    city: str
    age: int
    blood_type: str
    weight: float
    salary: float

    def __str__(self) -> str:
        return f"{self.gender} {self.first_name} {self.last_name} {self.city} {self.age} {self.blood_type} {self.weight} {self.salary}"


def load_data_file(filepath: str, wanted_year: Optional[int] = None):
    # id;pohlaví;jméno;přijmení;adresa;město;stát;narození;věk;krevní skupina;váha;výška;ROK;odvětví;RRŮMĚRNÝ PLAT
    # 0 ;1      ;2    ;3       ;4     ;5    ;6   ;7       ;8  ;9            ;10  ;11   ;12 ;13     ;14
    # len(fields) = 15

    # funkce načte data a vrátí:
    # // TODO pohlaví
    # // TODO jméno
    # // TODO příjmení
    # // TODO město
    # // TODO věk
    # // TODO krevní skupina
    # // TODO váha
    # // TODO průměrný plat
    students = []
    with open(filepath, "r", encoding="utf8") as file:
        file.readline()
        for line in file:
            line = line.replace("\n", "")
            fields = line.split(";")

            if len(fields) != 15:
                print("The line doesn't contain valid data")
                continue

            if not fields[12].isnumeric():
                print("Line doesn't contain valid year")
                continue

            sal = fields[14].replace(".", "")
            if not sal.isnumeric():
                print("Line doesn't contain valid salary")
                continue

            # c = fields[5].replace(" ", "")
            # if not c.lower().isalpha():
            #    print(f"Line doesn't contain valid city {fields[5]}")
            #    continue

            match fields[9]:
                case "O+" | "O-" | "o+" | "o-" | "0+" | "0-" | "A+" | "A-" | "B+" | "B-" | "AB+" | "AB-":
                    pass

                case _:
                    print(f"unknown blood type {fields[9]}")

            match fields[1].lower():
                case "žena":
                    pass
                case "muž":
                    pass
                case _:
                    print(f"Unknown gender: {fields[1]}")

            if not fields[8].isnumeric():
                print("Line doesn't contain valid age")
                continue

            w = fields[10].replace(".", "")
            if not w.isnumeric():
                print("Line doesn't contain valid weight")
                continue

            if wanted_year is None:
                students.append(Person(fields[1], fields[2], fields[3], fields[5], int(fields[8]), fields[9], float(fields[10]), float(fields[14])))
            if int(fields[12]) == wanted_year:
                students.append(Person(fields[1], fields[2], fields[3], fields[5], int(fields[8]), fields[9], float(fields[10]), float(fields[14])))

    return students


def count_average_salary(data: list[Person]):
    average = 0.0

    for p in data:
        average += p.salary

    return (average / len(data))


def count_median_salary(data: list[Person]):

    data.sort(key=lambda x: x.salary)

    if len(data) % 2 == 0:
        median = (data[len(data)//2 - 1].salary +
                  data[len(data)//2 + 1].salary) / 2
        return median
    return (data[len(data)//2].salary)


def blood(data: list[Person], city, blood_type) -> int:

    return 0


def count_average_weight(data: list[Person], year, city) -> float:

    sum = 0.0
    count = 0

    for p in data:
        if p.year == year and p.city == city:
            sum +=


def main(input_path: str):

    # print(count_average_salary(load_data_file(input_path)))
    # data14 = count_average_salary(load_data_file(input_path, 2014))
    # data15 = count_average_salary(load_data_file(input_path, 2015))
    # print(data14, data15)

    while True:
        try:
            year = int(input("Enter year: "))
            data = load_data_file(input_path, year)
            if len(data) == 0:
                print("No data found for given year")
                continue
            break
        except ValueError:
            print("Year must be a number")

    avg = count_average_salary(data)
    print(f"Průměrný plat v roce {year}  je  {avg}")

    median = count_median_salary(data)
    print(f"Medián v roce {year}  je  {median}")


if __name__ == '__main__':
    data_path = None

    if len(sys.argv) == 2:
        if not os.path.exists(sys.argv[1]):
            print("file doesn't exist")
            exit(1)
        data_path = sys.argv[1]

    elif len(sys.argv) == 1:
        print("Input doesn't  provided path to the file")
        exit(2)
    else:
        print("err")
        exit(1)

    main(data_path)
