# Comment
# print("Hello World!")

# print("こんにちは!")

# print("やっほー！")

# 演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%3)

# 変数
fire = 'moeru'
fire_length = 3
fire_times = 3.3

# print(type(fire))
# #ブーリアン型
# fire_moeru = False

# 条件分岐と関連演算子
# if else elif
# ==, !=, <, >, >=, <=
# if fire_length < 2:
#   print('大きい')
# elif fire_length == 3:
#   print('無い')
# else:
#   print('小さい')

# 関数
# def fire_moeru(arg):
#   fire_status = arg
#   if(fire_status < 10):
#     return 'mada daijobu'
#   else:
#     return 'yabai'

# print()

# list
# fire_list = ['fire_big', 'fire_medium', 'fire_small']
# print(fire_list[0])

# for 繰り返し文
# for index in range(11):
#   print(fire_moeru(index))

# for item in fire_list:
#   print(item)

# with
# opne()
# with open('./fire.txt', 'r') as file:
#   print(file)

# class
# class Card:
#   def __init__(self, date, user_name):
#     self.date = date
#     self.user_name = user_name
#   def message(self):
#     return 'この投稿は' + self.user_name +'さんが' + self.date + 'に投稿しました'
# date_a = '2021-01-01'
# user_name_a = 'kazu'
# card_a = Card(date_a, user_name_a)

# date_b = '2021-09-27'
# user_name_b = 'teru'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())

# import
# import math
# print(math.pi)

import numpy
numpy_list = [3, 1, 5, 10, 2093, 304, 123]
print(numpy.sum(numpy_list))
# 一例 ↓
# NumPy
# Pandas
# Flask
# Django