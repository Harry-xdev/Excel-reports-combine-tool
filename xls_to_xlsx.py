import pandas as pd
from pathlib import Path
import openpyxl
import os

def get_file_path_list_xls(input_path):
	folder = Path(input_path)
	xls_files = folder.glob('*.xls')
	file_path_lst = [str(i) for i in xls_files]
	file_name_lst = []
	for i in file_path_lst:
		i = i[:-4]
		file_name_lst.append(i)
		#print(i)
	return file_name_lst

def get_file_path_list_xlsx(input_path):
	folder = Path(input_path)
	xlsx_files = folder.glob('*.xlsx')
	file_path_lst = [str(i) for i in xlsx_files]
	file_name_lst = []
	for i in file_path_lst:
		i = i[:-5]
		file_name_lst.append(i)
		#print(i)
	return file_name_lst

def converter(input_file, output_file):
	excel_file = pd.ExcelFile(input_file)
	sheet_names = excel_file.sheet_names
	with pd.ExcelWriter(output_file) as writer:
		for i in sheet_names:
			df = pd.read_excel(excel_file, sheet_name=i)
			df.to_excel(writer, sheet_name=i, index=False)

def running():
	input_path = 'input'
	output_path = 'output'
	file_name_lst = get_file_path_list_xls(input_path)
	#Convert .xls to .xlsx
	for i in file_name_lst:
		input_file = i + '.xls'
		#delete 5 first strings of report name to change output link
		i = i[5:]
		output_file = output_path + '/' + i + '.xlsx'
		converter(input_file, output_file)
		os.remove(input_file)
	file_name_lst = get_file_path_list_xlsx(input_path)
	#Convert .xlsx to xlsx
	for i in file_name_lst:
		input_file = i + '.xlsx'
		#delete 5 first strings of report name to change output link
		i = i[5:]
		output_file = output_path + '/' + i + '.xlsx'
		converter(input_file, output_file)

	print('files converted to xlsx successful.')