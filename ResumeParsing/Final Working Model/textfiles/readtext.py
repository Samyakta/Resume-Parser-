#reads and gives output of all text files present in the directory 
import os

path = "C:\\Users\\Admin\\OneDrive\\Desktop\\C Programming\\mydirectory\\Final Working Model\\textfiles"

os.chdir(path)

# Read text File


def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}\{file}"

		# call read text file function
		read_text_file(file_path)
