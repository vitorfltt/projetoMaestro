import os

def join_files(output_file, part_files):
    with open(output_file, 'wb') as outfile:
        for part in part_files:
            with open(part, 'rb') as infile:
                outfile.write(infile.read())

if __name__ == "__main__":
    part_files = ["part_aa", "part_ab", "part_ac"]  # Adicione todas as partes aqui na ordem correta
    output_file = "app-casa_reconstructed.apk"
    join_files(output_file, part_files)
    print(f"Arquivo reconstruído: {output_file}")