from yscraper import youtubescraper as yes

title = "Avengers End Game Trailer"

links = yes.getLinks(title)

# for link in links:
#     print(link)

vidInfo = yes.getVideoInfo(links[0])
for key in vidInfo:
    print(f"{key} = {vidInfo[key]}")

#yes.downloadVideo(links[0], "./out/", title, width=360, extension="mp4")