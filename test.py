
from functions import func_get_filename

def count_xlsx_file():
	# script_path = os.path.abspath(__file__)
	# folder_path = os.path.dirname(script_path)
	file_lst = func_get_filename.get_filenames('export', '*.xlsx')
	length = len(file_lst)
	return length

print(count_xlsx_file())