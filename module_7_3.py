import random

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = random.randrange(300, 500)
team2_time = random.randrange(300, 400)


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result

tasks_total = score_1 + score_2

time_avg = (team1_time + team2_time / (score_1 + score_2))

print("В команде Мастера кода участников: %d ! " % team1_num)
print("В команде Мастера кода участников: %d и %d ! " % (team1_num, team2_num))

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} c !".format(team1_time * score_1))

print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: победа команды {challenge_result}!")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:5.3f} секунды на задачу!")
