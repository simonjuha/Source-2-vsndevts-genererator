import os
import wave

# set your relative directory of sound files folder
directory = 'sounds/'

# set your relative location for .vsndevts file to write to
vsndevts = 'soundevents/writeme.vsndevts'

# first line
content = "<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->\n{\n"

# iterate over subdirectories in
# the sounds/ directory
for subdir in os.listdir(directory):
    # construct the full path of the subdirectory
    subdir_path = os.path.join(directory, subdir)
    # check if the subdirectory is actually a directory
    if os.path.isdir(subdir_path):
        # iterate over files in the subdirectory
        for filename in os.listdir(subdir_path):
            f = os.path.join(subdir_path, filename)
            # checking if it is a file
            if os.path.isfile(f):
                # check if the file is a .wav file
                if f.endswith('.wav'):
                    # open the .wav file and read its sampling rate
                    with wave.open(f, 'rb') as wav_file:
                        sampling_rate = wav_file.getframerate()
                        if sampling_rate != 44100:
                            # write a warning to the console
                            print(f'Warning: {f} has sampling rate {sampling_rate}, expected 44100')
                        # pair the filename with the subdirectory name using '.'
                        content += '\t' + subdir + '.' + f.split('\\')[1].split('.')[0] + ' =\n \t{\n\t\t type = "hlvr_default_3d"\n\t\t volume = 1.000000\n\t\t use_hrtf = 1.000000\n\t\t vsnd_files = ["' + f.split('.')[0] + '.vsnd",]\t\n\t}\n\n'
                else:
                    # write a warning to the console
                    print(f'Warning: {f} is not a .wav file, skipping')

# write 
content = content.replace('\\', '/') # fix slashes
content += "}"
f = open(vsndevts, "w")
f.write(content)
f.close()

# pause the execution of the program until the user has pressed a key
input("Press any key to continue...")
