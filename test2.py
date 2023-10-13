from manga_down import mangareader     #import mangareader from manga_down

naruto = mangareader.Manga("Bleach")   #initialize Manga class with manga name
print(naruto.get_chapter_list())        #returns list of all chapters of given manga
naruto.download_chapter("687")  #just call the download_chapter by passing chapter number as argument