import os
import glob


def main():
    print('Which file names do you want to search for?')
    file_name = input() or '*'
    print('Which file names do you want to search for?')
    file_extension = input() or '*'
    files_list = find_files(file_name, file_extension)
    write_to_txt(files_list)


def find_files(file_name='*', file_extension='*'):
    files_list = glob.glob(f"**/{file_name}.{file_extension}", recursive=True)
    return files_list


def write_to_txt(files_list):
    cwd = os.getcwd()
    output_file_name = os.path.basename(cwd) + '_file_list'
    print(output_file_name)
    with open(output_file_name + '.txt', 'w+') as f:
        for item in files_list:
            f.write(item + '\n')
    f.close()


if __name__ == "__main__":
    main()
