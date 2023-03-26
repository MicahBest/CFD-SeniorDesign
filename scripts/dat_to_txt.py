import os
import csv
import pandas as pd

def dat_to_txt(filename, chord_length):
    """
    This function converts dat information into txt format for use in CAD modeling.
    
    Args:
        - filename : str, name of the file to be converted
        - chord_length : chord_length of the airfoil in any desired units
    """
    
    if filename[-4:] == ".dat":
        filename = filename[:-4]
    
    # read dat information to a list of lists
    datContent = [row.strip().split() for row in open(filename + ".dat").readlines()]

    # write it as a new CSV file
    with open("temp.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(datContent)

    # adding column for z values
    dataframe = pd.read_csv("temp.csv")
    dataframe['z'] = dataframe.apply(lambda z:0.0, axis=1)
    
    idxmax = dataframe['x'].idxmax()
    
    lines = []
    for i in range(len(dataframe)):
        if i <= idxmax:
            row = list(dataframe.loc[i])
        else:
            row = list(dataframe.loc[len(dataframe) - i + idxmax])
        row = [point * chord_length for point in row]
        
        str_row = ""
        for i in range(len(row)):
            str_row += str(row[i]) + " "
        lines += [str_row]
    
    # reorder coordinates for continuity
    with open(filename + ".txt", "w") as f:
        for line in lines:
            f.write(line)
            f.write('\n')
        
    os.remove("temp.csv")
    