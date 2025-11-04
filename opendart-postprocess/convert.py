from weasyprint import HTML
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python convert.py <input.html> <output.pdf>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    sys.exit(1)

print(f"Converting {input_file} → {output_file} ...")
HTML(input_file).write_pdf(output_file)
print("✅ PDF conversion complete.")
