
import os
import csv
import json



def get_path(filename):
    curr_dir = os.getcwd()
    file_path = os.path.join(curr_dir, filename)
    return file_path


def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            print(row)


def read_write_csv(file_path):
    reading_file = open(file_path, 'r')
    dialect = csv.Sniffer().sniff(reading_file.readline())
    delim = dialect.delimiter
    fileToWrite = input("Please enter the name of file to write :")
    print("Based on the file size read & write operations may take a little extra time")
    print("We request you to kindly wait.")
    print("Your patience in this regard is much appreciated...")
    print("Thanks...")
    reading_file2 = open(file_path, 'r')
    firstline= reading_file2.readline().split(delim)
    reading_file2.close()
    writing_file = open(fileToWrite, 'wt')
    reader = csv.DictReader(reading_file,fieldnames=firstline,delimiter=delim)
    for row in reader:
        json.dump(row,writing_file)
        writing_file.write("\n")
    writing_file.close()
    reading_file.close()
    print(open(fileToWrite, 'rt').read())


FileToRead = input("Please enter the name of a existing file to read :")
read_write_csv(get_path(FileToRead))
print("Finished printing, please press enter again to exit")
input()
