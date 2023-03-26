import os
import csv
import pandas as pd

def dat_to_csv(filename, chord_length):
    """
    This function converts dat information into csv format for use in CFD modeling.
    
    Args:
        - filename : str, name of the file to be converted
        - chord_length : chord_length of the airfoil in any desired units
    """
    
    if filename[-4:] == ".dat":
        filename = filename[:-4]
    
    # read dat information to a list of lists
    datContent = [row.strip().split() for row in open(filename + ".dat").readlines()]

    # write it as a new CSV file
    with open(filename + ".csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(datContent)

    # adding column for z values
    dataframe = pd.read_csv(filename + ".csv")
    dataframe['z'] = dataframe.apply(lambda x:0.0, axis=1)
    dataframe.to_csv(filename + ".csv", index=False, header=False)
    
    idxmax = dataframe['x'].idxmax()
    
    os.remove(filename + ".csv")
    
    # reorder coordinates for continuity
    with open(filename + ".csv", "w") as f:
        writer = csv.writer(f)
        for i in range(len(dataframe)):
            if i <= idxmax:
                row = list(dataframe.loc[i])
            else:
                row = list(dataframe.loc[len(dataframe) - i + idxmax])
            writer.writerow([point * chord_length for point in row])
    