import os

def input_path_func():
    '''
    This function retrieves the path of the input file from the repository
    :return: the input file absolute path
    '''
    input_folder_path = os.path.abspath("../input")
    input_content = os.listdir(input_folder_path)
    return os.path.join(input_folder_path,input_content[0])