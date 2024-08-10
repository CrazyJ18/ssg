from htmlnode import LeafNode
from splitnodes import *

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(value=text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("bad text type")

def text_to_textnodes(text):
    nodes = split_nodes_image([TextNode(text, text_type_text)])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    return split_nodes_delimiter(nodes, "`", text_type_code)

def markdown_to_blocks(markdown):
    blocks = []
    for s in markdown.split("\n\n"):
        stripped = s.strip()
        if stripped != "":
            blocks.append(stripped)
    return blocks