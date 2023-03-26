import argparse
from dat_to_csv import dat_to_csv
from dat_to_txt import dat_to_txt

parser = argparse.ArgumentParser()
parser.add_argument("airfoil")
parser.add_argument("chord_length", type=float)

args = parser.parse_args()

filename = "airfoils/" + args.airfoil
chord_length = args.chord_length

dat_to_csv(filename, chord_length)
dat_to_txt(filename, chord_length)