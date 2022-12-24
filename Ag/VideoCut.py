from manimlib import *
from moviepy.editor import *

def time_to_frames(time_str, fps):
    # Split the time string into hours, minutes, seconds, and frames
    hours, minutes, seconds, frames = time_str.split(":")
    # Convert hours, minutes, seconds, and frames to integers
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    frames = int(frames)
    # Calculate the total number of frames
    total_frames = fps * (hours * 3600 + minutes * 60 + seconds) + frames
    return total_frames

Word = "可控核聚变重大突破：美国人用激光惯性约束实现点火！"
txt = [[f"{i}/6",Word] for i in range(1,7)]

class video_text0(Scene):
    i = 0 
    def construct(self):
        text1 = Text(
                txt[self.i][0],
                font_size=40,
                color=RED,
                font ='Alibaba PuHuiTi 2.0 115 Black',
            )
        text2 = Text(
                txt[self.i][1],
                font_size=40,
                color=WHITE,
                font ='Alibaba PuHuiTi 2.0 75 SemiBold',
            )
        text = VGroup(text1,text2).arrange(RIGHT,buff=0.38)
        text.to_corner(DL).shift(UP)
        
        bg_text1 = BackgroundRectangle(text1,fill_opacity=0.96,buff=0.205,color=BLUE)
        bg_text2 = BackgroundRectangle(text2,fill_opacity=0.96,buff=0.168,color=BLUE_E)
        bg_text = VGroup(bg_text1,bg_text2)
        self.play(
                FadeIn(bg_text,scale=0.9),
                ShowPassingFlashAround(bg_text),
                ShowCreation(text),
            ) 
        self.wait(2.68)   
        self.play(
            Uncreate(text),
            FadeOut(bg_text),  
        )

class video_text1(video_text0):
    i = 1 

class video_text2(video_text0):
    i = 2

class video_text3(video_text0):
    i = 3

class video_text4(video_text0):
    i = 4
    
class video_text5(video_text0):
    i = 5
   
def video_clip():
    video_path = r"Z:\LiFiles\2022年\12月份\惯性核聚变\交付"
    video_name = "惯性核聚变-ttB"
    video_file = os.path.join(video_path, video_name+".mp4")
    video_clip = VideoFileClip(video_file)

    start_time_str = "00:01:30:05"
    end_time_str = "00:02:00:05"
    fps = video_clip.fps
    start_frames = time_to_frames(start_time_str, fps)
    end_frames = time_to_frames(end_time_str, fps)

    clip_path = os.path.join(video_path,"抖音切割")
    # clip_name = "clip.mp4"
    # clip_file = os.path.join(clip_path, clip_name)
    if os.path.exists(video_file):
        clip = video_clip.subclip(start_frames / fps, end_frames / fps)
        # clip.write_videofile(clip_file)
    
    image_path = os.path.join(clip_path,"images")
    image_name_in = "1 (1).jpg"
    # image_name_out = "1img_video.mp4"
    image_file_in = os.path.join(image_path, image_name_in)
    # image_file_out = os.path.join(clip_path, image_name_out)
    if os.path.exists(image_file_in):
        images = [image_file_in] * 5
        images_clip = ImageSequenceClip(images,fps=50,durations=0.1)
        images_clip_rz = images_clip.resize(height=1080)
        # images_clip.write_videofile(image_file_out)
    
    # final_name = video_name+"-1.mp4"
    # final_file = os.path.join(clip_path, final_name)
    final_clip = concatenate_videoclips([images_clip_rz,clip], method="compose")
    # final_clip.write_videofile(final_file)
    print("The first five frames of video are superimposed successfully!")
    
    media_path = r"E:\Dropbox\manim\AgManimgl\media\videos"
    media_name = "video_text0.mov"
    media_file = os.path.join(media_path, media_name)
    # video = VideoFileClip(final_file)
    overlay = VideoFileClip(media_file, has_mask=True)
    overlay = overlay.set_start(0.2)
    final_video = CompositeVideoClip([final_clip,overlay])
    final_video_file = os.path.join(clip_path, video_name+" 6-1.mp4")
    final_video.write_videofile(final_video_file)
    print("The final video is generated")

if __name__ == "__main__":
    from os import system
    # for i in range(1):
    #     system(f"manimgl {__file__} video_text{i} -ot --fps 50")
    video_clip()    
        