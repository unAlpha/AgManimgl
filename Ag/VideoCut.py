from manimlib import *
from moviepy.editor import *
from os import system

video_path = r"Z:\LiFiles\2023年\5月份\马斯洛\交付"
media_path = r"E:\Dropbox\manim\AgManimgl\media\videos"  
video_name = "马斯洛-tt2"
Word = "“五一”挤死也要旅游，图个啥？用马斯洛需求层次理论分析一下"
GeneratorFalse = False
num_clip = 2
clip_times=[
        # ["01:00:00:00","01:00:00:00"],
        # ["01:00:00:00","01:00:00:00"],
        # ["01:00:00:00","01:00:00:00"],
        # ["01:00:00:00","01:00:00:00"],
        # ["01:00:00:00","01:00:00:00"],
        # ["01:00:00:00","01:00:00:00"],
    ]
clip_path = os.path.join(video_path,"抖音切割")
image_path = os.path.join(clip_path,"images")
video_file = os.path.join(video_path, video_name+".mp4")
txt = [[f"{i+1}/{num_clip}",Word] for i in range(0,num_clip)]

class video_text0(Scene):
    i = 0 
    def construct(self):
        text1 = Text(
                txt[self.i][0],
                font_size=40,
                color=RED,
                # font ='Alibaba PuHuiTi 2.0 115 Black',
                font = '阿里巴巴普惠体 2.0',
                weight = 'Bold'
            )
        text2 = Text(
                txt[self.i][1],
                font_size=40,
                color=WHITE,
                # font ='Alibaba PuHuiTi 2.0 75 SemiBold',
                font = '阿里巴巴普惠体 2.0',
                weight = 'Medium'
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
        self.wait(0.1)

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

# 方法一 太慢了   
def moviepy_video_clip():
    video_file = os.path.join(video_path, video_name+".mp4")
    video_clip = VideoFileClip(video_file)
    fps = video_clip.fps
    
    time_str =[
        ["00:00:00","03:40:03"],
        ["03:37:18","06:57:37"],
        ["06:57:40","09:51:28"],
        ["09:51:34","15:51:35"],
        ["15:37:27","20:22:30"],
        ["20:12:19","21:50:37"],
    ]
    print("Start generate")
    for i,times in enumerate(time_str, start=0):
        print(f"Generate {i+1}")
        start_frames = time_to_frames(times[0], fps)
        end_frames = time_to_frames(times[1], fps)

        clip_path = os.path.join(video_path,"抖音切割")
        # clip_name = "clip.mp4"
        # clip_file = os.path.join(clip_path, clip_name)
        if os.path.exists(video_file):
            clip = video_clip.subclip(start_frames/fps, end_frames/fps)
            # clip.write_videofile(clip_file)
        
        image_path = os.path.join(clip_path,"images")
        image_name_in = f" ({i+1}).jpg"
        # image_name_out = "1img_video.mp4"
        image_file_in = os.path.join(image_path, image_name_in)
        # image_file_out = os.path.join(clip_path, image_name_out)
        if os.path.exists(image_file_in):
            print(image_file_in+" is exist")
            images = [image_file_in] * 5
            images_clip = ImageSequenceClip(images,fps=50,durations=0.1)
            images_clip_rz = images_clip.resize(height=1080)
            # images_clip.write_videofile(image_file_out)
            # final_name = video_name+"-1.mp4"
            # final_file = os.path.join(clip_path, final_name)
            final_clip = concatenate_videoclips([images_clip_rz,clip], method="compose")
            # final_clip.write_videofile(final_file)
            print("The first five frames of video are superimposed successfully!")
        
            media_name = "video_text0.mov"
            media_file = os.path.join(media_path, media_name)
            # video = VideoFileClip(final_file)
            overlay = VideoFileClip(media_file, has_mask=True)
            overlay = overlay.set_start(0.2)
            final_video = CompositeVideoClip([final_clip,overlay])
            final_video_file = os.path.join(clip_path, video_name+f" 6-{i+1}.mp4")
            final_video.write_videofile(final_video_file,codec="h264_nvenc",threads=32)
            print("The final video is generated")

# 推荐使用方法二
def convert_time(time_string, fps):
    # 将字符串转换成一个列表
    chars = [c for c in time_string]

    # 使用一个循环来分隔每两个字符
    pairs = time_string.split(":")

    ms = int(pairs[-1])*(1/fps)*1000
    parts_ms = str(ms).split(".")[0]
    while len(parts_ms) < 3:
        parts_ms = "0"+ parts_ms
    # 使用字符串的 join 方法来连接分隔的字符
    return ":".join(pairs[1:3]) + "." + parts_ms

def ffmpeg_video_clip():
    print("Start generate")
    video = VideoFileClip(video_file)
    fps = video.fps
    for i in range(num_clip):
        print(f"Generate {i+1}")
        clip_name = f"clip_{i+1}.ts"
        clip_file = os.path.join(clip_path, clip_name)
        image_name = f"{i+1}.jpg"
        image_file = os.path.join(image_path, image_name)
        image_file_video = os.path.join(clip_path, f"img_{i+1}.mp4")
        media_name = f"{video_name}_overlay_{i+1}.mov"
        media_file = os.path.join(media_path, media_name)
        final_video_over = os.path.join(clip_path, video_name+f"_tmp_6-{i+1}.ts")
        final_video_file = os.path.join(clip_path, video_name+f"_6-{i+1}.mp4")
        
        if os.path.exists(video_file):
            if not os.path.exists(image_file_video):
                print(f"order_img {i+1} 生成中……")
                order_img = f"ffmpeg -y -loop 1 \
                            -i {image_file} \
                            -t 0.1 \
                            -vf \"fps=50,format=yuv420p,\
                            scale=1920:1080:force_original_aspect_ratio=decrease,\
                            pad = 1920:1080:(ow-iw)/2:(oh-ih)/2\" \
                            -c:v libx264 -b:v 10000k -vbsf h264_mp4toannexb \
                            {image_file_video}"
                os.system(order_img) 
                print(f"order_img {i+1} 生成成功")
                
            if GeneratorFalse:
                start_time = convert_time(clip_times[i][0],fps)
                print(start_time)
                end_time = convert_time(clip_times[i][1],fps)
                print(end_time)
                if not os.path.exists(clip_file):
                    print(f"order_clip {i+1} 生成中……")
                    order_clip = f"ffmpeg -y -ss {start_time} -to {end_time} \
                                -accurate_seek -i {video_file} \
                                -c:v libx264 -b:v 10000k -c:a aac -b:a 195k -vbsf h264_mp4toannexb {clip_file}"
                    os.system(order_clip)
                    print(f"order_clip {i+1} 生成成功")
                    
                if not os.path.exists(final_video_over):
                    print(f"order_overlay {i+1} 生成中……")
                    order_overlay = f"ffmpeg -y -i {clip_file} \
                                    -itsoffset 0.5 -i {media_file} -filter_complex \
                                    \"[1:v]scale=1920:1080[over];[0:v][over]overlay=0:0\" \
                                    -c:v libx264 -b:v 10000k -c:a copy {final_video_over}"
                    os.system(order_overlay)
                    print(f"order_overlay {i+1} 生成成功")
                
                print(f"order_merge {i+1} 合并中")
                order_merge = f"ffmpeg -y -i \
                            \"concat:{image_file_video}|{final_video_over}\" \
                            -c:v libx264 -b:v 10000k -c:a copy {final_video_file}" 
                os.system(order_merge)
                print(f"order_merge {i+1} 合并成功") 
                    
                if os.path.exists(final_video_file):
                    rm_list = [clip_file,final_video_over,image_file_video]
                    for rmf in rm_list:
                        if os.path.exists(rmf):
                            os.remove(rmf)
                            print(f"Delet {rmf} done!")
           
if __name__ == "__main__":
    for i in range(num_clip):
        if not os.path.exists(os.path.join(media_path, f"{video_name}_overlay_{i+1}.mov")):
            system(f"manimgl {__file__} video_text{i} -wt --fps 50 --file_name {video_name}_overlay_{i+1}")
    ffmpeg_video_clip()    
        