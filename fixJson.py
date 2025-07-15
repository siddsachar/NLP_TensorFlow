input_file = "Sarcasm_Headlines_Dataset_v2.json"
output_file = "Sarcasm_Headlines_Dataset_v2_fixed.json"

with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith("//")]

with open(output_file, "w", encoding="utf-8") as f:
    f.write("[\n")
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            f.write(line.rstrip(",") + ",\n")
        else:
            f.write(line.rstrip(",") + "\n")
    f.write("]\n")