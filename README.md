# DSCI560-HW2

### Description: create three different scripts to perform the following tasks
- Generate 1000 random numbers over the range 0-100 
- Generate new numbers from the original 1000 using the equation y=3x+6 
- Visualize the results 

### Script files and Jupyther notebook file
- random_number.py
- equation.py 
- data.py
- hw2.ipynb

### Output files
- random_number.txt
- equation.txt
- data.jpg

### Run code in command line and follow this order
``` 
python3 random_number.py
python3 equation.py 
python3 data.py
```

### DOI
[![DOI](https://zenodo.org/badge/296792546.svg)](https://zenodo.org/badge/latestdoi/296792546)

### Visualization result
![data](https://user-images.githubusercontent.com/56018075/94214214-c9efc800-fe8d-11ea-9611-30e2515a2383.jpg)


# DSCI560-HW4

## Create a virtual environment for my GitHub project and execute it step by step

### step 1: Clone hw2 from GitHub
- `git clone https://github.com/jieqiong-pang/DSCI560-HW2.git`

### step 2: Create a blank virtual environment and name it dsci560H4 in this clone file
- `pip install virtualenv`
- `virtualenv dsci560H4`

![data](https://user-images.githubusercontent.com/56018075/97099766-e8421280-1649-11eb-8b80-e47f8b6f3e86.png)

### step 3: Activate the environment and install ONLY the dependencies to execute the random number generator script of Homework 2
- activate the environment `source dsci560H4/bin/activate`
- don't need to install any dependency for number generator script becasue it doesn't use any extra package

### step 4: Running the script for the number generator
- `python3 random_number.py`

### step 5: Compare the packages that I manually installed versus the dependency list I extracted
- before install, `pip freeze > requirements.txt`, the requirements.txt is empty
- after install, `pip install numpy`, `pip install matplotlib`, `pip freeze > requirements.txt`, the following has been added to the requirements.txt file

### step 6: Add the environment folder to a “.gitignore” file 
- create “.gitignore” file using command line `touch .gitignore`
- edit “.gitignore” file using command line `vim .gitignore`

### step 7: Upload your extracted dependencies 
- use GitHub Descktop application to upload extracted dependencies to github
