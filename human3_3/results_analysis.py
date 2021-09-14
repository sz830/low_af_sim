from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# This time we look at a discovered vcf we're looking for the 29000 mutations inserted at 19 different coverage bins.

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

data_3d = []
bin_map = {1: 5,
		   2: 15,
		   3: 25,
		   4: 35,
		   5: 45,
		   6: 55,
		   7: 65,
		   8: 75,
		   9: 85,
		   10: 95,
		   11: 105,
		   12: 115,
		   13: 125,
		   14: 135,
		   15: 145,
		   16: 155,
		   17: 165,
		   18: 175,
		   19: 185,
		   20: 195,
		   21: 250,
		   22: 350,
		   23: 450,
		   24: 550,
		   25: 650,
		   26: 750,
		   27: 850,
		   28: 950,
		   29: 1050,
		   30: 1150,
		   31: 1250,
		   32: 1350,
		   33: 1450,
		   34: 1550,
		   35: 1650,
		   36: 1750,
		   37: 1850,
		   38: 1950,
		   39: 2050,
		   40: 2150,
		   41: 2250,
		   42: 2350,
		   43: 2450,
		   44: 2550,
		   45: 2650,
		   46: 2750,
		   47: 2850,
		   48: 2950}

mutations_file = open("./artificial_mutations/1_mutations.vcf", "r")
txt = mutations_file.read()
lines = txt.splitlines()[3:] # trash the first 3 header lines

artificial_mutation_indices = []
for line in lines:
	words = line.split()
	index = words[1]
	artificial_mutation_indices.append(index)
print(str(len(artificial_mutation_indices))+" Artificial mutations") # should be 28,800

def chunks(lst, n):
	"""Yield successive n-sized chunks from lst."""
	for i in range(0, len(lst), n):
		yield lst[i:i + n]

bins = list(chunks(artificial_mutation_indices, 600)) # generate mutations used 600 mutations per coverage level
print("Num of bins should be 48:"+str(len(bins)))
print("Size of first bin should be 600:"+str(len(bins[0])))
print("Size of last bin should be 600:"+str(len(bins[len(bins)-1])))

for AF in range(1,21):
	mods_file = open("discovered_mutations/"+str(AF)+"_discovered.vcf", "r") 
	txt = mods_file.read()
	lines = txt.splitlines()
	
	# Find when the header ends, toss the lines before that
	start_index = 0
	for i in range(100000):
		if lines[i][0] != "#":
			start_index=i
			break;
	lines = lines[start_index:]
	print("start index:"+str(start_index))

	found_mutation_indices = []
	for line in lines:
		words = line.split()
		index = words[1]
		found_mutation_indices.append(index)

	print(str(len(found_mutation_indices))+" Total mutations found by Mutect out of what shoudl be 28,800")

	bin_number = 0
	for i in bins:
		bin_number+=1
		found_artificial_mutations=intersection(found_mutation_indices,i)
		print("For AF:"+str(AF)+" and coverage:"+str(bin_number)+" found:"+str(len(found_artificial_mutations)) +" out of 600")
		false_negative_rate = 1-(len(found_artificial_mutations)/600)
		print("False negative rate:"+str(false_negative_rate))
		data_3d.append([AF,bin_map[bin_number],false_negative_rate])

fig = plt.figure()
ax = plt.axes(projection='3d')
xdata=[]
ydata=[]
zdata=[]
for point in data_3d:
	xdata.append(point[0])
	ydata.append(point[1])
	zdata.append(point[2])

print(data_3d)

ax.scatter3D(xdata, ydata, zdata)
plt.show()






