from textnode import *
from extract import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            split_text_len = len(split_text)
            if split_text_len % 2 == 0:
                raise Exception("no closing delimiter")
            split_nodes = []
            for i in range(split_text_len):
                if i % 2 == 0:
                    split_nodes.append(TextNode(split_text[i], text_type_text))
                else:
                    split_nodes.append(TextNode(split_text[i], text_type))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
        else:
            text = node.text
            for image in images:
                sections = text.split(f"![{image[0]}]({image[1]})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], text_type_text))
                new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                text = sections[1]
            if text != "":
                new_nodes.append(TextNode(text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
        else:
            text = node.text
            for link in links:
                sections = text.split(f"[{link[0]}]({link[1]})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], text_type_text))
                new_nodes.append(TextNode(link[0], text_type_link, link[1]))
                text = sections[1]
            if text != "":
                new_nodes.append(TextNode(text, text_type_text))
    return new_nodes

#nodes = [TextNode("This is text with ![two](path/to/image1) ![images](path/to/image2)", text_type_text)]

#print(split_nodes_image(nodes))