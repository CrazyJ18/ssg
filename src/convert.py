from htmlnode import *
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

def block_to_block_type(block):
    if (block[:2] == "# "or block[:3] == "## " or block[:4] == "### " or
        block[:5] == "#### " or block[:6] == "##### " or 
        block[:7] == "###### "):
        return "heading"
    block_lines = block.splitlines()
    if block_lines[0] == "```" and block_lines[-1] == "```":
        return "code"
    for line in block_lines:
        if line[0] != ">":
            break
    else:
        return "quote"
    for line in block_lines:
        if line[:2] != "* " and line[:2] != "- ":
            break
    else:
        return "unordered_list"
    for i in range(len(block_lines)):
        li_num = f"{i + 1}"
        if block_lines[i][:len(li_num) + 2] != li_num + ". ":
            break
    else:
        return "ordered_list"
    return "paragraph"


def markdown_to_html_node(markdown):
    block_nodes = []
    for block in markdown_to_blocks(markdown):
        match block_to_block_type(block):
            case "paragraph":
                block_nodes.append(ParentNode("p", text_to_children(block)))
            case "heading":
                split_block = block.split(" ", 1)
                block_nodes.append(ParentNode(
                    f"h{len(split_block[0])}", 
                    text_to_children(split_block[1])))
            case "quote":
                text_lines = get_text_lines(block, 1)
                text = ""
                for line in text_lines[:-1]:
                    text += line + "\n"
                text += text_lines[-1]
                block_nodes.append(ParentNode(
                    "blockquote", text_to_children(text)))
            case "code":
                inner_node = ParentNode("code", text_to_children(block[4:-4]))
                block_nodes.append(ParentNode("pre", [inner_node]))
            case "unordered_list":
                text_lines = get_text_lines(block, 2)
                list_items = get_list_items(text_lines)
                block_nodes.append(ParentNode("ul", list_items))
            case "ordered_list":
                text_lines = get_text_lines(block, 2, True)
                list_items = get_list_items(text_lines)
                block_nodes.append(ParentNode("ol", list_items))
    return ParentNode("div", block_nodes)

def get_text_lines(block, offset, ordered=False):
    split_block = block.split("\n")
    text_lines = []
    match ordered:
        case True:
            for i in range(len(split_block)):
                text_lines.append(split_block[i][offset + len(f"{i + 1}"):])
        case _:
            for line in split_block:
                text_lines.append(line[offset:])
    return text_lines

def get_list_items(text_lines):
    list_items = []
    for line in text_lines:
        list_items.append(ParentNode("li", text_to_children(line)))
    return list_items

def text_to_children(text):
    html_nodes = []
    for node in text_to_textnodes(text):
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes