class BasicPlayer:
    def stream_video(self,video_title:str)->str:
        # Standard default behaviour
        return f"Streaming '{video_title}'in Standard Definition (420p)."
    
class PremiumPlayer(BasicPlayer):
    # Overriding :Modifying the exact same method signature for premium account
    def stream_video(self, video_title:str)->str:
        return f"Streaming'{video_title}' in Ultra High Definition (4k HDR)."


class MediaPlaylist:
    def __init__(self,name):
        self.name=name

    def add_media(self,title:str=None,media_id:int=None,track_list:list=None)->None:
        if title is not None and media_id is not None:
            
            print (f"Added the '{title}' having media id '{media_id}' to the playlist '{self.name}'")
        elif title is not None :
                    print(f"Added track '{title}' directly to playlist '{self.name}")
        elif media_id is not None:
            print(f"Looked up ID '{media_id}' and added it to playlist '{self.name}'")
        elif track_list is not None:
            print(f"Imported {len(track_list)} items into playlist '{self.name}'")
        else:
            print("No valid media items provided to add")

# Testing Method Overriding
free_user=BasicPlayer()
paid_user=PremiumPlayer()

print(free_user.stream_video("Avenger"))
print(paid_user.stream_video("Avenger"))

# Testing Method Overloading
my_playlist=MediaPlaylist("Sufi Tracks")

# Type A: Passing  title and media _id
my_playlist.add_media(title="O re piya" ,media_id=56)
# Type B Passing only title 
my_playlist.add_media(title="Arziyan")
# Type C passing only media id
my_playlist.add_media(media_id=456)
# Type D passing only track list
my_playlist.add_media(track_list=['Song1','Song 2','Song 3'])
# Type E passing nothing
my_playlist.add_media()