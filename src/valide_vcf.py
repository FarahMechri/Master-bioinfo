#!/usr/bin/env python3
import sys

def check_vcf_simple(vcf_file, output_file):
    valid_bases = {'A','G','T','C'}
    ref_invalid_count = 0
    alt_invalid_count = 0
    
    ref_empty = 0
    ref_N = 0
    ref_dot = 0
    
    alt_empty = 0
    alt_N = 0
    alt_dot = 0
    
    with open(vcf_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 5:
                continue
            ref = parts[3].upper()
            alt = parts[4].upper()
            
            # REF 
            if ref == '':
                ref_empty += 1
            elif ref == 'N':
                ref_N += 1
            elif ref == '.':
                ref_dot += 1
            elif ref not in valid_bases:
                ref_invalid_count += 1
            
            # ALT 
            alt_bases = alt.split(',')
            for b in alt_bases:
                if b == '':
                    alt_empty += 1
                elif b == 'N':
                    alt_N += 1
                elif b == '.':
                    alt_dot += 1
                elif b not in valid_bases:
                    alt_invalid_count += 1
    
    with open(output_file, 'w') as out:
        out.write(f"REF bases not A/G/T/C: {ref_invalid_count}\n")
        out.write(f"REF empty (''): {ref_empty}\n")
        out.write(f"REF N: {ref_N}\n")
        out.write(f"REF . : {ref_dot}\n\n")
        
        out.write(f"ALT bases not A/G/T/C: {alt_invalid_count}\n")
        out.write(f"ALT empty (''): {alt_empty}\n")
        out.write(f"ALT N: {alt_N}\n")
        out.write(f"ALT . : {alt_dot}\n")

if __name__ == "__main__":
    
    input_vcf = "../data/checked/henn_filtered1.vcf"
    output_txt = "../data/checked/outputcl.txt"

    check_vcf_simple(input_vcf, output_txt)
    print(f"Analyse terminée. Résultats dans {output_txt}")
