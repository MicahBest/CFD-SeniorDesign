# CFD-SeniorDesign
This repository will contain any scripts that will assist in CFD simulations. It will also contain a folder to store all of our airfoil data.

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

## Running the python script to convert 2D airfoil data
Run the following command from the base directory of the repository in Ubuntu:
```
python3 scripts/convert_airfoil.py naca0012 5.0
```

The command line takes 2 extra arguments: the first is the airfoil name and the second is the chord length.
The airfoil will be automatically converted to csv and txt files for CFD and CAD analysis.

## Airfoil Database
The airfoil data .dat files can be found in the [UIUC Airfoil Data Site](https://m-selig.ae.illinois.edu/ads/coord_database.html).
To use the .dat file, download and place the file in the airfoils/ directory in the repository and access this file from the conversion function.

## Airfoil Generator
Airfoils can be generated in the [Airfoil Tools Website](http://airfoiltools.com/airfoil/naca4digit).
