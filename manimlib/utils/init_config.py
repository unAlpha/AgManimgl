import yaml
import os

def init_customization():
    configuration = {
        "directories": {
            "mirror_module_path": False,
            "output": "",
            "raster_images": "",
            "vector_images": "",
            "sounds": "",
            "temporary_storage": "",
        },
        "universal_import_line": "from manimlib import *",
        "style": {
            "tex_template": "",
            "font": "Consolas",
            "background_color": "",
        },
        "window_position": "UR",
        "window_monitor": 0,
        "break_into_partial_movies": False,
<<<<<<< HEAD
        "camera_qualities": {
            "low": {
                "resolution": "854x480",
                "frame_rate": 15,
            },
            "medium": {
                "resolution": "1280x720",
                "frame_rate": 30,
            },
            "high": {
                "resolution": "1920x1080",
                "frame_rate": 60,
            },
            "ultra_high": {
                "resolution": "3840x2160",
                "frame_rate": 60,
            },
            "default_quality": "",
        }
=======
        "camera_resolutions": {
            "low": "854x480",
            "medium": "1280x720",
            "high": "1920x1080",
            "4k": "3840x2160",
            "default_resolution": "",
        },
        "fps": 30,
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3
    }

    print("Initialize configuration")
    scope = input(" Please select the scope of the configuration [global/local]: ")
    if scope == "global":
        from manimlib.config import get_manim_dir
        file_name = os.path.join(get_manim_dir(), "manimlib", "default_config.yml")
    else:
        file_name = os.path.join(os.getcwd(), "custom_config.yml")

    print("\n directories:")
    configuration["directories"]["output"] = input("  [1/8] Where should manim output video and image files place: ")
    configuration["directories"]["raster_images"] = input("  [2/8] Which folder should manim find raster images (.jpg .png .gif) in (optional): ")
    configuration["directories"]["vector_images"] = input("  [3/8] Which folder should manim find vector images (.svg .xdv) in (optional): ")
    configuration["directories"]["sounds"] = input("  [4/8] Which folder should manim find sound files (.mp3 .wav) in (optional): ")
    configuration["directories"]["temporary_storage"] = input("  [5/8] Which folder should manim storage temporary files: ")

<<<<<<< HEAD
    print("\n tex:")
    tex = input("  [6/8] Which executable file to use to compile [latex/xelatex]: ")
    if tex == "latex":
        configuration["tex"]["executable"] = "latex"
        configuration["tex"]["template_file"] = "tex_template.tex"
        configuration["tex"]["intermediate_filetype"] = "dvi"
    else:
        configuration["tex"]["executable"] = "xelatex -no-pdf"
        configuration["tex"]["template_file"] = "ctex_template.tex"
        configuration["tex"]["intermediate_filetype"] = "xdv"

    print("\n style:")
    configuration["style"]["background_color"] = input("  [7/8] Which background color do you want (hex code): ")
=======
        console.print("[bold]Styles:[/bold]")
        style_config = configuration["style"]
        tex_template = Prompt.ask(
            "  Select a TeX template to compile a LaTeX source file",
            default="default"
        )
        style_config["tex_template"] = tex_template
        style_config["background_color"] = Prompt.ask(
            "  Which [bold]background color[/bold] do you want [italic](hex code)",
            default="#333333"
        )

        console.print("[bold]Camera qualities:[/bold]")
        table = Table(
            "low", "medium", "high", "ultra_high",
            title="Four defined qualities",
            box=box.ROUNDED
        )
        table.add_row("480p15", "720p30", "1080p60", "2160p60")
        console.print(table)
        configuration["camera_resolutions"]["default_resolution"] = Prompt.ask(
            "  Which one to choose as the default rendering quality",
            choices=["low", "medium", "high", "ultra_high"],
            default="high"
        )
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3

    print("\n camera_qualities:")
    print("  Four defined qualities: low: 480p15  medium: 720p30  high: 1080p60  ultra_high: 2160p60")
    configuration["camera_qualities"]["default_quality"] = input("  [8/8] Which one to choose as the default rendering quality [low/medium/high/ultra_high]: ")

<<<<<<< HEAD
    with open(file_name, 'w', encoding="utf_8") as file:
        yaml.dump(configuration, file)
=======
        global_file_name = os.path.join(get_manim_dir(), "manimlib", "default_config.yml")
        if scope == "global":
            file_name = global_file_name
        else:
            if os.path.exists(global_file_name):
                remove_empty_value(configuration)
            file_name = os.path.join(os.getcwd(), "custom_config.yml")
        with open(file_name, "w", encoding="utf-8") as f:
            yaml.dump(configuration, f)

        console.print(f"\n:rocket: You have successfully set up a {scope} configuration file!")
        console.print(f"You can manually modify it in: [cyan]`{file_name}`[/cyan]")
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3

    print(f"\nYou have set up a {scope} configuration file")
    print(f"You can manually modify it again in: {file_name}\n")
