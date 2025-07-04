#!/bin/bash
DATA_DIR="../data"
OUT_DIR="../data/vcf"
mkdir -p "$OUT_DIR"

LOG_FILE="${OUT_DIR}/log_conversion.txt"
> "$LOG_FILE"
echo "./conversion_vcf.sh" >> "$LOG_FILE"

for prefix in comas henn anagnostu
do
    echo "Conversion de $prefix en vcf"
    echo "Conversion de $prefix en vcf" >> "$LOG_FILE"
    plink --bfile "${DATA_DIR}/$prefix" --recode vcf --out "${OUT_DIR}/${prefix}">> "$LOG_FILE" 2>&1
done

echo "done"
echo "done" >> "$LOG_FILE"
