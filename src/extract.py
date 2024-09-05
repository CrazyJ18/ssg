import re

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)]\((.*?)\)", text)


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("no title")