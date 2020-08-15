from yscraper import youtubescraper as yes

links = yes.getLinks("Avengers End Game Trailer")

# for link in links:
#     print(link)

vidInfo = yes.getVideoInfo(links[0])
for key in vidInfo:
    print(f"{key} = {vidInfo[key]}")

#yes.downloadVideo(links[0])