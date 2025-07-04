#!/bin/bash

POPDECAY="/home/farah/PopLDdecay/bin/PopLDdecay"
PLOT="/home/farah/PopLDdecay/bin/Plot_OnePop.pl"
VCF_DIR="../data/checked/sampling_output"


OUTDIR="../data/checked/LD_results1"
mkdir -p "$OUTDIR"

# Paramètres LD decay
MAXDIST=300
MAF=0.05

# Liste des fichiers (sans extension)
FILES=("sample_anagnostu_filtered" "sample_comas_filtered" "sample_henn_filtered")

# Boucle sur chaque fichier
for FILE in "${FILES[@]}"; do
    echo "➡️  execution : $FILE.vcf.gz"

 # Lancement de PopLDdecay
    $POPDECAY -InVCF "$VCF_DIR/$FILE.vcf.gz" -OutStat "$OUTDIR/${FILE}_LD" -MaxDist $MAXDIST -MAF $MAF

    # Tracé de la courbe avec le script Perl
    perl "$PLOT" -inFile "$OUTDIR/${FILE}_LD.stat.gz" -output "$OUTDIR/${FILE}_LD_plot"

    echo "✅ done for  $FILE"
done

echo "🎉 done !"
