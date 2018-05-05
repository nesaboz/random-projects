import os
import sys
from shutil import copyfile
import time


def find_files_in_folder(folder):
    """
    Find all the files

    Parameters
    ----------
    folder

    Returns
    -------

    """
    all_the_files = []
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            all_the_files.append(os.path.join(root, name))
        for name in dirs:
            # print(os.path.join(root, name))
            all_the_files.append(os.path.join(root, name))

    return all_the_files


def find_specific_files_only(list_to_search_in, looking_for):
    """
    Description: we want to give input a folder and how the file should look like, common name and extension etc.
    Code will then walk through all folder and store in a list_to_search_in or dict all filenames and pathnames

    Parameters
    ----------
    list_to_search_in
    looking_for

    Returns
    -------

    """

    looking_for = [x.lower() for x in looking_for]
    print(looking_for)
    list_of_only_what_looking_for = []

    for one_thing_to_look_for in looking_for:
        for name in list_to_search_in:
            if one_thing_to_look_for in name.lower():
                list_of_only_what_looking_for.append(name)
    return list_of_only_what_looking_for


def copy_from_list_of_names(list_to_copy_from, folder_to_copy_to):
    """
    Go over all the items in the list and copy to desired folder

    Parameters
    ----------
    list_to_copy_from (list of str): list of all the full paths to copy
    folder_to_copy_from (str): folder to copy to
    """
    list_of_new_paths = []
    if not os.path.exists(folder_to_copy_to):
        print('Folder {} does not exist'.format(folder_to_copy_to))
        return
    for name in list_to_copy_from:
        new_path = os.path.join(folder_to_copy_to, name.split('\\')[-1])
        list_of_new_paths.append(new_path)
        try:
            if not os.path.exists(new_path):
                copyfile(name, new_path)
            else:
                print('File exists {}'.format(new_path))
            time.sleep(0.05)
        except:
            temp = sys.exc_info()  # gather info
            print("{} {}".format(temp, name))  # print info

    return set(list_of_new_paths)


def main():
    """
    Ties everything together
    """

    all_the_files = find_files_in_folder(folder=r'C:\Users\nenad.bozinovic\Downloads\Dropbox (2)')
    list_of_only_what_looking_for = find_specific_files_only(
        all_the_files,
        looking_for=[r'DMDUniformitySystem_BLIBlankFluor_4X_FITC.tiff',
                     r'DMDUniformitySystem_BLIBlankFluor_4X_TRED.tiff'])

    list_of_new_paths = copy_from_list_of_names(
        list_of_only_what_looking_for,
        folder_to_copy_to=r'C:\Users\nenad.bozinovic\Dropbox (Berkeley Lights Inc.)\Projects\17_12_19_Nonuniformity '
                          r'metrics\just_images')

    for name in list_of_new_paths:
        print(name)

    # print('Copied {} files'.format(len(list_of_new_paths)))

main()

