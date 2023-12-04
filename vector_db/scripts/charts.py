import pandas as pd
import importlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df = pd.read_csv('/home/user/projects/arxiv_abs_Nov_2023.csv')


my_pie = df[df._year > 2013].groupby(['_year'])['_title'].count()
plt.clf()
plot = my_pie.plot(kind='pie', figsize=(10, 10))
plt.savefig('all_years.png')
#print(df.groupby(df._year)._title.count())
# b = df[df._year == 2019].groupby([df._year, df._month])._title.count()
current_year = {}
current_month = []
for i in range(2018, 2024):
    for j in month_list:
        work_year = df[df._year == i]
        work_month = work_year[work_year._month == j]
        result = work_month._year.count()
        current_month.append(result)
    current_year[i] = current_month
    current_month = []

for i in range(2018, 2024):
    plt.clf()
    plt.bar(month_list, current_year[i])
    plt.savefig(f'figure_{i}.png')

    # k.append(plot)
# my_bar = df[df._year == i].groupby([df._month])._title.count()
# plot = my_bar.plot(kind='bar', figsize=(10,10))
# plt.savefig('123.png')



# test = ['Apr', 'Aug', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep']
# print('list')
# print(sorted(test, key=lambda x: month_list.index(x)))
# print('dict')
# print(sorted(test, key=lambda x: month[x]))


# test = df[df._year == '1993'].sort_values(by=df._month, key=lambda x: month[x])
# print(test)
