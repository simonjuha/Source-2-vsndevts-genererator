import os

# set your relative directory of sound files folder
directory = 'sounds/foldername'

# set your relative location for .vsndevts file to write to
vsndevts = 'soundevents/writeme.vsndevts'

# last folder with files will be category name
folder = directory.split('/')[-1]

# first line
content = "<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->\n{\n"

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        content += '\t'+folder+'.'+f.split('\\')[1].split('.')[0]+' =\n \t{\n\t\t type = "hlvr_default_3d"\n\t\t volume = 1.000000\n\t\t use_hrtf = 1.000000\n\t\t vsnd_files = ["'+f.split('.')[0]+'.vsnd",]\t\n\t}\n\n'

# write 
content = content.replace('\\', '/') # fix slashes
content += "}"
f = open(vsndevts, "w")
f.write(content)
f.close()