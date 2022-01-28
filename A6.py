# 1, 3, 5, 7, 9 という5つの要素をもつ変数「odd_numbers」というリストを定義。
odd_numbers = [1, 3, 5, 7, 9]

# 変数「odd_numbers」の中身を順番に取り出して、中身を変数「number」に定義。
for number in odd_numbers:
    # 変数「number」を出力。
    print(number)

# 変数「number」はどんどん上書きされるので、forで繰り返しが終わったら、変数「number」には一番最後の要素「9」が残る。
print(number)
