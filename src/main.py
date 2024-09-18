import os, shutil
from convert import *


def copy_dir(src, dst):
    if os.path.exists(dst):
        for entry in os.listdir(dst):
            entry_path = os.path.join(dst, entry)
            if os.path.isfile(entry_path):
                os.remove(entry_path)
            else:
                shutil.rmtree(entry_path)
    else:
        os.mkdir(dst)
    for entry in os.listdir(src):
        entry_path = os.path.join(src, entry)
        if os.path.isfile(entry_path):
            print(f"{entry_path} copied to {shutil.copy(entry_path, dst)}")
        else:
            copy_dir(entry_path, os.path.join(dst, entry))
    return


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    new_html = template.replace(
        r"{{ Title }}", title).replace(r"{{ Content }}", html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path):
            if entry[-3:] == ".md":
                html_path = os.path.join(dest_dir_path, entry[:-3] + ".html")
                generate_page(entry_path, template_path, html_path)
        else:
            new_dest_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(entry_path, template_path, new_dest_path)
    return


def main():
    copy_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()