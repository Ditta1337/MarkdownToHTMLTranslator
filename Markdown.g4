grammar Markdown;

// Parser Rules
document: (header | list | image | link | paragraph | bolditalic | bold | italic | codeBlock | newline)+;

header: HEADER WS? TEXT newline*;
list: (unorderedList | orderedList)+;
unorderedList: (('*' | '-') WS? text)+ newline*;
orderedList: (ORDERED_LIST WS? text NEWLINE)+;
codeBlock: '```' NEWLINE (TEXT NEWLINE)* '```' newline*;
image: '![' TEXT? ']' '(' TEXT newline*;
link: '[' TEXT ']' '(' TEXT newline*;
paragraph: (text | bold | italic | bolditalic | SYMBOLS | DIGIT+ | WS)+ newline*;
bolditalic: '***' text '***';
bold: '**' text '**';
italic: '*' text '*';
text: TEXT | SPACE;
newline: NEWLINE;

// Lexer Rules
HEADER: '#' | '##' | '###' | '####' | '#####' | '######';
SYMBOLS: [!'"#$%&()+,-./:;<=>?@\\^_{|}~];
DIGIT: [0-9];
SPACE: ' ';
ORDERED_LIST: [0-9]+ '.' SPACE;
TEXT: WS? [\p{L}] ([\p{L}\p{N}] | SYMBOLS | SPACE)*;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
ESC: '\\"'|'\\\\';
