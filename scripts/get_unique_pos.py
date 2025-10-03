import csv

# Input and output file paths
input_file = "lexicon/dataset.csv"
output_file = "results/unique_pos.txt"

# Store unique items
unique_pos = set()

with open(input_file, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header (first row)

    for row in reader:
        if len(row) >= 4:  # check if 4th column exists
            unique_pos.add(row[3].strip())

# Write unique values to a new file
with open(output_file, "w", encoding="utf-8") as f:
    for item in sorted(unique_pos):
        f.write(item + "\n")

print(f"✅ Done! Found {len(unique_pos)} unique values in column 4.")
print(f"Results saved in {output_file}")
