import csv
import pandas as pd

def convert_2D_airfoil_dat_to_csv(filename):
    """
    This function converts dat information into csv format for use in CFD modeling.
    
    Args:
        - filename : str, name of the file to be converted
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
    
    # reorder coordinates for continuity
    with open(filename + ".csv", "w") as f:
        writer = csv.writer(f)
        for i in range(len(dataframe)):
            if i <= idxmax:
                writer.writerow(list(dataframe.loc[i]))
            else:
                writer.writerow(list(dataframe.loc[len(dataframe) - i + idxmax]))
    

if __name__ == "__main__":
    convert_2D_airfoil_dat_to_csv(filename="Airfoils/n0012")
    