#!/usr/bin/env python3
import sys
import pysam

def check_ref(vcf_file, ref_fasta, corrected_vcf, filtered_vcf, stats_file):
    fasta = pysam.FastaFile(ref_fasta)

    total = 0
    corrected = 0
    filtered_out = 0
    invalid_ref_count = 0

    with open(vcf_file, 'r') as fin, \
         open(corrected_vcf, 'w') as fcorrected, \
         open(filtered_vcf, 'w') as ffiltered:

        for line in fin:
            if line.startswith('#'):
                fcorrected.write(line)
                ffiltered.write(line)
                continue

            total += 1
            fields = line.strip().split('\t')
            chrom = fields[0]
            pos = int(fields[1])
            ref = fields[3]
            alt = fields[4]

            # Correction 
            ref_genome_base = fasta.fetch(chrom, pos - 1, pos).upper()

            if ref != ref_genome_base:
                corrected += 1
                fields[3] = ref_genome_base
                ref = ref_genome_base

            line_out = '\t'.join(fields) + '\n'
            fcorrected.write(line_out)

            # Filtrage REF == ALT
            if ref != alt:
                ffiltered.write(line_out)
            else:
                filtered_out += 1

    # Validation 
    with open(filtered_vcf, 'r') as fcheck:
        for line in fcheck:
            if line.startswith('#'):
                continue
            ref = line.strip().split('\t')[3]
            if ref not in ["A", "C", "G", "T"]:
                invalid_ref_count += 1

    
    with open(stats_file, 'w') as stats:
        stats.write(f"Total variants: {total}\n")
        stats.write(f"Corrected REF alleles: {corrected}\n")
        stats.write(f"Filtered out (REF == ALT): {filtered_out}\n")
        stats.write(f"Final variants kept: {total - filtered_out}\n")
        stats.write(f"Percentage corrected: {corrected / total * 100:.2f}%\n")
        stats.write(f"Percentage removed (REF == ALT): {filtered_out / total * 100:.2f}%\n")
        stats.write(f"Invalid REF entries in filtered VCF: {invalid_ref_count}\n")

    if invalid_ref_count > 0:
        print(f"⚠️ Attention : {invalid_ref_count} lignes dans {filtered_vcf} ont des REF invalides (≠ A/C/G/T)")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    vcf_input = sys.argv[1]
    ref_fasta = sys.argv[2]
    corrected_vcf = sys.argv[3]
    stats_file = sys.argv[4]
    filtered_vcf = corrected_vcf.replace("_checked.vcf", "_filtered.vcf")

    check_ref(vcf_input, ref_fasta, corrected_vcf, filtered_vcf, stats_file)

