import os
def rename_files():
  file_list = os.listdir(r"/Users/jerwodke/Desktop/prank")
  saved_path = os.getcwd()
  os.chdir(r"/Users/jerwodke/Desktop/prank")

  for file_name in file_list:
    os.rename(file_name, file_name.translate(None, "0123456789"))
    print(file_name+" has been changed")
  os.chdir(saved_path)
rename_files()

              
