import sets as s


s1=s.Set()
n=s.Set()
o=s.Set()

for x in range(0,51):
	if x%2 is 0:
		n.add(x)
	else:
		o.add(x)

print(n)
print(o)
s1 = n|o
print(s1)
s2 = n&o
print(s2)
print(s1.size())
s1.remove(0)
print(s1.size())

s3= s.Set()
for x in range(0, 31):
	s3.add(x)


print(s3)
s4 = s3 - n
s5 = n-s3
print(s4)
print(s5)

