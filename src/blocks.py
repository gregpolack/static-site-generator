def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    stripped_blocks = list(map(lambda x: x.strip(), blocks))
    filtered_blocks = list(filter(lambda x: x != "", stripped_blocks))

    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    heading_prefixes = ["# ", "## ", "### ", "#### ", "##### ", "###### " ]

    if block.startswith(tuple(heading_prefixes)):
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"