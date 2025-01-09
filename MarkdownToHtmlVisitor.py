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

    def visitList(self, ctx: MarkdownParser.ListContext):
        html = []
        for child in ctx.children:
            result = self.visit(child)
            if result:
                html.append(result)
        return ''.join(html)

    def visitCodeBlock(self, ctx: MarkdownParser.CodeBlockContext):
        code = '\n'.join([text.getText() for text in ctx.TEXT()])
        return f"<pre><code>{code}</code></pre>\n"

    def visitUnorderedList(self, ctx: MarkdownParser.UnorderedListContext):
        items = ctx.text()
        if not isinstance(items, list):
            items = [items]
        list_items = ''.join(f"<li>{self.visit(item)}</li>" for item in items)
        return f"<ul>{list_items}</ul>\n"

    def visitOrderedList(self, ctx: MarkdownParser.OrderedListContext):
        items = []
        for child in ctx.children:
            if isinstance(child, MarkdownParser.TextContext):
                items.append(f"<li>{child.getText().strip()}</li>")
        return f"<ol>{''.join(items)}</ol>\n"

    def visitLink(self, ctx: MarkdownParser.LinkContext):
        text = ctx.TEXT(0)
        url = ctx.TEXT(1).getText().replace(')', '')
        return f'<a href="{url}">{text}</a>\n'

    def visitImage(self, ctx: MarkdownParser.ImageContext):
        alt = ctx.TEXT(0).getText() if len(ctx.TEXT()) > 1 else ''
        src = ctx.TEXT(1).getText().replace(')', '')

        if alt:
            return f'<img src="{src}" alt="{alt}">\n'
        else:
            return f'<img src="{src}">\n'

    def visitParagraph(self, ctx: MarkdownParser.ParagraphContext):
        html = []
        for child in ctx.children:
            result = self.visit(child)
            if result is not None:
                result.replace('\n', '')
                html.append(result)
        return f"<p>{''.join(html)}</p>\n"

    def visitBold(self, ctx: MarkdownParser.BoldContext):
        items = ctx.text()
        if not isinstance(items, list):
            items = [items]
        bold_text = ''.join(self.visit(item) for item in items)
        return f"<strong>{bold_text}</strong>"

    def visitItalic(self, ctx: MarkdownParser.ItalicContext):
        items = ctx.text()
        if not isinstance(items, list):
            items = [items]
        italic_text = ''.join(self.visit(item) for item in items)
        return f"<em>{italic_text}</em>"

    def visitBolditalic(self, ctx: MarkdownParser.BolditalicContext):
        items = ctx.text()
        if not isinstance(items, list):
            items = [items]
        bolditalic_text = ''.join(self.visit(item) for item in items)
        return f"<strong><em>{bolditalic_text}</em></strong>"

    def visitText(self, ctx: MarkdownParser.TextContext):
        return ctx.getText()

    def visitNewline(self, ctx: MarkdownParser.NewlineContext):
        return "\n"