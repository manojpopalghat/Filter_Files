import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os,shutil
win=tk.Tk()
win.title('Filter Your Files')
path=r"C:\Downloads"
def SelectPath():
	global path
	done_lbl=ttk.Label(win,text='                                '*2)
	done_lbl.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)
	path=filedialog.askdirectory(initialdir=r"C:\Downloads")
	path_lbl=ttk.Label(win,text="                                                        "*2)
	path_lbl.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)
	path_lbl=ttk.Label(win,text=f"Selected Path is : {path}")
	path_lbl.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)
	
	
def	Filter():
	global path
	
	audio_extensions=('mp3','3gp','aa','aac','aax','act','aiff','amr','ape','au','awb',
	'dct','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p','mmf',
	'mpc','msv','nmf','nsf','ogg','oga','mogg','opus','ra','rm','raw','sln',
	'tta','voc','vox','wav','wma','wv','8svx')
	
	video_extensions=('mp4','m4p','m4v','webm','mkv','flv','vob','ogv','ogg','drc','gif',
		'gifv','mng','avi','MTS','M2TS','mov','qt','wmv','yuv','rm','rmvb','asf','amv',
		'mpg','mp2','mpeg','mpe','mpv','m2v','m4v','svi','3gp','3g2','mxf','roq','nsv',
		'flv','f4v','f4p','f4a','f4b')	
		
	document_extensions=('doc','docx','odt','pdf','rtf','tex','txt','wks','wps','wpd','md','PDF')

	compressed_extensions=('7z','arj','deb','pkg','rar','rpm','tar.gz','tar.xz','z','zip')

	disc_extensions=('bin','dmg','iso','toast','vcd')

	database_extensions=('csv','dat','db','dbf','log','mdb','sav','sql','xml','tar')

	executable_extensions=('apk','bat','bin','cgi','pl','com','exe','gadget','jar','wsf','sh')

	font_extensions=('fnt','fon','otf','ttf')

	image_extensions=('ai','bmp','gif','ico','jpeg','jpg','png','ps','psd','svg','tif','tiff')

	internet_extensions=('asp','aspx','cer','cfm','cgi','pl','css','htm','html','js','jsp','part','php','rss','xhtml','ics')

	presentation_extensions=('key','odp','pps','ppt','pptx')

	programming_extensions=('c','cpp','class','cs','h','java','sh','swift','vb','py','asm','o')

	spreadsheet_extensions=('ods','xlr','xls','xlsx')

	system_extensions=('bak','cab','cfg','cpl','cur','dll','dmp','drv','icns','ico','ini','lnk','msi','sys','tmp')



	os.chdir(path)

	directory_files=os.listdir()
	audio_list=[]
	video_list=[]
	document_list=[]
	compressed_list=[]
	disc_list=[]
	database_list=[]
	executable_list=[]
	font_list=[]
	image_list=[]
	internet_list=[]
	presentation_list=[]
	programming_list=[]
	spreadsheet_list=[]
	system_list=[]

	#audio
	for file in directory_files:
		for extension in audio_extensions:
			if file.endswith('.'+extension):
				audio_list.append(file)

	#video
	for file in directory_files:
		for extension in video_extensions:
			if file.endswith('.'+extension):
				video_list.append(file)

	#document
	for file in directory_files:
		for extension in document_extensions:
			if file.endswith('.'+extension):
				document_list.append(file)

	#compressed
	for file in directory_files:
		for extension in compressed_extensions:
			if file.endswith('.'+extension):
				compressed_list.append(file)

	#disc
	for file in directory_files:
		for extension in disc_extensions:
			if file.endswith('.'+extension):
				disc_list.append(file)

	#database
	for file in directory_files:
		for extension in database_extensions:
			if file.endswith('.'+extension):
				database_list.append(file)		
				
	#executable				
	for file in directory_files:
		for extension in executable_extensions:
			if file.endswith('.'+extension):
				executable_list.append(file)

	#font			
	for file in directory_files:
		for extension in font_extensions:
			if file.endswith('.'+extension):
				font_list.append(file)

	#image			
	for file in directory_files:
		for extension in image_extensions:
			if file.endswith('.'+extension):
				image_list.append(file)

	#internet			
	for file in directory_files:
		for extension in internet_extensions:
			if file.endswith('.'+extension):
				internet_list.append(file)
		
	#presentation			
	for file in directory_files:
		for extension in presentation_extensions:
			if file.endswith('.'+extension):
				presentation_list.append(file)

	#programming			
	for file in directory_files:
		for extension in programming_extensions:
			if file.endswith('.'+extension):
				programming_list.append(file)

	#spreadsheet			
	for file in directory_files:
		for extension in spreadsheet_extensions:
			if file.endswith('.'+extension):
				spreadsheet_list.append(file)

	#system			
	for file in directory_files:
		for extension in system_extensions:
			if file.endswith('.'+extension):
				system_list.append(file)


	#print(audio_list)
	if len(audio_list)>0:
		if not os.path.exists('Audio'):
			os.mkdir('Audio')
		for i in audio_list:
			shutil.move(i,f'Audio/{i}') 

	#print(video_list)
	if len(video_list)>0:
		if not os.path.exists('Video'):
			os.mkdir('Video')
			
		for i in video_list:
			shutil.move(i,f'Video/{i}') 

	#print(document_list)
	if len(document_list)>0:
		if not os.path.exists('Document'):
			os.mkdir('Document')
			
		for i in document_list:
			shutil.move(i,f'Document/{i}') 
			
	#print(compressed_list)
	if len(compressed_list)>0:
		if not os.path.exists('Compressed'):
			os.mkdir('Compressed')
		
		for i in compressed_list:
			shutil.move(i,f'Compressed/{i}') 
			
	#print(disc_list)
	if len(disc_list)>0:
		if not os.path.exists('Disc'):
			os.mkdir('Disc')
		
		for i in disc_list:
			shutil.move(i,f'Disc/{i}') 
			

	#print(database_list)
	if len(database_list)>0:
		if not os.path.exists('Database'):
			os.mkdir('Database')
		
		for i in database_list:
			shutil.move(i,f'Database/{i}') 
			
	#print(executable_list)
	if len(executable_list)>0:
		if not os.path.exists('Executable'):
			os.mkdir('Executable')
		
		for i in executable_list:
			shutil.move(i,f'Executable/{i}') 
			
	#print(font_list)
	if len(font_list)>0:
		if not os.path.exists('Font'):
			os.mkdir('Font')
		
		for i in font_list:
			shutil.move(i,f'Font/{i}') 
			

	#print(image_list)
	if len(image_list)>0:
		if not os.path.exists('Image'):
			os.mkdir('Image')
		
		for i in image_list:
			shutil.move(i,f'Image/{i}') 
			
	#print(internet_list)
	if len(internet_list)>0:
		if not os.path.exists('Internet'):
			os.mkdir('Internet')
		
		for i in internet_list:
			shutil.move(i,f'Internet/{i}') 
			
	#print(presentation_list)
	if len(presentation_list)>0:
		if not os.path.exists('Presentation'):
			os.mkdir('Presentation')
		
		for i in presentation_list:
			shutil.move(i,f'Presentation/{i}') 
			
	#print(programming_list)
	if len(programming_list)>0:
		if not os.path.exists('Programming'):
			os.mkdir('Programming')
		
		for i in programming_list:
			shutil.move(i,f'Programming/{i}') 
			

	#print(spreadsheet_list)
	if len(spreadsheet_list)>0:
		if not os.path.exists('Spreadsheet'):
			os.mkdir('Spreadsheet')
		
		for i in spreadsheet_list:
			shutil.move(i,f'Spreadsheet/{i}') 
		

	#print(system_list)
	if len(system_list)>0:
		if not os.path.exists('System'):
			os.mkdir('System')

		for i in system_list:
			shutil.move(i,f'System/{i}') 

	done_lbl=ttk.Label(win,text='********** DONE !!! **********')
	done_lbl.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)
	
	
	
	
	
	
select_button=ttk.Button(win,text='Select Folder',width=15,command=SelectPath)
select_button.grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)

path_lbl=ttk.Label(win,text=f"Default Path is : {path}")
path_lbl.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)

filter_button=ttk.Button(win,text='Filter Files',width=15,command=Filter)
filter_button.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)




win.mainloop()
