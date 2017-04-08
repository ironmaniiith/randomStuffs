#!/usr/bin/python
import inspect, re
from itertools import permutations, combinations
import operator
from copy import deepcopy

def getNumberSequence(arr):
	"""
		arr = ([1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
			[1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
			[1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
		 )
		 returns -> ['111', '100', '110', '110', '101', '011', '011', '100', '111', '101']
	"""
	number_seq = []
	for i in xrange(0,len(a)):
		bit_seq = ''
		for seq in arr:
			bit_seq += str(seq[i])
		number_seq.append(bit_seq)
	return number_seq

def varname(p):
	for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
		m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
		if m:
			return m.group(1)

def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj]

def pair_indices(s, arr, rev_arr):
	return arr.index(s), len(arr) - rev_arr.index(s) - 1

def add_0_1(arr, t, dec):
	arr[t[int(dec)]] = arr[t[int(dec)]] + "0"
	arr[t[int(dec)^1]] = arr[t[int(dec)^1]] + "1"
	# print arr

	# Later on also add the shuffling of order of bits while adding 0 or 1 if required


a = [1,0,1,1,0,1,1,1,1,1]
b = [1,1,1,1,1,0,0,1,1,1]
c = [1,1,0,1,1,1,1,1,1,1]
d = [1,0,1,1,0,1,1,0,1,0]
e = [1,0,1,0,0,0,1,0,1,0]
f = [1,0,0,0,1,1,1,0,1,1]
g = [0,0,1,1,1,1,1,0,1,1]

# getNumberSequence((b,d,f))

complete_arr = [a,b,c,d,e,f,g]

count = {}
for i in complete_arr:
	name = namestr(i, globals())[0]
	# print "Initializing {0} to {1}".format(name,0)
	count[name] = 0
print count

required_bits = 3
max_repetition = 2
C = combinations(complete_arr, required_bits)

# This is an awesome code to print the name of the variable :P. Yes you read it correct :P.
# for i in p:
# 	for j in i:
# 		print namestr(j, globals())[0],
# 	print
ans = []
ans_arr = []
for arr in C:
	final_arr = []
	repeated = []
	for i in xrange(0,len(a)):
		x = ''
		for j in xrange(0,required_bits):
			x += str(arr[j][i])
		# print x
		if x not in final_arr:
			final_arr.append(x)
		else:
			repeated.append(x)
			# try:
				# r[x] += 1
			# except Exception, e:
				# r[x] = 0
	flag = True
	if len(final_arr) >= 5:
		for i in repeated:
			if repeated.count(i) > 1:
				print "NO"
				flag = False
				break
		if flag:
			print repeated
			ans.append(repeated)
			for i in arr:
				print namestr(i, globals())[0],
				count[namestr(i, globals())[0]]+=1
			print 
			for i in arr:
				print i
			ans_arr.append(arr)
print sorted(count.items(), key=operator.itemgetter(1))

final_seq = []
for j in xrange(0,2):
	for seq in ans:
		for num in seq:
			final_seq.append(num+str(j))

concatinated_final_ans_arr = []
unique_concatinated_final_ans_arr = []
for arr in ans_arr:
	number_seq = getNumberSequence(arr)
	concatinated_final_ans_arr.append(number_seq)
	unique_concatinated_final_ans_arr.append(set(number_seq))
# print unique_concatinated_final_ans_arr
print concatinated_final_ans_arr
# The concatinated_final_ans_arr is of the form
# [['111', '100', '110', '110', '101', '011', '011', '100', '111', '101']]

bit_seq_pair_dicts = []
# Store the information like this:
# [{'011': (5, 6), '100': (1, 7), '101': (4, 9), '111': (0, 8), '110': (2, 3)}]

for arr in concatinated_final_ans_arr:
	rev_arr = deepcopy(arr)
	rev_arr.reverse()
	d = {}
	for bit_seq in arr:
		i,j = pair_indices(bit_seq, arr, rev_arr)
		try:
			d[bit_seq]
		except Exception, e:
			d[bit_seq] = (i,j)
	bit_seq_pair_dicts.append(d)
print bit_seq_pair_dicts


# And both 0 and 1 bit to the repeated bits in concatinated_final_ans_arr
dot_bit_added_bit_seq = []

# Take into consideration all the possible P&C's of the strings present in the bit_seq_pair_dicts
for index, d in enumerate(bit_seq_pair_dicts):
	keys = d.keys()
	l = len(keys)
	print "Length is ",l
	for i in xrange(0, 2**l):
		bit = '{0:0'+ str(l) +'b}'
		bit = bit.format(i)
		print "Bit is ", bit
		old_arr = deepcopy(concatinated_final_ans_arr[index])
		for j in xrange(0,l):
			add_0_1(old_arr, d[keys[j]], bit[j])
		print old_arr
		print "Hello"
# for s in concatinated_final_ans_arr:
# 	s = list(s)
# 	print s
# 	for i in [0,1]:
# 		for arr in s:
# 			dot_bit_added_bit_seq.append(arr + str(i))

# print dot_bit_added_bit_seq
print bit_seq_pair_dicts