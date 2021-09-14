mouse exome chr 1
human3 contig 1

This experiment aims to find the relationship between Coverage and False negative

Same as human3-2 but
1) Mutation indices will be picked with an additional filter for mapq and queryQ
2) Mutation indices will be the same for each bam file. last time it was random sample 1000 per coverage bin
3) Coverages will be binned to be by 10step until 200x and then 100step until 3000x making it about 50,000 mutations per bam file.
4) Lets crank AF up to 15%
5) This time I'll verify in IGV a lot more so there won't be any bugs. not that there's proof there were any last time.

1) Generate mutations vcf files with
python generate_mutations_vcf.py

2) Use vcfs to mod the bam and put them in modded_bams folder
Best not to try running these all in different terminals. I had some weird errors show up. dunno why but it may not be able to do it.

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

4) Check IGV for files modded, 1,5,10,15,20
Check each bins mutations make sure they were all input correctly
This step is very important.
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

6) Run the compare vcfs script to get final data on how well Mutect did