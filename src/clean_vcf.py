#!/usr/bin/env python3
import sys


valid_bases = {"A", "C", "G", "T"}

def is_valid_ref_alt(ref, alt):
    #REF
    if ref == '' or ref == '.' or ref == 'N' or ref not in valid_bases:
        return False

    #ALT
    alt_bases = alt.split(',')
    for b in alt_bases:
        if b == '' or b == '.' or b == 'N' or b not in valid_bases:
            return False

    return True

def filter_vcf(input_vcf, output_vcf):
    with open(input_vcf, 'r') as fin, open(output_vcf, 'w') as fout:
        for line in fin:
            if line.startswith('#'):
                fout.write(line)
                continue

            parts = line.strip().split('\t')
            if len(parts) < 5:
                continue  

            ref = parts[3]
            alt = parts[4]

            if is_valid_ref_alt(ref, alt):
                fout.write(line)

if __name__ == "__main__":
    input_vcf = "../data/checked/henn_filtered.vcf"
    output_vcf = "../data/checked/henn_filtered1.vcf"
    filter_vcf(input_vcf, output_vcf)
    print(f"✅ clean : {output_vcf}")
