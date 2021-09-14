This analysis uses data for human cells sequenced at 1000x coverage obtained from
https://www.ncbi.nlm.nih.gov/sra/SRX5342252[accn]
After aligning the bam is stored as human3.bam

This experiment aims to find the relationship between coverage, allele frequency and false negatives

1) Indices selected for artificial mutation are filtered for sufficient mapQ and readQ
2) Mutation indices will be the same for each bam file. The difference is the percentage of reads mutated. the allele frequency
3) Coverages will be binned with step 10 until 200x and then step 100 until 3000x and 600 indices are selected per coverage bin. This makes 28,800 total artificial mutations per bam file. 600 x 48bins
4) Allele frequency will step by 1% from 1 to 20%

Artificial mutations are inserted with biostar404363.jar, a script developed by Lindenbaum, Pierre
Obtained through http://lindenb.github.io/jvarkit/Biostar404363.html
Usage - The program take in an original unmodified bam file(human3.bam), and a vcf file containing information on what mutations should be inserted at what rate(will be generated), and uses that to make the modifications.

Preprocessing
----
human3.bam was obtained from SRA, aligned, sorted, indexed, then only the first contig (CM000663.2) was separated out with "bamtools split -in human3.bam -reference"
coverage.txt was obtained with "samtools depth human3.bam -o coverage.txt"
A copy of hg38 is required as well obtained through Assembly database.

Step for the analysis
-----
1) Generate mutations vcf files with
python generate_mutations_vcf.py

2) Use generated vcfs to mod the bam and put them in modded_bams folder
Run batched in different terminal windows

java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/1_mutations.vcf human3.bam -o ./modded_bams/modded_1.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/2_mutations.vcf human3.bam -o ./modded_bams/modded_2.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/3_mutations.vcf human3.bam -o ./modded_bams/modded_3.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/4_mutations.vcf human3.bam -o ./modded_bams/modded_4.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/5_mutations.vcf human3.bam -o ./modded_bams/modded_5.bam

java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/6_mutations.vcf human3.bam -o ./modded_bams/modded_6.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/7_mutations.vcf human3.bam -o ./modded_bams/modded_7.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/8_mutations.vcf human3.bam -o ./modded_bams/modded_8.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/9_mutations.vcf human3.bam -o ./modded_bams/modded_9.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/10_mutations.vcf human3.bam -o ./modded_bams/modded_10.bam

java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/11_mutations.vcf human3.bam -o ./modded_bams/modded_11.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/12_mutations.vcf human3.bam -o ./modded_bams/modded_12.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/13_mutations.vcf human3.bam -o ./modded_bams/modded_13.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/14_mutations.vcf human3.bam -o ./modded_bams/modded_14.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/15_mutations.vcf human3.bam -o ./modded_bams/modded_15.bam

java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/16_mutations.vcf human3.bam -o ./modded_bams/modded_16.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/17_mutations.vcf human3.bam -o ./modded_bams/modded_17.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/18_mutations.vcf human3.bam -o ./modded_bams/modded_18.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/19_mutations.vcf human3.bam -o ./modded_bams/modded_19.bam
java -jar /Users/jiggy/jvarkit/dist/biostar404363.jar -p ./artificial_mutations/20_mutations.vcf human3.bam -o ./modded_bams/modded_20.bam

3) Index the bams
cd modded_bams
samtools index modded_1.bam
samtools index modded_2.bam
samtools index modded_3.bam
samtools index modded_4.bam
samtools index modded_5.bam
samtools index modded_6.bam
samtools index modded_7.bam
samtools index modded_8.bam
samtools index modded_9.bam
samtools index modded_10.bam
samtools index modded_11.bam
samtools index modded_12.bam
samtools index modded_13.bam
samtools index modded_14.bam
samtools index modded_15.bam
samtools index modded_16.bam
samtools index modded_17.bam
samtools index modded_18.bam
samtools index modded_19.bam
samtools index modded_20.bam

4) Check IGV for modded_1.bam, modded_5.bam, modded_10.bam, modded_15.bam, modded_20.bam 
Make sure artificial mutations are there
Make sure indices match.

5) Run Mutect on the modded bams. Five in each terminal window
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_1.bam -O ~/low_af_sim/human3_3/discovered_mutations/1_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_2.bam -O ~/low_af_sim/human3_3/discovered_mutations/2_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_3.bam -O ~/low_af_sim/human3_3/discovered_mutations/3_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_4.bam -O ~/low_af_sim/human3_3/discovered_mutations/4_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_5.bam -O ~/low_af_sim/human3_3/discovered_mutations/5_discovered.vcf

gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_6.bam -O ~/low_af_sim/human3_3/discovered_mutations/6_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_7.bam -O ~/low_af_sim/human3_3/discovered_mutations/7_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_8.bam -O ~/low_af_sim/human3_3/discovered_mutations/8_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_9.bam -O ~/low_af_sim/human3_3/discovered_mutations/9_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_10.bam -O ~/low_af_sim/human3_3/discovered_mutations/10_discovered.vcf

gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_11.bam -O ~/low_af_sim/human3_3/discovered_mutations/11_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_12.bam -O ~/low_af_sim/human3_3/discovered_mutations/12_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_13.bam -O ~/low_af_sim/human3_3/discovered_mutations/13_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_14.bam -O ~/low_af_sim/human3_3/discovered_mutations/14_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_15.bam -O ~/low_af_sim/human3_3/discovered_mutations/15_discovered.vcf

gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_16.bam -O ~/low_af_sim/human3_3/discovered_mutations/16_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_17.bam -O ~/low_af_sim/human3_3/discovered_mutations/17_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_18.bam -O ~/low_af_sim/human3_3/discovered_mutations/18_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_19.bam -O ~/low_af_sim/human3_3/discovered_mutations/19_discovered.vcf
gatk --java-options -Xmx16G Mutect2 -R ~/reference_genomes/hg38/hg38.fna -I ~/low_af_sim/human3_3/modded_bams/modded_20.bam -O ~/low_af_sim/human3_3/discovered_mutations/20_discovered.vcf

6) Compare discovered mutations with artificial mutations to get false negative rate for each AF and coverage level
python results_analysis.py

7) Copy paste results from results_analysis into the data line of plot_results.py