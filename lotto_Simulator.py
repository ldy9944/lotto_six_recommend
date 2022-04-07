from operator import index
import lotto_gen_for_Simulator
from selenium import webdriver
import time
import os

# ロット6ホームページで最近の当選番号を読み込む
url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

time.sleep(1)

raw_win_num = driver.find_elements_by_class_name('js-lottery-number-pc')
win_num = list()

for i in raw_win_num:
    i = i.text
    i = int(i)
    win_num.append(i)

bonus = driver.find_element_by_class_name('js-lottery-bonus-pc').text
bonus = bonus.replace('(', '')
bonus = bonus.replace(')', '')
bonus = int(bonus)

# ロット6ホームページで最近の当選金額を読み込む
first_value = 0
second_value = 0
third_value = 0
fourth_value = 0
fifth_value = 0

raw_value = driver.find_elements_by_class_name('alnRight')

for i in raw_value:
    raw_a = raw_value[raw_value.index(i)].text
    a = raw_a.replace('円', '')
    a = a.replace(',', '')
    
    if i == raw_value[1]:
        a = int(a)
        first_value = a
    elif i == raw_value[3]:
        a = int(a)
        second_value = a
    elif i == raw_value[5]:
        a = int(a)
        third_value = a
    elif i == raw_value[7]:
        a = int(a)
        fourth_value = a
    elif i == raw_value[9]:
        a = int(a)
        fifth_value = a

driver.quit()

os.system('cls')

# 初期画面出力
print('<ロト６シミュレーター！>')
print('---------------------')
print('当選番号：{0}'.format(win_num))
print('ボーナス番号：[{0}]'.format(bonus))
print('---------------------')
print()
print('---------------------')
print('1等 : {0}円'.format(format(first_value, ',')))
print('2等 : {0}円'.format(format(second_value, ',')))
print('3等 : {0}円'.format(format(third_value, ',')))
print('4等 :{0}円'.format(format(fourth_value, ',')))
print('5等 :{0}円'.format(format(fifth_value, ',')))
print('---------------------')

# 実行回数入力　間違えるとプログラムを終了
try:
    max_cnt = int(input('実行回数を数字のみで入力してください。\n'))
    if max_cnt <= 0:
        raise ValueError
except ValueError:
    print('正しい数字を入力してください')
    input('Enterを押すとプログラムを終了致します。')
    exit()

# 発行番号、当選番号の変数指定
# 合計購入金額を計算
total_cost = 200 * max_cnt
my_lottos = list()
my_index = list()

# 番号発行
for i in range(1, max_cnt + 1):
    print('{0}行 :'.format(i), end=' ')
    lotto_gen_for_Simulator.gen_lotto(my_lottos)
    my_index.append(f'{i}行：')

# 発行された番号の中で何等がいくつか計算
first = 0
second = 0
third = 0
fourth = 0
fifth = 0

my_first = list()
my_second = list()
my_third = list()
my_fourth = list()
my_fifth = list()

for i in my_lottos:
    i = set(i)
    win_num = set(win_num)

    if i == win_num:
        first += 1
        i = list(i)
        i.sort()
        print('1等 :', i)
        my_first.append(f'1等 : {i}')

    elif len(i & win_num) == 5 and bonus in i:
        second += 1
        i = list(i)
        i.sort()
        print('2等 :', i)
        my_second.append(f'2等 : {i}')

    elif len(i & win_num) == 5:
        third += 1
        i = list(i)
        i.sort()
        print('3等 :', i)
        my_third.append(f'3等 : {i}')

    elif len(i & win_num) == 4:
        fourth += 1
        i = list(i)
        i.sort()
        print('4等 :', i)
        my_fourth.append(f'4等 : {i}')

    elif len(i & win_num) == 3:
        fifth += 1
        i = list(i)
        i.sort()
        print('5等 :', i)
        my_fifth.append(f'5等 : {i}')
    else:
        pass

win_num = list(win_num)
win_num.sort()

# 合計当選金額を計算
total_win_value = (first * first_value) + (second * second_value) + (third * third_value) + (fourth * fourth_value) + (fifth * fifth_value)

# 結果を出力
print('<結果発表！>')

print('当選番号：{0}'.format(win_num))

print('ボーナス番号：[{0}]'.format(bonus))

print()

print('1等 : {0}口'.format(first))
print('2等 : {0}口'.format(second))
print('3等 : {0}口'.format(third))
print('4等 :{0}口'.format(fourth))
print('5等 :{0}口'.format(fifth))
print('---------------------')
print('合計購入額：{0}円'.format(format(total_cost, ',')))
print('合計当選金額：{0}円'.format(format(total_win_value, ',')))

if total_cost < total_win_value:
    print('お得ですね！おめでとうございます！')
elif total_cost == total_win_value:
    print('同率です！')
else:
    print('損しました！残念です。')

# 結果ファイルを作成
print()
file = input('結果をファイルに保存しましょうか？(Y / N)')

if file == 'Y' or file == 'y':
    f_result = open('result.txt', 'w', encoding='UTF-8', newline='')

    for i in my_lottos:
        f_result.write(f'{my_index[my_lottos.index(i)]}')
        f_result.write(f'{i}')
        f_result.write('\n')

    f_result.write('--------------------------')
    f_result.write('\n')

    for i in my_first:
        f_result.write(f'{i}')
        f_result.write('\n')

    f_result.write('--------------------------')
    f_result.write('\n')

    for i in my_second:
        f_result.write(f'{i}')
        f_result.write('\n')

    f_result.write('--------------------------')
    f_result.write('\n')

    for i in my_third:
        f_result.write(f'{i}')
        f_result.write('\n')

    f_result.write('--------------------------')
    f_result.write('\n')

    for i in my_fourth:
        f_result.write(f'{i}')
        f_result.write('\n')

    f_result.write('--------------------------')
    f_result.write('\n')

    for i in my_fifth:
        f_result.write(f'{i}')
        f_result.write('\n')

    f_result.write('--------------------------')
    f_result.write('\n')

    f_result.write('<結果発表！>')
    f_result.write('\n')
    f_result.write('当選番号：{0}'.format(win_num))
    f_result.write('\n')
    f_result.write('ボーナス番号：[{0}]'.format(bonus))

    f_result.write('\n')

    f_result.write('1等 : {0}口'.format(first))
    f_result.write('\n')
    f_result.write('2等 : {0}口'.format(second))
    f_result.write('\n')
    f_result.write('3等 : {0}口'.format(third))
    f_result.write('\n')
    f_result.write('4等 :{0}口'.format(fourth))
    f_result.write('\n')
    f_result.write('5等 :{0}口'.format(fifth))
    f_result.write('\n')
    f_result.write('---------------------')
    f_result.write('\n')
    f_result.write('合計購入額：{0}円'.format(format(total_cost, ',')))
    f_result.write('\n')
    f_result.write('合計当選金額：{0}円'.format(format(total_win_value, ',')))
    f_result.write('\n')

    if total_cost < total_win_value:
        f_result.write('お得ですね！おめでとうございます！')
    elif total_cost == total_win_value:
        f_result.write('同率です！')
    else:
        f_result.write('損しました！残念です。')

    f_result.close()
else:
    pass
