"""file utility"""
import csv

def read(filename):
    """Reads a file and returns a list of lines"""
    with open(filename, encoding="utf-8") as file:
        lines = [line.strip() for line in file]
    return lines

def write(data, filename):
    """Writes a list of lines to a file"""
    with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

def convert(lines, timeseparator="-->"):
    """Converts a list of lines to a list of lists"""
    data = []
    item = []
    count = 0
    for line in lines:
        if timeseparator in line:
            count = 0
            row = line.split(timeseparator)
            item = []
            item.append(row[0].strip())
            item.append(row[1].strip())
        else:
            count += 1
            item.append(line)
            if count == 2:
                data.append(item)
    return data
