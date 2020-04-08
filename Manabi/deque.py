'''
Deque とは、スタックとキューを一般化したものです (この名前は「デック」と発音され、
これは「double-ended queue」の省略形です)。Deque はどちらの側からも append と
pop が可能で、スレッドセーフでメモリ効率がよく、どちらの方向からもおよそ O(1) の
パフォーマンスで実行できます。
list オブジェクトでも同様の操作を実現できますが、これは高速な固定長の操作に
特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や
insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします。
'''

# Listの場合
from collections import deque
import time

start = time.time()
list_array = list(range(100000))
for i in range(1000):
    list_array.pop(0)
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# dequeの場合
start = time.time()
deque_array = deque(range(100000))
for i in range(1000):
    deque_array.popleft()
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
