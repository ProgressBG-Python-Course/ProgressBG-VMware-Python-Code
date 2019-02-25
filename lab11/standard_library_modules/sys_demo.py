import sys
import os

mylib_path = os.path.join(os.environ['PROJECT_PATH'], '_custom_functions')
sys.path.append(mylib_path)
from custom_functions import preaty_print as iep_pp


iep_pp("sys.executable: ", sys.executable)
iep_pp("sys.version: ", sys.version)
iep_pp("sys.version_info: ", sys.version_info)
iep_pp("sys.path: ", sys.path)
