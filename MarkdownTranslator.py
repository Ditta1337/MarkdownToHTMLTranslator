import sys
from antlr4 import *
from MarkdownLexer import MarkdownLexer
from MarkdownParser import MarkdownParser
from MarkdownToHtmlVisitor import MarkdownToHtmlVisitor


def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = MarkdownLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MarkdownParser(stream)
    tree = parser.document()

    visitor = MarkdownToHtmlVisitor()
    html = visitor.visit(tree)

    output_file = input_file.rsplit('.', 1)[0] + '.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Translation complete. Output saved to {output_file}")


if __name__ == '__main__':
    main(sys.argv)
