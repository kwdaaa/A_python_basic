# "Bob", "Tom", "Ken" という 3つの要素をもつ変数「members」というリストを定義。
members = ["Bob", "Tom", "Ken"]

# 変数「members」のインデント番号「0」の中身を出力。
print(members[0])

# 変数「members」のインデント番号「1」の中身を出力。
print(members[1])

print(members[:2])

# 内包表記
print('\n'.join(member for member in members if member == 'Bob' or member == 'Ken'))
