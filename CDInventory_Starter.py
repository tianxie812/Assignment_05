# ------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Tian, 2020-Feb-22, adding deletion part of the code)
# Tian, 2020-Feb-19, Created File
# ------------------------------------------#

# Declare Variables

strChoice = ''  # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}   # dictionary of data row
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

    if strChoice == 'l':
        # Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'Title': lstRow[1], 'Artist Name': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, ' Title': strTitle, 'Artist Name': strArtist}
        lstTbl.append(dicRow)

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep=', ')

    elif strChoice == 'd':
        # Add functionality of deleting an entry
        # Show current inventory
        print('Your current inventory is...')
        print('ID, Title, Artist Name')
        for row in lstTbl:
            print(*row.values(), sep=', ')

	# Enter ID to delete
        deleteID = None
        deleteID = input('Enter an ID to delete: ')
        # Loop thru lstTbl
        for item in range(len(lstTbl)): 
                if lstTbl[item]['ID'] == int(deleteID): 
                    del lstTbl[item]
                break
        # Show inventory after deletion
        print('Your current inventory is now')
        print('ID, Title, Artist Name')
        for row in lstTbl:
            print(*row.values(), sep=', ')
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')