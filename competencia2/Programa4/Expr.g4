grammar Expr;

root: expr EOF;

expr: EOF;
ID: [a-zA-Z]+;
IF: 'if';

MAYOR_QUE: '>';
NUM: [0-9]+;
WS : [ \t\r\n]+ -> skip ;