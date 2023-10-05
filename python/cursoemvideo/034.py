"""Reads input and outputs new salary value."""
salary = float(input("Qual é o salário do funcionário? R$ "))

if salary > 1250:
    new = (salary * 0.10) + salary
else:
    new = (salary * 0.15) + salary

print("Quem ganhava R$ {:.2f} passará a ganhar R$ {:.2f} agora.".format(salary, new))
