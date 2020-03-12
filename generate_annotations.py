import re
import sys
import csv

sample_file = sys.argv[1] # Words to annotate
data_file = sys.argv[2] # Complete file
entity_type = sys.argv[3] # Custom entity annotation

strings_to_annotate = []

output_file_name = f"{entity_type}_annotated.csv"
output_header = "File", "Line", "Begin Offset", "End Offset", "Type"

def read_sample_file():
	print(f"Reading file {sample_file}...")
	for line in open(sample_file, 'r'): 
		strings_to_annotate.append(line.strip())

def process_data_file():
	write_row(output_header, 'w')
	regex = re.compile(r'\b(' + '|'.join(strings_to_annotate) + r')\b')
	print(f"Reading data file {data_file}...")
	with open(data_file, 'r') as data:
		for line_num, line in enumerate(data, start=0):
			print("Processing line {}: {}".format(line_num, line))
			for match in regex.finditer(line):
				print("Annotated phrase '{}' in pos. {}-{}".format(match.group(0), match.start(), match.end()))
				write_annotation_to_file(line_num, match.start(), match.end())

def write_annotation_to_file(line_num, offset_start, offset_end):
	write_row([sample_file, line_num, offset_start, offset_end, entity_type], 'a')

def write_row(row, open_action):
	with open(output_file_name, open_action, encoding="utf-8") as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(row)

read_sample_file()
process_data_file()
print("Done!")