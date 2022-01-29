def parse_date(orginal_date):
    temp = orginal_date.split("/")
    return f"{temp[2]}-{temp[1]}-{temp[0]}"

#Get the authors of the songs
#song_authors = [artist.find(name="span", class_="u-line-height-normal@mobile-max").getText().strip() for artist in row_divs]  
    
#complete_songs = []

#for i in range(len(row_divs)):
#    complete_songs.append(f"{song_titles[i]} - {song_authors[i]}")