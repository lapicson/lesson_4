#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.



from sys import argv
script_name, work_hours, pay_per_hour, award = argv

print('Имя скрипта:', script_name)
print('Оплата сотрудника:', int(work_hours)*int(pay_per_hour)+int(award))