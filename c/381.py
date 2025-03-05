"""
<方針>
- 番兵として右側に `1` を置いておく．
- 左側から見る．
- `1` がどれだけ連続するかを記録する．
- `/` が出てきたら `2` の数を数える．
- 条件分岐を頑張って実装する．ソースコードは `†WYSIWYG†` です．
"""
# 入力
N = int(input())
S = list(input())

# 番兵
S.append("1")

ans = -1 # 答え
look = 1 # 現在何をカウントアップしているか．最初は1
one = 0 # 1の現在のカウント数
two = 0 # 2の現在のカウント数
# 文字を順番に見ていく．
for s in S:
  match look:
    case 1:
      match s:
        case "1":
          one += 1
          two = 0
          look = 1
        case "/":
          two = 0
          look = 2
        case "2":
          one = 0
          two = 0
          look = 1
    case 2:
      match s:
        case "1":
          ans = max(ans, min(one, two)*2 + 1) # 答えを更新
          one = 1
          two = 0
          look = 1
        case "/":
          ans = max(ans, min(one, two)*2 + 1) # 答えを更新
          one = 0
          two = 0
          look = 1
        case "2":
          two += 1
          look = 2
# 出力
print(ans)

# # def is_11_22_bracket(S: str,N:int) -> str:
    
# #     # Check if the length of S is odd
# #     if N % 2 == 0:
# #         return "No"
    
# #     mid = N // 2
    
# #     # Check if the first half (excluding the middle) is all '1's
# #     if not all(c == '1' for c in S[:mid]):
# #         return "No"
    
# #     # Check if the middle character is '/'
# #     if S[mid] != '/':
# #         return "No"
    
# #     # Check if the second half (excluding the middle) is all '2's
# #     if not all(c == '2' for c in S[mid+1:]):
# #         return "No"
    
# #     return "Yes"
# def is_11_22_bracket(S: str) -> bool:
#     n = len(S)
    
#     # 奇数長でない場合は除外
#     if n % 2 == 0:
#         return False

#     mid = n // 2

#     # 条件を効率的にチェック
#     return S[mid] == '/' and S[:mid] == '1' * mid and S[mid+1:] == '2' * mid


# def longest_11_22_substring(S: str) -> int:
#     n = len(S)
#     max_length = 0
    
#     # 部分文字列の開始位置を固定し、長さが奇数のものだけを試す
#     for length in range(1, n + 1, 2):  # 奇数長のみ
#         for start in range(n - length + 1):
#             if is_11_22_bracket(S[start:start+length]):
#                 max_length = max(max_length, length)

#     return max_length
# # Read input
# N = int(input())
# S = input()

# # Determine if S is an "11/22" string and print the result
# print(longest_11_22_substring(S))