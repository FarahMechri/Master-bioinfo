#!/usr/bin/env python3
import random
import os 
input_dir = "/home/farah/Bureau/bioinfo/data/checked"
output_dir = "/home/farah/Bureau/bioinfo/data/checked/sampling_output"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith("_filtered.vcf"):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, "sample_" + file)



        with open(input_path, 'r') as infile:
           lines = infile.readlines()


        header = [line for line in lines if line.startswith('#')]
        data = [line for line in lines if not line.startswith('#')]


        sample_size = int(0.75 * len(data))
        sampled_data = random.sample(data, sample_size)


        with open(output_path, 'w') as outfile:
           outfile.writelines(header + sampled_data)
        print(f"done for {input_path} -> {output_path}")
