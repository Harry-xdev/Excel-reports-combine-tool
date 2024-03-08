from pathlib import Path

def count_xlsx_file(folder_path):
	folder = Path(folder_path)
	xls_files = folder.glob('*.xlsx')
	xlsx_lst = [str(i) for i in xls_files]
	print(len(xlsx_lst))


count_xlsx_file('New folder')