from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib.request
import youtube_dl 
import sys

def dwl_vid(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
		ydl.download([zxt])

def help():
	print("Input file should contain search queries on different lines")
	print("The first search result of youtube will be downloaded without asking you anything")
	print("To download from a different source you will have to change the code involving youtube_dl and replace it with wget or similar tools\n")
	return

ydl_opts = {
    # 'format': 'bestaudio/best',                               To change the preferred format 
    # 'prefer_ffmpeg': True,
    # 'keepvideo': True
	}
if(len(sys.argv)==2):
	file = open(sys.argv[1],"r")
	for line in file:
		textToSearch = line
		query = urllib.parse.quote(textToSearch)
		url = "https://www.youtube.com/results?search_query=" + query
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		# for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		#     print('https://www.youtube.com' + vid['href'])
		try:
			vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
			print(vid['href'])
			link_of_the_video = "https://www.youtube.com" + vid['href']
			zxt = link_of_the_video.strip()
			try:
				dwl_vid()
			except:
				print("Error in downloading")
				continue
		except:
			continue
	file.close()
	print("Hurray")
	exit()
else:
	while(1):
		print("Type in the keyword for video you want to download.\nPress q to quit.For more info type help()\nDownload:")
		search_query = input()
		if(search_query=='q'):
			exit()
		if(search_query=="help()"):
			help()
			continue
		query = urllib.parse.quote(search_query)
		url = "https://www.youtube.com/results?search_query=" + query
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		try:
			vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
			print(vid['title'])
			now= input("Download? (press n or no to cancel)\n")
			if(now in ['y',"Y",'Yes']):
				link_of_the_video = "https://www.youtube.com" + vid['href']
				zxt = link_of_the_video.strip()
				try:
					dwl_vid()
				except:
					print("Error in downloading")
					continue
			else:
				continue			
		except:
			print("Search corrupted.\nTry other keywords")
			continue
		print("Download successfull!\n")

	
