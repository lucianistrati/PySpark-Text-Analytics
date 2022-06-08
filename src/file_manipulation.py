rows = []

def split():
	with open("data/biographies.list", "r", errors='ignore') as f:
		lines = f.readlines()
		for line in lines:
			rows.append(line)
	num_lines = len(rows) // 30
	for i in range(30):
		with open(f"data/multiple_datasets/biographies_{i}.list", "w") as f:
			for text in rows[i * num_lines: i * (num_lines + 1)]:
				f.write(text + "\n")
	
		


def merge():
	pass

split()
#merge()
