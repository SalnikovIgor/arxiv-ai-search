import pandas as pd
import importlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# pdf = PdfPages('Figures.pdf')

df = pd.read_csv('/home/user/projects/arxiv-ai-search/arxiv_abs_Nov_2023.csv')

# for col in df.columns:
#     print(col)

# print(df.head())
# my_pie = df.groupby(['_year'])['_title'].count()
#print(df._year.value_counts())
# plot = my_pie.plot(kind='pie', figsize=(10, 10))
# pdf.savefig()
#print(df.groupby(df._year)._title.count())

# b = df[df._year == 2019].sort_values(by=df._month, key=lambda x: month_list.index(x)).groupby([df._year, df._month])._title.count()
# print(b)
# k = []
# for i in range(2018, 2024):
#     print(i)
#     my_bar = df[df._year == i].groupby([df._month])._title.count()
#     plot = my_bar.plot(kind='bar', figsize=(10,10))
#     # k.append(plot)
#     plt.savefig('123.png')



test = ['Apr', 'Aug', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep']
print('list')
print(sorted(test, key=lambda x: month_list.index(x)))
print('dict')
print(sorted(test, key=lambda x: month[x]))


test = df[df._year == '1993'].sort_values(by=df._month, key=lambda x: month[x])
print(test)
