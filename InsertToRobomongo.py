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


def del_none(d):
    dup=d.copy()
    for key, value in d.items():
        if(value is None)or(value is '')or(value is ""):
            del dup[key]
        elif isinstance(value, dict):
            del_none(value)
    return (dup)


def read_write_csv(file_path):
    reading_file = open(file_path, 'r')
    dialect = csv.Sniffer().sniff(reading_file.readline())
    delim = dialect.delimiter
    fileToWrite = input("Please enter the name of file to write :")
    writing_file = open(fileToWrite, 'wt')
    reading_file2 = open(file_path, 'r')
    firstline= reading_file2.readline().split(delim)
    print(firstline)
    reading_file2.close()
    reader = csv.DictReader(reading_file,fieldnames=firstline,delimiter=delim)
    for row in reader:
        json.dump(row,writing_file)
        writing_file.write("\n")
    writing_file.close()
    writing_file2 = open(fileToWrite)
    from pymongo import MongoClient
    client = MongoClient('50.84.62.186', 27017)
    db=client.annt
    db.authenticate ("annt","5r4ShV7Z")
    collection=db.nuthan
    for line in writing_file2:
        record = json.loads(str(line))
        purifiedRecord=del_none(record)
        collection.insert(purifiedRecord)
        
    fecthed=collection.find()
    for line in fecthed:
        print(line.keys())
    writing_file2.close()
    reading_file.close()
    print(open(fileToWrite, 'rt').read())



FileToRead = input("Please enter the name of a existing file to read :")
read_write_csv(get_path(FileToRead))
print("Finished printing, please press enter again to exit")
input()

