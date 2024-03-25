# Importing modules 
from tabulate import tabulate
import sys
from sub import generator
import datetime

# Initiating variables
rows = 0
cols = 0 
SizeOfGrid = ""
matrix = []
listRow =[]
tempMatrix = []
templist = []
statusList = []
html_name = ""
file_name = ""
TimeNow = ""

# Geting input from the user and creating a 5x5 grid if no commands are passed
if len(sys.argv) > 1:
       SizeOfGrid = sys.argv[1]
else:
    SizeOfGrid = "5x5"

# Dividing the single argument into two elements so that we can check if the size of the grid is in the permitted range
SizeOfGrid = SizeOfGrid.split("x")
rows = int(SizeOfGrid[0])
cols = int(SizeOfGrid[1])

# Checking if the size of the grid is in the permitted range
if rows < 3 or cols < 3:
    print ("The number of rows and columns must be greater than or equal to 3 ")
    exit()
elif rows > 9 or cols > 9:
    print ("The number of rows and columns must be lesser than or equal to 9")
    exit()

# If the input is valid,
else:
    # Generating random numbers
    from sub import generator
    generator()

    # Creating the and adding values into the matrix
    matrix =[]
    for a in range(rows):
        listRow =[]
        for i in range(cols):            
            listRow.append(generator())
        matrix.append(listRow)    

    tempMatrix = []

    for rw in range(cols):
        templist = []
        for r in matrix:
            templist.append(r[rw])
        tempMatrix.append(templist)

    # Generating the status     
    statusList = [] 
    for rw in tempMatrix:
        status = "OK"
        for val in rw:
            if val == "":
                status = "NO"
        statusList.append(status)
        
    matrix.append(statusList)

    # Displaying the output of the created grid
    print(tabulate(matrix, tablefmt = "fancy_grid"))

    # Generating the text and html files
      
    # Getting the current time
    import datetime
    TimeNow = datetime.datetime.now()

    # Generate html file name using the current time
    html_name = 'Html ' + str(rows)+"x"+str(cols)  +TimeNow.strftime(' %H-%M-%S') + '.html'

    # Writing to the newly created html file
    with open (html_name, "w") as f:
        f.write(tabulate(matrix, tablefmt = "html"))
    
    # Generate file name using the current time
    file_name = 'Sample ' + str(rows)+"x"+str(cols)  +TimeNow.strftime(' %H-%M-%S') + '.txt'

    # Writing to the newly created file
    with open(file_name, 'w') as f:
        f.write(tabulate(matrix,tablefmt='txt'))

    