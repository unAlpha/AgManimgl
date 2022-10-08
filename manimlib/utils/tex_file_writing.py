<<<<<<< HEAD
import sys
import os
import hashlib
from contextlib import contextmanager
=======
from __future__ import annotations

from contextlib import contextmanager
import os
import re
import yaml
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3

from manimlib.utils.directories import get_tex_dir
<<<<<<< HEAD
from manimlib.config import get_manim_dir
from manimlib.config import get_custom_config
from manimlib.logger import log
=======
from manimlib.utils.simple_functions import hash_string
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3


SAVED_TEX_CONFIG = {}


<<<<<<< HEAD
def get_tex_config():
=======
def get_tex_template_config(template_name: str) -> dict[str, str]:
    name = template_name.replace(" ", "_").lower()
    with open(os.path.join(
        get_manim_dir(), "manimlib", "tex_templates.yml"
    ), encoding="utf-8") as tex_templates_file:
        templates_dict = yaml.safe_load(tex_templates_file)
    if name not in templates_dict:
        log.warning(
            "Cannot recognize template '%s', falling back to 'default'.",
            name
        )
        name = "default"
    return templates_dict[name]


def get_tex_config() -> dict[str, str]:
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3
    """
    Returns a dict which should look something like this:
    {
        "template": "default",
        "compiler": "latex",
        "preamble": "..."
    }
    """
    # Only load once, then save thereafter
    if not SAVED_TEX_CONFIG:
<<<<<<< HEAD
        custom_config = get_custom_config()
        SAVED_TEX_CONFIG.update(custom_config["tex"])
        # Read in template file
        template_filename = os.path.join(
            get_manim_dir(), "manimlib", "tex_templates",
            SAVED_TEX_CONFIG["template_file"],
        )
        with open(template_filename, "r") as file:
            SAVED_TEX_CONFIG["tex_body"] = file.read()
    return SAVED_TEX_CONFIG


def tex_hash(tex_file_content):
    # Truncating at 16 bytes for cleanliness
    hasher = hashlib.sha256(tex_file_content.encode())
    return hasher.hexdigest()[:16]
=======
        template_name = get_custom_config()["style"]["tex_template"]
        template_config = get_tex_template_config(template_name)
        SAVED_TEX_CONFIG.update({
            "template": template_name,
            "compiler": template_config["compiler"],
            "preamble": template_config["preamble"]
        })
    return SAVED_TEX_CONFIG


def tex_content_to_svg_file(
    content: str, template: str, additional_preamble: str
) -> str:
    tex_config = get_tex_config()
    if not template or template == tex_config["template"]:
        compiler = tex_config["compiler"]
        preamble = tex_config["preamble"]
    else:
        config = get_tex_template_config(template)
        compiler = config["compiler"]
        preamble = config["preamble"]
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3

    if additional_preamble:
        preamble += "\n" + additional_preamble
    full_tex = "\n\n".join((
        "\\documentclass[preview]{standalone}",
        preamble,
        "\\begin{document}",
        content,
        "\\end{document}"
    )) + "\n"

<<<<<<< HEAD
def tex_to_svg_file(tex_file_content):
=======
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3
    svg_file = os.path.join(
        get_tex_dir(), hash_string(full_tex) + ".svg"
    )
    if not os.path.exists(svg_file):
        # If svg doesn't exist, create it
        create_tex_svg(full_tex, svg_file, compiler)
    return svg_file


<<<<<<< HEAD
def tex_to_svg(tex_file_content, svg_file):
    tex_file = svg_file.replace(".svg", ".tex")
    with open(tex_file, "w", encoding="utf-8") as outfile:
        outfile.write(tex_file_content)
    svg_file = dvi_to_svg(tex_to_dvi(tex_file))

    # Cleanup superfluous documents
    tex_dir, name = os.path.split(svg_file)
    stem, end = name.split(".")
    for file in filter(lambda s: s.startswith(stem), os.listdir(tex_dir)):
        if not file.endswith(end):
            os.remove(os.path.join(tex_dir, file))

    return svg_file


def tex_to_dvi(tex_file):
    tex_config = get_tex_config()
    program = tex_config["executable"]
    file_type = tex_config["intermediate_filetype"]
    result = tex_file.replace(".tex", "." + file_type)
    if not os.path.exists(result):
        commands = [
            program,
            "-interaction=batchmode",
            "-halt-on-error",
            f"-output-directory=\"{os.path.dirname(tex_file)}\"",
            f"\"{tex_file}\"",
            ">",
            os.devnull
        ]
        exit_code = os.system(" ".join(commands))
        if exit_code != 0:
            log_file = tex_file.replace(".tex", ".log")
            log.error("LaTeX Error!  Not a worry, it happens to the best of us.")
            with open(log_file, "r") as file:
                for line in file.readlines():
                    if line.startswith("!"):
                        log.debug(f"The error could be: `{line[2:-1]}`")
            sys.exit(2)
    return result


def dvi_to_svg(dvi_file, regen_if_exists=False):
    """
    Converts a dvi, which potentially has multiple slides, into a
    directory full of enumerated pngs corresponding with these slides.
    Returns a list of PIL Image objects for these images sorted as they
    where in the dvi
    """
    file_type = get_tex_config()["intermediate_filetype"]
    result = dvi_file.replace("." + file_type, ".svg")
    if not os.path.exists(result):
        commands = [
            "dvisvgm",
            "\"{}\"".format(dvi_file),
            "-n",
            "-v",
            "0",
            "-o",
            "\"{}\"".format(result),
            ">",
            os.devnull
        ]
        os.system(" ".join(commands))
    return result
=======
def create_tex_svg(full_tex: str, svg_file: str, compiler: str) -> None:
    if compiler == "latex":
        program = "latex"
        dvi_ext = ".dvi"
    elif compiler == "xelatex":
        program = "xelatex -no-pdf"
        dvi_ext = ".xdv"
    else:
        raise NotImplementedError(
            f"Compiler '{compiler}' is not implemented"
        )

    # Write tex file
    root, _ = os.path.splitext(svg_file)
    with open(root + ".tex", "w", encoding="utf-8") as tex_file:
        tex_file.write(full_tex)

    # tex to dvi
    if os.system(" ".join((
        program,
        "-interaction=batchmode",
        "-halt-on-error",
        f"-output-directory=\"{os.path.dirname(svg_file)}\"",
        f"\"{root}.tex\"",
        ">",
        os.devnull
    ))):
        log.error(
            "LaTeX Error!  Not a worry, it happens to the best of us."
        )
        with open(root + ".log", "r", encoding="utf-8") as log_file:
            error_match_obj = re.search(r"(?<=\n! ).*", log_file.read())
            if error_match_obj:
                log.debug(
                    "The error could be: `%s`",
                    error_match_obj.group()
                )
        raise LatexError()

    # dvi to svg
    os.system(" ".join((
        "dvisvgm",
        f"\"{root}{dvi_ext}\"",
        "-n",
        "-v",
        "0",
        "-o",
        f"\"{svg_file}\"",
        ">",
        os.devnull
    )))

    # Cleanup superfluous documents
    for ext in (".tex", dvi_ext, ".log", ".aux"):
        try:
            os.remove(root + ext)
        except FileNotFoundError:
            pass
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3


# TODO, perhaps this should live elsewhere
@contextmanager
<<<<<<< HEAD
def display_during_execution(message):
    # Only show top line
    to_print = message.split("\n")[0]
=======
def display_during_execution(message: str):
    # Merge into a single line
    to_print = message.replace("\n", " ")
    max_characters = os.get_terminal_size().columns - 1
    if len(to_print) > max_characters:
        to_print = to_print[:max_characters - 3] + "..."
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3
    try:
        print(to_print, end="\r")
        yield
    finally:
        print(" " * len(to_print), end="\r")
<<<<<<< HEAD
=======


class LatexError(Exception):
    pass
>>>>>>> fb50e4eb55e05c91c01e55fa1713b3ad69fa42e3
