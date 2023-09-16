"""Converts a file from txt to csv format"""
from util.file import read, convert, write
import settings

def main():
    """Main function"""
    lines = read(settings.INPUT_FILE)
    data = convert(lines)
    write(data, settings.OUTPUT_FILE)

if __name__ == "__main__":
    main()
