import random
import os
import subprocess

df = [1, 6,1,31,31,31]

cnt = 1
while True:

#print(df)
	arrA = []
	arrB = []

	for j in range(1):
		for i in range(len(df)):
			a = random.randint(0,0xffffffff) & 0xffffffff
			b = (a ^ pow(2,df[i])) & 0xffffffff

			arrA.append(str(hex(a)).replace("0x", ""))
			arrB.append(str(hex(b)).replace("0x",""))
	'''
	print(arrA)
	print(arrB)
	'''

	m1 = ""
	m2 = ""

	for i in range(len(arrA)):
		m1 += arrA[i]
		m2 += arrB[i]

	'''
	print(m1)
	print("\n\n")
	print(m2)
	break	
	'''

	cmd = ['./sha', m1]
	fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout 
	data = fd_popen.read().strip() 
	fd_popen.close() 
	
	cmd = ['./sha', m2]
	fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
	data2 = fd_popen.read().strip()
	'''
	if data == data:
		print(data)
		print(data2)
		break
	'''

	data = data.split(" ")
	data2 = data2.split(" ")

	'''
	for i in range(len(data)):
		if data[i] == data2[i]:
			print(data)
			print(data2)
			exit(0)
	'''
	
	if data == data2:
		print("m1 =",arrA)
		print("m2 =",arrB)
		print("hash1 =",data)
		print("hash2 =",data2)
		print("try:",cnt)
		break

	cnt= cnt +1
