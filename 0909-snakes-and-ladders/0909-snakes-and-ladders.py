class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        min_rolls = [-1] * (n * n + 1)
        q = deque()

        min_rolls[1] = 0
        q.append(1)

        while q :
            cur = q.popleft()

            for dice in range(1, 7) :
                sum = cur + dice

                if sum > n * n :
                    break

                r = (sum - 1) // n
                c = (sum - 1) % n

                row = n - 1 - r
                col = (n - 1 - c) if (r % 2 == 1) else c
                next = board[row][col] if board[row][col] > 0 else sum

                if next == n * n :
                    return min_rolls[cur] + 1
                
                if min_rolls[next] == -1 :
                    min_rolls[next] = min_rolls[cur] + 1
                    q.append(next)

        return -1

