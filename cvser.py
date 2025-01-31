import sys
import os.path
import requests
import pandas


def main():
    has_arg = len(sys.argv)
    # check if user provided xlsx
    has_error = handle_arg_error(has_arg)

    # proceed if user provided xlxx
    if has_error == False:
        xlsx = sys.argv[1]
        convert_to_csv(xlsx)

def handle_arg_error(arg):
    # user provided no arguments
    if arg == 1:
        print("Error: Please provide xlsx file")
        return True
    # user provided more than one argument
    elif arg > 2:
        print("Error: Please provide one file only")
        return True
    # user provided one argument
    else:
        return False
    
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