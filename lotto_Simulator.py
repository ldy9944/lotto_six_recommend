import lotto_gen_for_Simulator

time = int(input('実行回数を数字のみで入力してください。\n'))
my_lottos = list()
win_num = [11, 20, 26, 31, 34, 38]
bonus = 32

for i in range(1, time + 1):
    print('{0}行 :'.format(i), end=' ')
    lotto_gen_for_Simulator.gen_lotto(my_lottos)

first = 0
second = 0
third = 0
fourth = 0
fifth = 0

for i in my_lottos:
    i = set(i)
    win_num = set(win_num)

    if i == win_num:
        first += 1
        i = list(i)
        i.sort()
        print('1等 :', i)
    elif len(i & win_num) == 5 and bonus in i:
        second += 1
        i = list(i)
        i.sort()
        print('2等 :', i)
    elif len(i & win_num) == 5:
        third += 1
        i = list(i)
        i.sort()
        print('3等 :', i)
    elif len(i & win_num) == 4:
        fourth += 1
        i = list(i)
        i.sort()
        print('4等 :', i)
    elif len(i & win_num) == 3:
        fifth += 1
        i = list(i)
        i.sort()
        print('5等 :', i)
    else:
        pass

print('1等 :', first)
print('2等 :', second)
print('3等 :', third)
print('4等 :', fourth)
print('5等 :', fifth)