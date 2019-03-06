import os

data_entries = os.listdir( os.path.join(os.getcwd(),'data') )
print(data_entries)

cwd = os.getcwd()

os.rename( os.path.join(cwd,"data/Test"), os.path.join(cwd,"data/Test".lower()) )

# for entry in data_entries:
#   os.rename( entry, entry.lower() )