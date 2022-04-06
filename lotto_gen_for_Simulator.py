import random

# ロト6の番号を出す関数設定
def gen_lotto(my_lottos):
    lotto = set()
    while len(lotto) < 6:
        lotto.add(random.randrange(1, 44))
    lotto = list(lotto)
    lotto.sort()
    print(lotto)
    my_lottos.append(lotto)
    return my_lottos