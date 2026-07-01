grammar Expr;

root: expr EOF;

expr: EOF;
NUM: [0-9]+;
RESTA: '-';
WS : [ \t\r\n]+ -> skip ;