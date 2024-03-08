from pathlib import Path

def get_filenames(folder_path, format):
	folder = Path(folder_path)
	files = folder.glob(f'{format}')
	lst_str = [str(i) for i in files]
	name_lst = []
	for i in lst_str:
		i = i[(len(folder_path) + 1):]
		name_lst.append(i)
		#print(i)
	return name_lst