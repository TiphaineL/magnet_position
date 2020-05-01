# magnet_position

Change the file input in line 12 of main.py and run main.py

Parameters (such as the size of the robot arm, etc...) can be modified in hector > constants.py 

If the file structure is modified, this is handed in problem_opereations > extract_data.py, in the function 
create_list_of_probes_from_file(file) 

---

When ran, main.py returns:

conflicted_magnet: a list of objects, with parameters: 
conflicted_magnet.blocking_magnet  # the blocking magnet 
conflicted_magnet.conflicted_magnet   # the blocked magnet 
conflicted_magnet.pickup_area      # the pickup area that is blocked 

fully_blocked_magnets: a list of objects which are the magnets being fully blocked

positioning array: an array containing all the magnets (1st column: magnet type, 2nd column: magnet number), with their ordering number on the third column (1: positioned first, 2: positioned 2nd etc) and a list of available pickup areas (the ones that aren't blocked by other magnets). See overleaf documentation for the nomenclature.

The array can be saved into a file.




