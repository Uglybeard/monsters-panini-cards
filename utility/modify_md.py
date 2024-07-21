import os

folder_path = '../cards'

file_names = [f for f in os.listdir(folder_path) if f.endswith('.md')]

def modify_files(file_names, folder_path):
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        name=file_name.split(".")[0]
        modified_name=name.replace(" ","-")
        name=name.capitalize()
        
        new_content = f"# {name}\n\n![](../images/{modified_name}.jpg)\n"
        
        with open(file_path, 'w') as file:
            file.write(new_content)

modify_files(file_names, folder_path)
