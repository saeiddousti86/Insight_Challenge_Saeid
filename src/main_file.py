'''
This file is the main file of the Insight Fellowship Challenge
Author: Saeid Dousti
submitted: 03-19-2020
'''
from input_path import input_path_func
from cmp_main_list import cmp_main_list_func
from process import process_func
from write_csv import write_report_func, write_error_func

if __name__ == "__main__":
    input_path = input_path_func()
    main_list, error_list = cmp_main_list_func(input_path)
    output_list = process_func(main_list)
    write_report_func(output_list)
    write_error_func(error_list)

    print('Done!')
