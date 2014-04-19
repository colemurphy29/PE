sos = 0
ss = 0
for x in range(1, 101):
	sos += x**2
	ss += x
ss = ss**2
print ss-sos