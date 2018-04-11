n, a, b = [int(i) for i in input().split()]
s = input()
sum, cnt, v = a + b, 0, []
for i in range(0, n):
	if s[i] == '.':
		cnt += 1
	else:
		if cnt != 0:
			v.append(cnt)
		cnt = 0
if cnt != 0:
	v.append(cnt)
for i in range(0, len(v)):
	if a > b:
		if v[i] % 2 == 0:
			na = v[i] // 2
			nb = v[i] // 2
		else:
			na = v[i] // 2 + 1
			nb = v[i] // 2
		if a >= na:
			if nb <= b:
				a -= na
				b -= nb
			else:
				a -= na
				b = 0
		else:
			if nb <= b:
				b -= nb
				a = 0
			else:
				a = 0
				b = 0
	else:
		if v[i] % 2 == 0:
			na = v[i] // 2
			nb = v[i] // 2
		else:
			na = v[i] // 2
			nb = v[i] // 2 + 1
		if b >= nb:
			if na <= a:
				a -= na
				b -= nb
			else:
				b -= nb
				a = 0
		else:
			if na <= a:
				a -= na
				b = 0
			else:
				a = 0
				b = 0
print(sum - (a + b))
			