# # with open('./weather_data.csv', 'r') as file:
# #     data = file.readlines()
#
# # import csv
#
#
# # with open('./weather_data.csv', 'r') as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] == 'temp':
# #             continue
# #         temperatures.append(int(row[1]))
# #     print(temperatures)
#
import pandas
my_data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(my_data[my_data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(my_data[my_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(my_data[my_data['Primary Fur Color'] == 'Black'])
print(gray_squirrels_count)


data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
#
# # data = pandas.read_csv('./weather_data.csv')
# # data_dict = data.to_dict()
#
#
# # print(data['temp'].mean())
# # print(data['temp'].max())
# #
# # # Get data from columns
# # print(data['condition'])
# # print(data.condition)
#
# # Get data from row
# # print(data[data.day == 'Monday'])
# # print(data[data.temp == data.temp.max()])
#
# # Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_data.csv')
#
#
