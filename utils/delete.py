import sys
import os
import shutil

image_fullpath=sys.argv[1]
image_fullpath = image_fullpath[1:]
format = image_fullpath[-3:]

if(format == "jpg"):
  if os.path.exists(image_fullpath):
      os.remove(image_fullpath)
      shutil.rmtree(f"{image_fullpath[:-4]}_grid")
      os.remove(f"{image_fullpath[:-4]}_grid.jpg")
      os.remove(f"{image_fullpath[:-4]}_grid_help.jpg")
      print("Remove")
  else:
    print("The file does not exist")
else:
  if os.path.exists(image_fullpath):
      os.remove(image_fullpath)
      shutil.rmtree(f"{image_fullpath[:-4]}_grid_red")
      os.remove(f"{image_fullpath[:-4]}_grid.png")
      os.remove(f"{image_fullpath[:-4]}_grid_red.jpg")
      os.remove(f"{image_fullpath[:-4]}.zip")
      print("Remove")
  else:
    print("The file does not exist")