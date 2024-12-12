grammar Markdown;

// Parser
document: (header | list | codeBlock | paragraph | bold | italic | text | newline)+;

header: HEADER WS? TEXT NEWLINE;
paragraph: (text | bold | italic)+ NEWLINE;
list: (unorderedList | orderedList)+;
unorderedList: ('*' | '-') WS? text NEWLINE;
orderedList: (ORDERED_LIST WS? text NEWLINE)+;
codeBlock: '```' NEWLINE (TEXT NEWLINE)* '```' NEWLINE;
bold: '**' text '**';
italic: '*' text '*';
text: TEXT;
newline: NEWLINE;

// Lexer
HEADER: '#' | '##' | '###' | '####' | '#####' | '######';
ORDERED_LIST: [0-9]+ '.';
TEXT: ~[\r\n*#\-]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;