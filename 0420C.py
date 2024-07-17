def bubble_sort(arr):
    n = len(arr)
    swap_count = 0  # 入れ替え回数をカウントする変数
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
                # 入れ替えとそれぞれの要素番号を表示
                print(f"{j} {j+1}", arr)
    return swap_count, arr

# 入力を受け取る
N = int(input())  # 出令の数
orders = []  # 出令のリスト
for _ in range(N):
    order = list(map(int, input().split()))
    orders.append(order)

# バブルソートを実行し、入れ替え回数とソート後の出令リストを取得
swap_count, sorted_orders = bubble_sort(orders)

# ソートした回数を出力
print( swap_count)

# ソート後の出令リストを出力
for order in sorted_orders:
    print(*order)