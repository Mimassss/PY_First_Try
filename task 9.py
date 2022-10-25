salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
salary_sum = 0
spend_sum = 0
# TODO Оформить решение
for i in range (months):
    salary_sum += salary
    spend_sum += spend
    spend *= 1 + increase
    need_money = spend_sum - salary_sum
    print(round(need_money))
