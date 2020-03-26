import sqlite3
import matplotlib.pyplot as plt  

conn = sqlite3.connect('data.db')
cur = conn.cursor()

salary = []
select_query = 'SELECT salary FROM vacancys'
for sal in cur.execute(select_query):
    salary.append(sal[0])

avg = (sum(salary) / len(salary))

d = 0
for s in salary:
    d += (s - avg)**2
d = d /len(salary)
print('Average: ', avg)
print('Dispertion: ', d)
print('Sigma: ', d**0.5)

print('FORK PYTHON DEV')
print('MAX IS ', avg + d**0.5)
print('MIN IS ', avg - d**0.5)

plt.hist(salary, bins= 50, density=0.1, color ='r')
plt.grid(True)
plt.xlabel('Salary, rub.')
plt.ylabel('Vacancy')
plt.title('Python developer salary distribution')
plt.savefig('salary.png')
plt.show()
