import pysam
import random
import numpy as np

# Run: python generate_mutations_vcf.py
# Will read some files and generate artificial mutations files in artificial_mutations/ folder at allele frequencies 1-20

reference = pysam.FastaFile("/Users/jiggy/reference_genomes/hg38/hg38.fna")
f = open("coverage.txt", "r") # a file generated via samtools depth. gives coverage at each base
txt = f.read()
lines = txt.splitlines() # 23,262,277 bases in this contig
chrom = "CM000663.2" # because I split the bams by contigs, the low allele freq analysis will be done only on this contig. chrom 1

# Fill the quality_map which contains mapq and readq averaged values at all indices
# Used to filter indices later
quality_map = {}
bam = pysam.AlignmentFile("human3.bam", "rb")
for pileupcolumn in bam.pileup("CM000663.2", stepper="nofilter", min_base_quality=0):
	index = pileupcolumn.reference_pos+1 # pysam is 0-indexed, but we work with 1-indexed
	mapping_qualities = pileupcolumn.get_mapping_qualities()
	query_qualities = pileupcolumn.get_query_qualities()
	avg_readq = sum(query_qualities)/len(query_qualities)
	avg_mapq = sum(mapping_qualities)/len(mapping_qualities)# 60,70,90,100 bins dont have enough entries
	quality_map[index]=[avg_readq, avg_mapq]

# Thresholds determined after plotting the data and chosen arbitrarily.
readq_threshold = 30
mapq_threshold = 43
# Indices of coverage level A to B.
indices_0_10 = []
indices_10_20 = []
indices_20_30 = []
indices_30_40 = []
indices_40_50 = []
indices_50_60 = []
indices_60_70 = []
indices_70_80 = []
indices_80_90 = []
indices_90_100 = []
indices_100_110 = []
indices_110_120 = []
indices_120_130 = []
indices_130_140 = []
indices_140_150 = []
indices_150_160 = []
indices_160_170 = []
indices_170_180 = []
indices_180_190 = []
indices_190_200 = []
indices_200_300 = []
indices_300_400 = []
indices_400_500 = []
indices_500_600 = []
indices_600_700 = []
indices_700_800 = []
indices_800_900 = []
indices_900_1000 = []
indices_1000_1100 = []
indices_1100_1200 = []
indices_1200_1300 = []
indices_1300_1400 = []
indices_1400_1500 = []
indices_1500_1600 = []
indices_1600_1700 = []
indices_1700_1800 = []
indices_1800_1900 = []
indices_1900_2000 = []
indices_2000_2100 = []
indices_2100_2200 = []
indices_2200_2300 = []
indices_2300_2400 = []
indices_2400_2500 = []
indices_2500_2600 = []
indices_2600_2700 = []
indices_2700_2800 = []
indices_2800_2900 = []
indices_2900_3000 = []

# Sort our 1-based indices into these buckets
for line in lines:
	words = line.split()
	index = words[1]
	coverage = int(words[2])
	readq = quality_map[int(index)][0]
	mapq = quality_map[int(index)][1]
	if(readq >= readq_threshold and mapq >= mapq_threshold):
		if(coverage<10):
			indices_0_10.append(index)
		elif(coverage<20):
			indices_10_20.append(index)
		elif(coverage<30):
			indices_20_30.append(index)
		elif(coverage<40):
			indices_30_40.append(index)
		elif(coverage<50):
			indices_40_50.append(index)
		elif(coverage<60):
			indices_50_60.append(index)
		elif(coverage<70):
			indices_60_70.append(index)
		elif(coverage<80):
			indices_70_80.append(index)
		elif(coverage<90):
			indices_80_90.append(index)
		elif(coverage<100):
			indices_90_100.append(index)
		elif(coverage<110):
			indices_100_110.append(index)
		elif(coverage<120):
			indices_110_120.append(index)
		elif(coverage<130):
			indices_120_130.append(index)
		elif(coverage<140):
			indices_130_140.append(index)
		elif(coverage<150):
			indices_140_150.append(index)
		elif(coverage<160):
			indices_150_160.append(index)
		elif(coverage<170):
			indices_160_170.append(index)
		elif(coverage<180):
			indices_170_180.append(index)
		elif(coverage<190):
			indices_180_190.append(index)
		elif(coverage<200):
			indices_190_200.append(index)
		elif(coverage<300):
			indices_200_300.append(index)
		elif(coverage<400):
			indices_300_400.append(index)
		elif(coverage<500):
			indices_400_500.append(index)
		elif(coverage<600):
			indices_500_600.append(index)
		elif(coverage<700):
			indices_600_700.append(index)
		elif(coverage<800):
			indices_700_800.append(index)
		elif(coverage<900):
			indices_800_900.append(index)
		elif(coverage<1000):
			indices_900_1000.append(index)
		elif(coverage<1100):
			indices_1000_1100.append(index)
		elif(coverage<1200):
			indices_1100_1200.append(index)
		elif(coverage<1300):
			indices_1200_1300.append(index)
		elif(coverage<1400):
			indices_1300_1400.append(index)
		elif(coverage<1500):
			indices_1400_1500.append(index)
		elif(coverage<1600):
			indices_1500_1600.append(index)
		elif(coverage<1700):
			indices_1600_1700.append(index)
		elif(coverage<1800):
			indices_1700_1800.append(index)
		elif(coverage<1900):
			indices_1800_1900.append(index)
		elif(coverage<2000):
			indices_1900_2000.append(index)
		elif(coverage<2100):
			indices_2000_2100.append(index)
		elif(coverage<2200):
			indices_2100_2200.append(index)
		elif(coverage<2300):
			indices_2200_2300.append(index)
		elif(coverage<2400):
			indices_2300_2400.append(index)
		elif(coverage<2500):
			indices_2400_2500.append(index)
		elif(coverage<2600):
			indices_2500_2600.append(index)
		elif(coverage<2700):
			indices_2600_2700.append(index)
		elif(coverage<2800):
			indices_2700_2800.append(index)
		elif(coverage<2900):
			indices_2800_2900.append(index)
		elif(coverage<3000):
			indices_2900_3000.append(index)

print("Printing bin sizes") # To get an idea of how many artificial mutations can be created per bin
print(len(indices_0_10))
print(len(indices_10_20))
print(len(indices_20_30))
print(len(indices_30_40))
print(len(indices_40_50))
print(len(indices_50_60))
print(len(indices_60_70))
print(len(indices_70_80))
print(len(indices_80_90))
print(len(indices_90_100))
print(len(indices_100_110))
print(len(indices_110_120))
print(len(indices_120_130))
print(len(indices_130_140))
print(len(indices_140_150))
print(len(indices_150_160))
print(len(indices_160_170))
print(len(indices_170_180))
print(len(indices_180_190))
print(len(indices_190_200))
print(len(indices_200_300))
print(len(indices_300_400))
print(len(indices_400_500))
print(len(indices_500_600))
print(len(indices_600_700))
print(len(indices_700_800))
print(len(indices_800_900))
print(len(indices_900_1000))
print(len(indices_1000_1100))
print(len(indices_1100_1200))
print(len(indices_1200_1300))
print(len(indices_1300_1400))
print(len(indices_1400_1500))
print(len(indices_1500_1600))
print(len(indices_1600_1700))
print(len(indices_1700_1800))
print(len(indices_1800_1900))
print(len(indices_1900_2000))
print(len(indices_2000_2100))
print(len(indices_2100_2200))
print(len(indices_2200_2300))
print(len(indices_2300_2400))
print(len(indices_2400_2500))
print(len(indices_2500_2600))
print(len(indices_2600_2700))
print(len(indices_2700_2800))
print(len(indices_2800_2900))
print(len(indices_2900_3000))

# Select mutation indices randomly from areas of high coverage
n_mutations = 600 # Some bins don't 1000 viable indices.
indices_0_10 = random.sample(indices_0_10, n_mutations)
indices_0_10.sort()
indices_10_20 = random.sample(indices_10_20, n_mutations)
indices_10_20.sort()
indices_20_30 = random.sample(indices_20_30, n_mutations)
indices_20_30.sort()
indices_30_40 = random.sample(indices_30_40, n_mutations)
indices_30_40.sort()
indices_40_50 = random.sample(indices_40_50, n_mutations)
indices_40_50.sort()
indices_50_60 = random.sample(indices_50_60, n_mutations)
indices_50_60.sort()
indices_60_70 = random.sample(indices_60_70, n_mutations)
indices_60_70.sort()
indices_70_80 = random.sample(indices_70_80, n_mutations)
indices_70_80.sort()
indices_80_90 = random.sample(indices_80_90, n_mutations)
indices_80_90.sort()
indices_90_100 = random.sample(indices_90_100, n_mutations)
indices_90_100.sort()
indices_100_110 = random.sample(indices_100_110, n_mutations)
indices_100_110.sort()
indices_110_120 = random.sample(indices_110_120, n_mutations)
indices_110_120.sort()
indices_120_130 = random.sample(indices_120_130, n_mutations)
indices_120_130.sort()
indices_130_140 = random.sample(indices_130_140, n_mutations)
indices_130_140.sort()
indices_140_150 = random.sample(indices_140_150, n_mutations)
indices_140_150.sort()
indices_150_160 = random.sample(indices_150_160, n_mutations)
indices_150_160.sort()
indices_160_170 = random.sample(indices_160_170, n_mutations)
indices_160_170.sort()
indices_170_180 = random.sample(indices_170_180, n_mutations)
indices_170_180.sort()
indices_180_190 = random.sample(indices_180_190, n_mutations)
indices_180_190.sort()
indices_190_200 = random.sample(indices_190_200, n_mutations)
indices_190_200.sort()
indices_200_300 = random.sample(indices_200_300, n_mutations)
indices_200_300.sort()
indices_300_400 = random.sample(indices_300_400, n_mutations)
indices_300_400.sort()
indices_400_500 = random.sample(indices_400_500, n_mutations)
indices_400_500.sort()
indices_500_600 = random.sample(indices_500_600, n_mutations)
indices_500_600.sort()
indices_600_700 = random.sample(indices_600_700, n_mutations)
indices_600_700.sort()
indices_700_800 = random.sample(indices_700_800, n_mutations)
indices_700_800.sort()
indices_800_900 = random.sample(indices_800_900, n_mutations)
indices_800_900.sort()
indices_900_1000 = random.sample(indices_900_1000, n_mutations)
indices_900_1000.sort()
indices_1000_1100 = random.sample(indices_1000_1100, n_mutations)
indices_1000_1100.sort()
indices_1100_1200 = random.sample(indices_1100_1200, n_mutations)
indices_1100_1200.sort()
indices_1200_1300 = random.sample(indices_1200_1300, n_mutations)
indices_1200_1300.sort()
indices_1300_1400 = random.sample(indices_1300_1400, n_mutations)
indices_1300_1400.sort()
indices_1400_1500 = random.sample(indices_1400_1500, n_mutations)
indices_1400_1500.sort()
indices_1500_1600 = random.sample(indices_1500_1600, n_mutations)
indices_1500_1600.sort()
indices_1600_1700 = random.sample(indices_1600_1700, n_mutations)
indices_1600_1700.sort()
indices_1700_1800 = random.sample(indices_1700_1800, n_mutations)
indices_1700_1800.sort()
indices_1800_1900 = random.sample(indices_1800_1900, n_mutations)
indices_1800_1900.sort()
indices_1900_2000 = random.sample(indices_1900_2000, n_mutations)
indices_1900_2000.sort()
indices_2000_2100 = random.sample(indices_2000_2100, n_mutations)
indices_2000_2100.sort()
indices_2100_2200 = random.sample(indices_2100_2200, n_mutations)
indices_2100_2200.sort()
indices_2200_2300 = random.sample(indices_2200_2300, n_mutations)
indices_2200_2300.sort()
indices_2300_2400 = random.sample(indices_2300_2400, n_mutations)
indices_2300_2400.sort()
indices_2400_2500 = random.sample(indices_2400_2500, n_mutations)
indices_2400_2500.sort()
indices_2500_2600 = random.sample(indices_2500_2600, n_mutations)
indices_2500_2600.sort()
indices_2600_2700 = random.sample(indices_2600_2700, n_mutations)
indices_2600_2700.sort()
indices_2700_2800 = random.sample(indices_2700_2800, n_mutations)
indices_2700_2800.sort()
indices_2800_2900 = random.sample(indices_2800_2900, n_mutations)
indices_2800_2900.sort()
indices_2900_3000 = random.sample(indices_2900_3000, n_mutations)
indices_2900_3000.sort()

for AF in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]: # 1% to 20% AF
	filename = "./artificial_mutations/"+str(AF)+"_mutations.vcf"
	file = open(filename,"a")
	# Print header stuff. For VCF files
	file.write("##fileformat=VCFv4.2\n")
	file.write("##INFO=<ID=AF,Number=A,Type=Float,Description=\"Allele Frequency among genotypes, for each ALT allele, in the same order as listed\">\n")
	file.write("#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO\n")

	indices = indices_0_10 + indices_10_20 + indices_20_30 + indices_30_40 + indices_40_50 + indices_50_60 + indices_60_70 + indices_70_80 + indices_80_90 + indices_90_100 + indices_100_110 + indices_110_120 + indices_120_130 + indices_130_140 + indices_140_150 + indices_150_160 + indices_160_170 + indices_170_180 + indices_180_190 + indices_190_200 + indices_200_300 + indices_300_400 + indices_400_500 + indices_500_600 + indices_600_700 + indices_700_800 + indices_800_900 + indices_900_1000 + indices_1000_1100 + indices_1100_1200 + indices_1200_1300 + indices_1300_1400 + indices_1400_1500 + indices_1500_1600 + indices_1600_1700 + indices_1700_1800 + indices_1800_1900 + indices_1900_2000 + indices_2000_2100 + indices_2100_2200 + indices_2200_2300 + indices_2300_2400 + indices_2400_2500 + indices_2500_2600 + indices_2600_2700 + indices_2700_2800 + indices_2800_2900 + indices_2900_3000

	possible_bases = ["A","T","C","G"]
	for index in indices:
		ref = reference.fetch(chrom,int(index)-1,int(index)).upper()
		alt = "A"
		# Make alt something that isn't the reference
		if ref in possible_bases:
			alt = possible_bases[(possible_bases.index(ref)+1)%4]
		file.write(chrom+"\t"+index+"\t.\t"+ref+"\t"+alt+"\t.\t.\tAF="+str(AF/100)+"\n")
	file.close()




