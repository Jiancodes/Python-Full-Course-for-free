# copyfile() = copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copy2('test.txt','C:\\Users\\MengJian\\Desktop\\Python_Full_Course_for_free\\copy.txt') #src.dst