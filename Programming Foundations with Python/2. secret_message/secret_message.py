import os



def rename_files():
	file_path = (os.getcwd() + "/prank") 
	file_list = os.listdir(file_path)
	os.chdir(file_path)	
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
rename_files()
