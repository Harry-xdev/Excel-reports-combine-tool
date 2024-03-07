import pandas as pd
from pathlib import Path
import openpyxl
import os

from functions import func_get_filename


folder = 'input'
format_lst = ['*.xlsx' , '*.xls']

xlsx = []
xls = []

xlsx_file = func_get_filename.get_filenames(folder, format_lst[0])
xlsx = xlsx + xlsx_file
xls_file = func_get_filename.get_filenames(folder, format_lst[1])
xls = xls + xls_file

print(xlsx)
print(xls)


def converter(input_file, output_file):
	excel_file = pd.ExcelFile(input_file)
	sheet_names = excel_file.sheet_names
	with pd.ExcelWriter(output_file) as writer:
		for i in sheet_names:
			df = pd.read_excel(excel_file, sheet_name=i)
			df.to_excel(writer, sheet_name=i, index=False)

def running():
	input_path = 'input'
	output_path = 'converted'
	file_name_lst = xls
	#Convert .xls to .xlsx
	for i in file_name_lst:
		input_file = i + '.xls'
		#delete 5 first strings of report name to change output link
		i = i[5:]
		output_file = output_path + '/' + i + '.xlsx'
		converter(input_file, output_file)
		os.remove(input_file)
	file_name_lst = xlsx
	#Convert .xlsx to xlsx
	for i in file_name_lst:
		input_file = i + '.xlsx'
		#delete 5 first strings of report name to change output link
		i = i[5:]
		output_file = output_path + '/' + i + '.xlsx'
		converter(input_file, output_file)
	print('Files converted to xlsx successful.')