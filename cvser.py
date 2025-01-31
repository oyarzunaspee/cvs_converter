import sys
import os.path
import requests
import pandas
import re


def main():
    # check if provided files are valid
    handle_arg_error(sys.argv)

    # iterate through provided files
    for xlsx_file in sys.argv[1:]:
        convert_to_csv(xlsx_file)

def handle_arg_error(arguments):
    # check if user provided at least 1 file
    try:
        arguments[1]
    except IndexError:
        print("Error: Please provide at least one xlsx file")
        raise Exception("No xlsx provided")
    
    # check if arguments are either type file or match a url
    for arg in arguments[1:]:
        # regex for url
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        
        # check if argument is a file
        is_file = os.path.isfile(arg)
        # check if argument matches a url
        is_url = re.match(url_pattern, arg)
        
        # if argument is neither a file nor matches a url raise error
        if not is_file and is_url is None:
            print("Error: Please provide a valid xlsx file")
            raise Exception(f"Wrong file: {arg}") 
    
def convert_to_csv(xlsx):
    prepared_xlsx = xlsx
    # check if user provided xlsx in file or link format
    is_file = os.path.isfile(xlsx)

    # if link get response
    if is_file == False:
        prepared_xlsx = get_url_response(xlsx)

    # format excel
    excel_file = pandas.read_excel(prepared_xlsx)
    # ask user for new name for csv file
    new_name = input("Name new CVS file: ")
    cvs_name = f"{new_name}.cvs"
    # create output csv file
    excel_file.to_csv(cvs_name, index = None, header=True)

def get_url_response(url):
    # get url response
    get_url = requests.get(url)
    url_content = get_url.content
    return url_content

if __name__ == "__main__":
    main()