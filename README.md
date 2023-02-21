# CFD-SeniorDesign
This repository will contain any scripts that will assist in CFD simulations. It will also contain a folder to store all of our airfoil data.

## Airfoil Database
The airfoil data .dat files can be found in the [UIUC Airfoil Data Site](https://m-selig.ae.illinois.edu/ads/coord_database.html).
To use the .dat file, download and place the file in the Airfoils/ directory in the repository and access this file from the conversion function.

## Instructions for Use
In Ubuntu Terminal, navigate to the desired destination directory using `cd` commands. If the C:/ drive is desired, use the following commands:
```
cd ~/../../mnt/c/
```
Use this command once to clone the GitHub repository:
```
git clone git@github.com:MicahBest/CFD-SeniorDesign.git
```

To pull recent commits and update the scripts, use the following command:
```
git pull
```

## Running the python script to convert 2D airfoil data from dat to csv
Set the filename in the bottom of the script then run the following command from the base directory of the repository in Ubuntu:
```
python3 scripts/2D_airfoil_dat_to_csv.py
```
