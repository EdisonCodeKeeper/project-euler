def fn(n):
	return (3, n * (n + 1) / 2), (4, n * n), (5, n * (3 * n - 1) / 2), (6, n * (2 * n - 1)), (7, n * (5 * n - 3) / 2), (8, n * (3 * n - 2))

def next(types, data):
	if len(types) == 6 and data[0] / 100 == data[-1] % 100:
		print data, sum(data)
	else:
		for t, d in ds.get((types[-1], data[-1]), []):
			if t not in types:
				next(types + [t], data + [d])

if __name__ == '__main__':
	p = []
	n = 19
	while n < 141:
		for type, data in fn(n):
			if 1000 <= data <= 9999 and data % 100 > 9:
				p.append((type, data))
		n += 1
	ds = {}
	for t1, d1 in p:
		for t2, d2 in p:
			if t1 != t2 and d1 % 100 == d2 / 100:
				ds[t1, d1] = ds.get((t1, d1), []) + [(t2, d2)]
	for type, data in ds:
		next([type], [data])