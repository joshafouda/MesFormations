# Fonction pour lire le programme de la formation à partir d'un fichier Markdown
def read_description(description_file):
    with open(description_file, 'r', encoding='utf-8') as file:
        return file.read()