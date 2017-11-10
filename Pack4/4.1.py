class sd():
	def __init__(self, skra):
		l = skra.split(",")
		self.skra = skra
		self.time = int(str(skra[0:2]) + str(skra[3:5]) + str(skra[6:8]) + str(skra[9:12]))
		self.cost = round(float(l[2]) * 100)
		self.ex = l[3][0]
		self.kol = int(l[2])

class issl(list):
	def __init__(self, x):
		self.max = [0, 0]
		self.c = 0
		self.k = set(str(x))
	def rez(self):
		l1 = str(self.max[1] // 10000000) + "." + str((self.max[1] // 1000) % 100) + "."
		l2 = str((self.max[1] // 100000) % 100) + "." + str(self.max[1] % 1000)
		la = l1 + l2
		l3 = str(self.max[1] // 10000000) + "." + str((self.max[1] // 1000) % 100) + "."
		l4 = str((self.max[1] // 100000) % 100 + 1) + "." + str(self.max[1] % 1000)
		lb = l3 + l4
		print(la,lb)
	def pupu(self, y):
		if(y.ex in self.k):
			self.append(y)
			self.c += 1
			while (self[0].time + 1000 <= y.time):
				self.c -= 1
				del self[0]
			if (self.c > self.max[0]):
				self.max[0] = int(self.c)
				self.max[1] = int(self[0].time)


print("Vvedite Birzhi:")
st = input()
with open("TRD2.csv") as f:
	s = issl(st)
	f.readline()
	for line in f.readlines():
		s.pupu(sd(line))
	s.rez()
