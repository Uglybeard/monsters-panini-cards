import re

pattern = r'https:\/\/resized-image\.uwufufu\.com\/worldCupSelection\/\d+\/original\/[\w%]+\.jpg'

def find_matches(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    matches = re.findall(pattern, content)
    return matches

def remove_duplicates(matches):
    return list(set(matches))

# Funzione per scrivere l'output in un file
def write_output(matches, output_file_path):
    with open(output_file_path, 'w') as file:
        for match in matches:
            file.write(match + '\n')

file_path = 'uwufufu.txt'
output_file_path = 'cards.txt'

matches = find_matches(file_path)
unique_matches = remove_duplicates(matches)

write_output(unique_matches, output_file_path)

print(f"Found {len(unique_matches)} unique matches.")
