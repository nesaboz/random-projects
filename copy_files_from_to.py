from shutil import copyfile, rmtree, move
import os

f = r'C:\Manufacturing_matlab\Optics\QC\optical_qc_matlab_analysis\list_of_files.txt'
destination_path = r'C:\Manufacturing_matlab\Optics\QC\optical_qc_matlab_analysis\used'

with open(f, "r") as infile:
    for line in infile:
        line = line.rsplit()[0]
        a, b = os.path.split(line)
        print(line)
        print(os.path.join(destination_path, b))
        try:
            copyfile(line, os.path.join(destination_path, b))
        except:
            pass
