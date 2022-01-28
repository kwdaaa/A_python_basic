# 関数「random」を読み込む
import random


# 関数「daice()」を作成
def dice():
    # 変数「number」に リスト[1, 2, 3, 4, 5, 6]を定義。
    number = [1, 2, 3, 4, 5, 6]
    # 変数「result」に変数「number」から「random.choice」によってランダムで選ばれた値を定義。
    result = random.choice(number)
    # 変数「result」に入った値を戻り値として定義。
    return result


# 関数「daice()」を出力。
print(dice())
