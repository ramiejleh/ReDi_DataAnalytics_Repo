You will find the hints below!

# Files you will need for the homework and exercises
For the exercises, you will need:
1 The notebook called exercise.ipynb
2 The CSV file called pension_fund_data.csv

For the homework, you will need:
1 The notebook called homework.ipynb
2 The CSV file called legosets.csv

For the optional homework, you will also need themes.csv
\
\
\
\


Scroll down for hints...
\
\
\
\
\
\
\
\
\
\
\
\

# Hints
## Lego homework
#### all_pieces:
Add all row entries for the number of pieces to a variable.

#### year_most:
Create a list with just the release year of every set. Then iterate over the set of this list (a Python set is much like a set in mathematics;  it works almost like a Python list but  it does not allow duplicates),  and check whether that year had more sets released than the year before.  But remember,  it is the year, not the number of sets, that is the information we want!
You can also use Counter from the collections module for this task.

#### average_pieces:
You can use some of the work you've already done for this task.

#### most_used_word:
You can use an approach similar to the one for year_most.  However, if you use iteration, It can be a bit tricky because the most common occurence may not be a word.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\

## Hints for the pension fund exercise:

### First hints

#### Remove any wrong or odd row entries:
There is something in the dataset that definetely doesn't belong there. You won't have any doubt about it when you find it.

#### Read the file into memory:
Remember that you will have to iterate over the csv.reader object when assigning the content of the file to a variable.

#### Remove 'company_name:'. 
You can do this by making your own helper function or use a built-in function.

#### Write the nice and clean data to another CSV file.
Using csv.reader object won't work this time.

#### Format the invested sums
Use helper functions to make sure the formatting is correct.
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
### Second hints:

#### Remove any wrong or odd row entries:
There is one row that definetely does not belong in the dataset. Find all the different names of the pension funds that occur in column 1, and you will find it.

#### Read the file into memory:
You have to create a csv.reader object, then add each element of the object to a list. You can also have a look at Realpython that has a good guide on CSV files: https://realpython.com/python-csv/

#### Remove 'company_name:'. 
Create a helper function that turns the column entry into a list using the strip method, then remove 'company_name' from the list, and return it as a string. You can also use the built-in replace function.

#### Write the nice and clean data to another CSV file.
csv.reader objects are only for reading files. You'll have to use the csv.writer object instead.  The Realpython guide mentioned above can help you with this as well.

#### Format the invested sums
Write two helper functions, one for AkademikerPension and one for Industriens Pension. They should both take the invested sum as an input, but the function body should then format the sum correctly and return the correct sum. You can then either use if-statements in your loop to check which helper function to use or create another helper function that first checks which helper function to use, then uses this helper function to format the sum, and finally returns the correctly formatted sum to the main loop. 
