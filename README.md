# README

#### by Juju_Beans  
---
**Project:** Hurricane Analysis  

**Objective:**

Use fundamental knowledge of Python to organize and process the data of 34 different hurricanes in order to find solutions for nine different tasks.

**Results:**  

Created `my_solutions.py`.

For comparative review see `provided_solutions.py`. Please mind the slight changes to task objectives as noted at the bottom of the file.

---

**Task 1**   
Use a conversion table to return a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".

**Task 2**  
Construct a dictionary named hurricanes so that its keys are the names of the hurricanes, and its values are dictionaries made from the lists:
*  Name
*  Month
*  Years
*  Max Sustained Wind
*  Areas Affected
*  damages
*  death

**Task 3**  
Code a function that converts the hurricanes dictionary to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.

**Task 4**  
Code a function that creates a dictionary where the keys are the affected areas, and the values are counts of how many times that area was affected.

**Task 5**  
Using the hurricanes dictionary, code a function that finds the area hit by the most hurricanes, and returns that area's name and how often it was hit.

**Task 6**  
Using the hurricanes dictionary, code a function that returns the hurricane that had the highest mortality stats, and how many deaths it caused.

**Task 7**  
Using the hurricanes dictionary, code a function that rates hurricanes on a mortality scale and also returns a dictionary where the keys are mortality ratings and the __values__**(see below) are lists containing a dictionary for each hurricane that falls into that mortality rating.

**Task 8**  
Code a function that returns the hurricane that caused the greatest damage as well as just how costly it was in USD.

**Task 9**  
Using the hurricanes dictionary, code a function that rates hurricanes on a damage scale. Have it return a dictionary where the keys are damage ratings and the __values__**(see below) are lists containing a dictionary for each hurricane that falls into that mortality rating.

---
__values__**: (Task 7 & Task 9 ) altered code to return onl7 hurricane name as value in dictionary instead of the entire metadata associated hurricane with relavent hurricane.
