class MediaPlayer:
    def play_audio(self, audiofile):
        raise NotImplemented
    
    def stop_audio(self):
        raise NotImplemented
    
    def play_video(self, videofile):
        raise NotImplemented
    
    def stop_video(self):
        raise NotImplemented
    
    def adjust_volume(self):
        raise NotImplemented
    
class AudioPlayer:
    def play_audio(self, audiofile):
        raise NotImplemented
    
    def stop_audio(self):
        raise NotImplemented
    
    def adjust_volume(self):
        raise NotImplemented
    
class VideoPlayer:
    def play_video(self, videofile):
        raise NotImplemented
    
    def stop_video(self):
        raise NotImplemented
    
    def adjust_volume(self):
        raise NotImplemented
    
class MP3Player(AudioPlayer):
    def play_audio(self, audiofile):
        pass
    
    def stop_audio(self):
        pass
    
    def adjust_volume(self):
        pass
    
class MP4VideoPlayer(VideoPlayer):
    def play_video(self, videofile):
        pass
    
    def stop_video(self):
        pass
    
    def adjust_volume(self):
        pass
    
class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self, audiofile):
        pass
    
    def stop_audio(self):
        pass
    
    def adjust_volume(self):
        pass
    
    def play_video(self, videofile):
        pass
    
    def stop_video(self):
        pass
    
    def adjust_volume(self):
        pass
    
    