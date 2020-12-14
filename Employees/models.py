from datetime import date, timedelta


class Employee:

    def __init__(self, name, email, salary_per_day):
        self.name = name
        self.email = email
        self.salary_per_day = salary_per_day

    def work(self):
        return "I come to the office."

    def __gt__(self, other):
        return self > other

    def __lt__(self, other):
        return self < other

    def __ge__(self, other):
        return self >= other

    def __le__(self, other):
        return self <= other

    def __eq__(self, other):
        return self == other

    def salary(self, amount_of_days):
        return self.salary_per_day * amount_of_days

    def check_salary(self):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [5, 6]
        diff = (now - month_start).days + 1
        day_count = 0

        for day in range(diff):
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1

        return day_count * self.salary_per_day


class Recruiter(Employee):

    hired_this_month = set()

    def work(self):
        return super().work()[:-1] + " and start to hiring."

    def __str__(self):
        return f'Recruiter: {self.name}'


class Programmer(Employee):

    def __init__(self, name, email, salary_per_day, *tech_stack):
        super().__init__(name, email, salary_per_day)
        self.tech_stack = tech_stack
        self.closed_this_month = {}

    def work(self):
        return super().work()[:-1] + " and start to coding."

    def __str__(self):
        return f'Programmer: {self.name}'

    def __add__(self, other):
        return set(self.tech_stack + other.tech_stack)


class Candidate:

    def __init__(self, full_name, email, main_skill, main_skill_grade, *technologies):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f'Candidate: {self.full_name}'


class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.maim_skill = main_skill
        self.maim_skill_level = main_skill_level

    def __str__(self):
        return f'Vacancy: {self.title}'

