def create_youtube_video(title,discription):
	vid = {"Title": title, "Discription": discription, "likes": 0, "dislikes": 0 , "comments": {}}
	return vid

youtube_video=create_youtube_video("bashar","fun")
print(youtube_video)

def likes(youtube_video):
	print('hi')
	if "likes" in youtube_video:
		print('bashar')
		youtube_video["likes"]+=1
		return youtube_video

def dislikes(youtube_video):
	print('hi')
	if "dislikes" in youtube_video:
		print('bashar')
		youtube_video["dislikes"]+=1
		return youtube_video

print(likes(youtube_video))

def add_comment("youtube_video", "username", "comment_text"):
	youtube_video["comments"][username]=comment_text

youtube_video=create_youtube_video("lill","CS")
for i in range (495):
	likes(youtube_video)
	