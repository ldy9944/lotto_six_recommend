import random

# ロト6の番号を出す関数設定
def gen_lotto():
    lotto = set()
    while len(lotto) < 6:
        lotto.add(random.randrange(1, 44))
    lotto = list(lotto)
    lotto.sort()
    print(lotto)

# 上記の関数を繰り返す回数を入力
time = int(input('実行回数を数字のみで入力してください。'))

# 入力値に従い関数を繰り返して結果を出す。
for i in range(1, time + 1):
    print('{0}行 :'.format(i), end=' ')
    gen_lotto()
