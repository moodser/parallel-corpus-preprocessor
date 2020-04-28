"""
Created on Tue Feb 09 2019

@script: Parallel Corpus Pre-processor

@author: Moodser Hussain
@contact: moodser.hussain@gmail.com	
@org: COMSATS University Islamabad, Lahore Campus, Pakistan

"""

####################################
## Acknowledgement
#### Dr. Rao Muhammad Adeel Nawab (Supervisor)
#### Mr. Muhammad Sharjeel (Co-Supervisor)
####################################

"""
@functionality:
-> It remove and count blank lines from parallel corpus files.
-> It count number of short sentences (one world sentences) but don't remove them.
-> It remove and count long lines (length > 40) from parallel corpus files.
"""



# Required Libraries
import random, sys, os, glob, math

def getFileNames():
	# Get the name of files in a list
	directory = os.getcwd()
	files = sorted(os.listdir(directory+'/en'))
	i=0
	for thisFile in files:
		files[i] = os.path.splitext(thisFile)[0]
		i=i+1
	return files

if __name__ == '__main__':
	file_names = getFileNames()
	
	os.mkdir(os.getcwd()+'/en_new')
	os.mkdir(os.getcwd()+'/ur_new')

	# Generating a file to store number of empty and short sentences
	report = open('report.txt', 'a+', encoding="utf8")

	for filename in file_names:
		en = corpus_en = filename+'.en'
		ur = corpus_ur = filename+'.ur'
		
		# Initializing Variables
		line_number = single_word = empty_line = long_lines = 0
		line_del_list = []

		# Generating Temporary Files (for removing blank lines from English File)
		new_en = open('en_new/'+corpus_en+'.temp', 'a+', encoding="utf8")
		new_ur = open('ur_new/'+corpus_ur+'.temp', 'a+', encoding="utf8")

		with open('en/'+corpus_en, encoding="utf8") as file:
			for line in file:
				line_number=line_number+1
				if (len(str(line).split())>1 and len(str(line).split())<=41):
					new_en.writelines(line)
					if (len(str(line).split())==2):
						single_word=single_word+1
				elif (len(str(line).split())>41):
					line_del_list.append(line_number)
					long_lines=long_lines+1
				else:
					line_del_list.append(line_number)
					empty_line=empty_line+1

		# Saving Report for English File
		report.writelines('\n')
		report.writelines('File Name : '+en+'\n')
		report.writelines('Empty Lines : '+str(empty_line)+'\n')
		report.writelines('One Word Sentences : '+str(single_word)+'\n')
		report.writelines('Long Sentences (Removed) : '+str(long_lines)+'\n')
		report.writelines('\n')

		line_number=0
		# Removing Sentences from Urdu File (against English Blank Lines)
		with open('ur/'+corpus_ur, encoding="utf8") as file:
			for line in file:
				line_number=line_number+1
				if line_number not in line_del_list:
					new_ur.writelines(line)	
		new_en.close()
		new_ur.close()

		# Considering temporary files as current files
		corpus_en = corpus_en+'.temp'
		corpus_ur = corpus_ur+'.temp'

		# Generating Final Files
		final_en = open('en_new/'+en, 'a+', encoding="utf8")
		final_ur = open('ur_new/'+ur, 'a+', encoding="utf8")
		# Initializing Variables
		line_number = single_word = empty_line = long_lines = 0
		line_del_list = []

		# Detecting Blank Lines and Short Sentences (from Urdu File)
		with open('ur_new/'+corpus_ur, encoding="utf8") as file:
			for line in file:
				line_number=line_number+1
				if (len(str(line).split())>1 and len(str(line).split())<=41):
					final_ur.writelines(line)
					if (len(str(line).split())==2):
						single_word=single_word+1
				elif (len(str(line).split())>41):
					line_del_list.append(line_number)
					long_lines=long_lines+1
				else:
					line_del_list.append(line_number)
					empty_line=empty_line+1

		# Saving Report for Urdu File
		report.writelines('File Name : '+ur+'\n')
		report.writelines('Empty Lines : '+str(empty_line)+'\n')
		report.writelines('One Word Sentences : '+str(single_word)+'\n')
		report.writelines('Long Sentences (Removed) : '+str(long_lines)+'\n')
		report.writelines('\n #################################')
		line_number=0

		# Removing Sentences from English File (against Urdu Blank Lines)
		with open('en_new/'+corpus_en, encoding="utf8") as file:
			for line in file:
				line_number=line_number+1
				if line_number not in line_del_list:
					final_en.writelines(line)		



		#Closing Files
		final_en.close()
		final_ur.close()
		# Removing Temporary Files
		os.remove('en_new/'+corpus_en)
		os.remove('ur_new/'+corpus_ur)
