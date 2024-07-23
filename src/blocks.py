def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    stripped_blocks = list(map(lambda x: x.strip(), blocks))
    filtered_blocks = list(filter(lambda x: x != "", stripped_blocks))

    return filtered_blocks