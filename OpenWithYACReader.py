# coding: utf-8
#
#OpenWithYACReader.py
#
#Author: Killo3967
#
#Description: Open the comic with YACReade 
#
#Version: 1.1
#               
#Feel free to copy, use or modify any or all of this as you like.
#
#ComicRack Declarations
#
#@Name Open with YACReader
#@Hook Books
#@Key Open with YACReader
#@Image yacreader.png
#@PCount 0


import clr
import os
from System.IO import *
clr.AddReference("System")
from System.Diagnostics import Process
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *

# Declare variable
yacreader_executable = "C:\Program Files\YACReader\YACReader.exe"

def OpenWithYACReader(books):
	fileTypes = '.cbz,.zip,.tar,.cb7,.7z,.cbr,.rar,.pdf'.split(',')
	eComicInfo = FileInfo(books[0].FilePath)
  
	# if exists YACReader executable
	if os.path.exists(yacreader_executable):
		# if the file is a comic
		if eComicInfo.Extension.lower() in fileTypes:
			try:
				Process.Start(r'"C:\Program Files\YACReader\YACReader.exe"', r'"' + books[0].FilePath + r'"')
			except:
				MessageBox.Show(ComicRack.MainWindow, 'Could not find YACReader')
		
		else:
			MessageBox.Show(ComicRack.MainWindow, 'Cannot open ' + eComicInfo.Extension + ' files with YAC READER')
