from MarkdownParser import MarkdownParser
from MarkdownVisitor import MarkdownVisitor

class MarkdownToHtmlVisitor(MarkdownVisitor):

    def visitDocument(self, ctx: MarkdownParser.DocumentContext):
        html = []
        for child in ctx.children:
            result = self.visit(child)
            if result is not None:
                html.append(result)
        return ''.join(html)

    def visitHeader(self, ctx: MarkdownParser.HeaderContext):
        level = len(ctx.HEADER().getText())
        text = ctx.TEXT().getText()
        return f"<h{level}>{text}</h{level}>"

    def visitParagraph(self, ctx: MarkdownParser.ParagraphContext):
        html = []
        for child in ctx.children:
            result = self.visit(child)
            if result is not None:
                html.append(result)
        return f"<p>{''.join(html)}</p>\n"

    def visitList(self, ctx: MarkdownParser.ListContext):
        html = []
        for item in ctx.children:
            result = self.visit(item)
            if result is not None:
                html.append(result)
        return ''.join(html)

    def visitCodeBlock(self, ctx: MarkdownParser.CodeBlockContext):
        code = ''.join([text.getText() for text in ctx.TEXT()])
        return f"<pre><code>{code}</code></pre>\n"

    def visitUnorderedList(self, ctx: MarkdownParser.UnorderedListContext):
        return f"<ul><li>{self.visit(ctx.text())}</li></ul>\n"

    def visitOrderedList(self, ctx: MarkdownParser.OrderedListContext):
        items = [self.visit(child) for child in ctx.children if child.getText().strip()]
        return f"<ol>{''.join(f'<li>{item}</li>' for item in items)}</ol>\n"

    def visitBold(self, ctx: MarkdownParser.BoldContext):
        return f"<strong>{self.visit(ctx.text())}</strong>"

    def visitItalic(self, ctx: MarkdownParser.ItalicContext):
        return f"<em>{self.visit(ctx.text())}</em>"

    def visitText(self, ctx: MarkdownParser.TextContext):
        return ctx.getText()

    def visitNewline(self, ctx: MarkdownParser.NewlineContext):
        return "\n"