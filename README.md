# launch.py
A python import of Darwin's launch.h

# Example

```python
from launch import *

#prepare msg
daemon_name = launch_data_new_string(b"com.apple.geod")
msg = launch_data_alloc(LAUNCH_DATA_DICTIONARY)
launch_data_dict_insert(msg, daemon_name, LAUNCH_KEY_GETJOB)

#send msg
res = launch_msg(msg)
_program_path = launch_data_dict_lookup(res, LAUNCH_JOBKEY_PROGRAM)
program_path = launch_data_get_string(_program_path)
print(program_path) #should print the path of the program that the daemon runs

#free memory
launch_data_free(msg)
launch_data_free(res)

```

# Important notes
+ This is a direct import of launch.h, so the user must handle the memory management.
+ Be careful with what to free and what to NOT free.
