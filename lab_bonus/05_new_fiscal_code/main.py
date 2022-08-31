import argparse as ap
from person import Person as FC

if __name__ == '__main__':
    # read the file name from CLI
    parser = ap.ArgumentParser(description='script that get a file path and check for correct fiscal code in the file')
    parser.add_argument('path', type=str, help='enter the path of the file')
    path = parser.parse_args().path