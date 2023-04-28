def dfs(n, m):
    s = []

    def generate_combinations():
        if len(s) == m:
            print(' '.join(map(str, s)))
            return

        for i in range(1, n + 1):
            if i not in s:
                s.append(i)
                generate_combinations()
                s.pop()

    generate_combinations()

if __name__ == '__main__':
    n, m = map(int, input().split())
    dfs(n, m)