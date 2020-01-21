# magnet_position

Change the file input in line 10 of main.py and run main.py - 
Parameters (such as the size of the robot arm, etc...) can be modified in hector > constants.py - 
If the file structure is modified, this is handed in opereations > extract_data.py, in the function 
create_list_of_probes_from_file(file) ---

When ran, main.py returns a list of objects: blocked_magnet -
with parameters: -
blocked_magnet.blocking_magnet  # the blocking magnet -
blocked_magnet.blocked_magnet   # the blocked magnet -
blocked_magnet.pickup_area      # the pickup area that is blocked -
