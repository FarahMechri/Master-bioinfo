#!/bin/bash
sudo apt update
sudo apt install bcftools
mamba create -n  commands
mamba activate commands
cd Téléchargements
cd data
cd Comas_2017
~/Téléchargements/plink --bfile northafrica_syria_filtered --geno 0.05 --mind 0.1 --hwe 0.00001 --maf 0.01 --chr 1-22 --make-bed --out output
cd ..
cd Henn2012
cd NAfrica_Bas
~/Téléchargements/plink --bfile NAfrica_Bas --geno 0.05 --mind 0.1 --hwe 0.00001 --maf 0.01 --chr 1-22 --make-bed --out output
cd..
cd..
cd Anagnostu_2020
~/Téléchargements/plink --bfile Tunisia_dataset --geno 0.05 --mind 0.1 --hwe 0.00001 --maf 0.01 --chr 1-22 --make-bed --out output
cd ..
cd Comas_2017
~/Téléchargements/plink --bfile comas --recode vcf-iid --out vcf_file
cd ..
cd Anagnostu_2020
~/Téléchargements/plink --bfile anagnostu --recode vcf-iid --out vcf_file
cd ..
cd Henn2012
cd NAfrica_Bas
~/Téléchargements/plink --bfile henn --recode vcf-iid --out vcf_file
cd ..
cd ..

