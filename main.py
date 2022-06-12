LETTER_FILE_PATH = "./Input/Letters/starting_letter.txt"
OUTPUT_FOLDER = "./Output/ReadyToSend/letter_for_"
RECEIVER_NAME_PLACEHOLDER = "[name]"
SENDER_NAME_PLACEHOLDER = "Angela"
SENDER_NAME = "te acha"
NAMES_FILE = "./Input/Names/invited_names.txt"


with open(LETTER_FILE_PATH, "r") as letter_file:
    sample_letter = letter_file.readlines()

with open(NAMES_FILE, "r") as name_file:
    names = name_file.readlines()

for name in names:
    name = name.strip()
    output_file_name = OUTPUT_FOLDER + name + ".txt"
    output_file = open(output_file_name, "w")
    for lines in sample_letter:
        lines = lines.strip()
        lines = lines.replace(RECEIVER_NAME_PLACEHOLDER, name)
        lines = lines.replace(SENDER_NAME_PLACEHOLDER, SENDER_NAME)
        lines = lines + "\n"
        output_file.write(lines)
    output_file.close()
