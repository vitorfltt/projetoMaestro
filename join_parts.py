import os

def join_files(output_file, part_files):
    with open(output_file, 'wb') as outfile:
        for part in part_files:
            with open(part, 'rb') as infile:
                outfile.write(infile.read())

if __name__ == "__main__":
    part_files = ["part_aa", "part_ab", "part_ac","part_ad","part_ae","part_af","part_ag","part_ah"]
    output_file = "app-casa_reconstructed.apk"
    join_files(output_file, part_files)
    output_file_path = os.path.abspath(output_file)
    print(f"Arquivo reconstruído: {output_file}")
    print(f"Caminho completo do arquivo: {output_file_path}")