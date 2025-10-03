import csv

def clean_csv(input_file: str, output_file: str):
    issues = []  # to collect rows with >4 columns

    with open(input_file, newline='', encoding="utf-8") as inf, \
         open(output_file, "w", newline='', encoding="utf-8") as outf:
        reader = csv.reader(inf)
        writer = csv.writer(outf)

        for row_num, row in enumerate(reader, start=1):
            if len(row) == 3:
                # Add empty 4th column
                row.append("")
            elif len(row) == 4:
                # Strip commas inside the last column
                row[3] = row[3].replace(",", " ").strip()
            elif len(row) > 4:
                # More than 4 columns — log the problem
                issues.append((row_num, row))
                # Try to merge everything after the 3rd column into one string
                row = row[:3] + [",".join(row[3:])]
            # else if less than 3, don't touch (rare case)

            writer.writerow(row)

    print(f"✅ Cleaned file saved as: {output_file}")
    if issues:
        print("⚠️ Found rows with more than 4 columns (possible manual review needed):")
        for rnum, rdata in issues:
            print(f"  Line {rnum}: {rdata}")

# Example usage:
clean_csv("lexicon/dataset.csv", "lexicon/dataset_clean.csv")
