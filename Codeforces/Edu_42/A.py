n = int(input())
a = list(map(int, input().split()))
sm = sum(a) / 2
ans = 0
for i in range(0, n):
	ans += a[i]
	if ans >= sm:
		break;
print(i + 1)