import models

if __name__ == '__main__':
    recruiter_aleks = models.Recruiter('Aleks', 'aleks@gmail.com', 50)
    programmer_semen = models.Programmer('Semen', 'semen@gmail.com', 70, 'java', 'js', 'python')
    programmer_kris = models.Programmer('Kris', 'kriss@gmail.com', 60, 'html', 'css', 'js')
    candidate_ivan = models.Candidate('Ivan', 'ivan@gmail.com', 'python', 'senior', 'python', 'php', 'js', 'ruby')
    candidate_dmytro = models.Candidate('Dmytro', 'dmytro@gmail.com', 'python', 'junior', 'python', 'js')
    candidate_artem = models.Candidate('Artem', 'artem@gmail.com', 'java', 'middle', 'java', 'js', 'c++')
    vacancy_python_dev = models.Vacancy('python developer', 'python', 'senior')
    vacancy_java_dev = models.Vacancy('java developer', 'java', 'junior')

print(candidate_artem)