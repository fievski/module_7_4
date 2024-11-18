team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
# 1. Переменные: количество участников первой команды
team1_message = "В команде Мастера кода участников: %d !" % team1_num
print(team1_message)

# 2. Переменные: количество участников в обеих командах
teams_message = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_message)

# Использование format()
# 3. Переменные: количество задач решённых командой 2
score_2_message = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score_2_message)

# 4. Переменные: время за которое команда 2 решила задачи
team2_time_message = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(team2_time_message)

# Использование f-строк
# 5. Переменные: количество решённых задач по командам
scores_message = f"Команды решили {score_1} и {score_2} задач."
print(scores_message)

# 6. Переменные: исход соревнования
result_message = f"Результат битвы: {challenge_result}!"
print(result_message)

# 7. Переменные: количество задач и среднее время решения
tasks_message = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(tasks_message)


# print('Привет,' + ' мир!')
# print('Меня зовут %(name)s, мне %(year)s' % {'name': 'Сэм', 'year': 14})
# print('Я учусь в {}{}'.format('Урбан', '-university'))
# print(f'{"Urban" * 2} это лучший универ')