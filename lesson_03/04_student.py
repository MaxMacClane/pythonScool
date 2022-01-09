# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей
quantity_months = int(input('Inter quantity months: '))
inflation = 3
money_from_parents = 0
educational_grant, expenses = 10000, 12000

# for _ in range(quantity_months): 'if use loop
while quantity_months > 0:
    money_from_parents += expenses - educational_grant
    expenses += (expenses * inflation) / 100
    quantity_months -= 1
print('For colledg living', quantity_months, 'need to ask your perents', money_from_parents.__round__(2))




