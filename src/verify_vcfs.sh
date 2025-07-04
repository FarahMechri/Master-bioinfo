#!/bin/bash

GENOME="../data/Homo_sapiens.GRCh37.dna.chromosome.1.fa"
VCF_DIR="../data/vcf"
OUTPUT_DIR="../data/checked"
STATS_DIR="../data/stats"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$STATS_DIR"

#genome_indexed
if [ ! -f "${GENOME}.fai" ]; then
    echo "Indexation du génome avec samtools..."
    samtools faidx "$GENOME"
fi

FILES=("comas.vcf" "henn.vcf" "anagnostu.vcf")

for vcf in "${FILES[@]}"; do
    input_file="${VCF_DIR}/${vcf}"
    base_name=$(basename "$vcf" .vcf)
    output_file="${OUTPUT_DIR}/${base_name}_checked.vcf"
    stats_file="${STATS_DIR}/${base_name}_stats.txt"

echo "🧬 Execution for $input_file"
    python3 check_and_fix_vcf.py "$input_file" "$GENOME" "$output_file" "$stats_file"

    echo "✅ done :"
    echo "   - corrected vcf : $output_file"
    echo "   - filtred vcf  : ${output_file/_checked.vcf/_filtered.vcf}"
    echo "   - Statistics : $stats_file"
done

echo "🎉 cleansing done "
                        
