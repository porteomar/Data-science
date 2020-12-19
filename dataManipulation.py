import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183,
           193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178,
           182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages =[57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65,
       52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51,
       54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183,
           193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178,
           182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
# without numpy
cnt = 0
for height in heights:
    if height > 188:
        cnt += 1
print ("There are", cnt, "people taller than 188cm.\n")

# with numpy
heights_arr = np.array(heights) # creates a numpy array from heights
print ("There are", (heights_arr > 188).sum(), "people taller than 188cm.\n")

# get the number of heights in the ndarray (n-dimensional array) heights_arr
# Once an array is created in numpy its size cant change
print("There are", heights_arr.size, "heights in the array\n")

# get the shape of the dimension (the demenion)
# output is a tuple indicating that there is only one dimension
print ("The current shape of heights_arr is", heights_arr.shape, "\n")

# convert a list to a numpy array
heights_and_ages = heights + ages # mashes the 2 arrays together
heights_and_ages_arr = np.array(heights_and_ages) # creates numppy array
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45)) # creates a 2D array of the heights [0] and ages array[1]

print (heights_and_ages_arr, '\n')

# A numpy array is homogeneous: every elem must be the same data type
print("The data type of the numpy array heights_arr:", heights_arr.dtype, '\n')

# If one elem is turned into a float the whole thing is
heights_float_arr = np.array(heights_float)
print(heights_float_arr, '\n')
print("The data type of the numpy array heights_float_arr:", heights_float_arr.dtype, '\n')

# Print the 3rd elem in the numpy array height_arr
print("The height of the third (Thomas Jefferson) president is:", heights_arr[2], "cm", '\n')

# print the age of the third president
print("The age of the third president (Thomas Jefferson) was ", heights_and_ages_arr[1,2], '\n') # heights_and_ages_arr[1,2] row (arr) 1 (2) elem (column) 2 (3)

############
# Slicing #
###########

# Slicing: syntax: "int1 : int2" . select all the numbers from int1 up to but not including int2

print("All of the first 3 heights in the heights and ages array: ", heights_and_ages_arr[0, 0:3], '\n') # can also be written as heights_and_ages_arr[0, :3]

print("The entire 3rd column of the heights and ages array:", heights_and_ages_arr[:,3], '\n') # [height, age]

###########################
# Assigning Single Values #
##########################

# Correcting a single value in the heights_arr
print("Heights array mistake", heights_arr, '\n') # heights_arr[3] = 163
heights_arr[3] = 165
print("Heights array fixed, ", heights_arr, '\n') # heights_arr[3] = 165

# correcting values in a 2D array
print("Heights and age array mistake", heights_and_ages_arr, '\n') # heights_and_ages_arr = 163
heights_and_ages_arr[0,3] = 165
print("Heights and age array fixed", heights_and_ages_arr, '\n') # heights_and_ages_arr = 165

# slicing to change multiple elems
# replacing the entire first row of heights_and_ages_arr with the mean height of 180
heights_and_ages_arr[0,:] = 180
print("heights and ages array with the first row replaces with its mean of 180: ", heights_and_ages_arr, '\n')

# combining slicing to change any subset of the array
# reassign 0 to the left upper corner

heights_and_ages_arr[:2, :2] = 0 # heights[0] and [1] == 0 and ages[0] and [1] == 0 | [:2, :2] = the first to elems of each row
print("heights and ages array with the upper left hand corner set to 0: ", heights_and_ages_arr, '\n')

# you can update both height and age of the first president by supplying the data in a list
heights_and_ages_arr[:,0] = [190,58] # [:,0] = column 0 form each row
print("updating the first presidents height and age with a list",heights_and_ages_arr, '\n')

# data can also be updated in a subarray with a numpy array
new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 42:] = new_record #heights_and_ages_arr[:, 42:] = both rows in the 2D array and elems 42 to the end
print("updating the last 3 elems of the heights and ages array:", heights_and_ages_arr, '\n')

########################
# Combining Two Arrays #
########################

ages_arr = np.array(ages)
print(ages_arr.shape) #  45 column 1D array
print('\n')
# Reshape the heights_arr to be (45,1) like the ages_arr and stack both to horizontally by column to create a 2drray using hstack
ages_arr = ages_arr.reshape((45,1)) # reshape the ages_arr = (45,1)
heights_arr = heights_arr.reshape((45,1)) # reshape the heights_arr = ages_arr
heights_and_ages_arr = np.hstack((heights_arr, ages_arr)) # stacks the the heights_arr and the ages_arr on top of each other to get a 2d arr

print("Uses .hstack to stack the heights and ages array by column (height, ages)" , heights_and_ages_arr[:3,])
print("New shape of the heights_and_ages_arr", heights_and_ages_arr.shape, '\n')

# using vstack to stakc the arrays vertically by row
ages_arr = ages_arr.reshape((1, 45)) # reshape the ages_arr = (1, 45)
heights_arr = heights_arr.reshape((1, 45)) # reshape the heights_arr = ages_arr
heights_and_ages_arr = np.vstack((heights_arr, ages_arr)) # stacks the height and ages array on top of each other vertically by row

print("Uses .vstack to stack the heights and ages array by row (height, ages)" , '\n',heights_and_ages_arr[:,:3])
print("New shape of the heights_and_ages_arr", heights_and_ages_arr.shape, '\n')

################
# Concatenate #
################
# concatenate can be used to link to arrays instead of hstack and vstack

# using contatenate to link array instead of hstack to stack arrays horizontally
ages_arr = ages_arr.reshape((45,1)) # reshape the ages_arr = (45,1)
heights_arr = heights_arr.reshape((45,1)) # reshape the heights_arr = ages_arr
heights_and_ages_arr = np.concatenate((heights_arr, ages_arr), axis = 1)
print("using .concatenate to stack arrays horizontally instead of .hstack", '\n', heights_and_ages_arr[:3, :], '\n')

# using contatenate to link array instead of vstack to stack arrays vertically
ages_arr = ages_arr.reshape((1,45)) # reshape the ages_arr = (45,1)
heights_arr = heights_arr.reshape((1,45)) # reshape the heights_arr = ages_arr
heights_and_ages_arr = np.concatenate((heights_arr, ages_arr), axis = 0)
print("using .concatenate to stack arrays vertically instead of .vstack", '\n', heights_and_ages_arr[:,:3], '\n')

###################################
# doing math operations on arrays #
###################################

# converting the height array from cm to ft
print("Height array converted to Feet\n")
print(heights_arr * 0.0328084) # multiplying by the number of feet in a cm

# summing all the elems in an array using sum()
print("the sum of the heights and ages array is\n", heights_and_ages_arr.sum())

# sum the elems of the height and ages array separately using sum(axis)
# sum(axis=0) computes the sum for each column
# sum(axis=1) computes the sum for each row
heights_arr = heights_arr.reshape((45, 1)) # reshape to have 45 rows and 1 column
ages_arr = ages_arr.reshape((45, 1))
heights_and_ages_arr = np.hstack((heights_arr, ages_arr)) # stacks the two arrays on top of each other
print("The sum of all of the heights in the heights and ages array is\n", heights_and_ages_arr.sum(axis=0))

# Comparisons
# Getting the ages of each president < 55
# can use ==, !=, >=, <=, <, >
# returns an array of booleans

heights_and_ages_arr = np.hstack((heights_arr, ages_arr)) # stacks heights on top of ages
print("All the presidents who are less than 55\n", heights_and_ages_arr[:, 1] < 55) # [:, 1] checks all of the elems in index 1

# check how many rows (number of presidents) satisfy the condition using .sum()
print("There are", (heights_and_ages_arr[:,1] == 55).sum(), "that were 55 years old\n")

# Masking and Subsetting
# Using a mask of boolean values to filter out an array

mask = (heights_and_ages_arr[:,0] >= 182).sum() # all the presidents that are taller than or equal to 182 cm
tall_presidents = heights_and_ages_arr[mask,] # the mask filters out all of the short presidents creating a subarray of the heights and ages array
print("An array of all of the tall preseidents (>= 182cm)", tall_presidents.shape)

