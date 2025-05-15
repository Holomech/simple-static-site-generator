from textnode import TextType, TextNode

def main():
    text_node = TextNode("example anchor text", TextType.LINK, "https://www.example.com")
    print(text_node)

main()
