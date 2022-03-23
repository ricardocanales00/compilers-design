grammar prueba;

program : expression+ ;

expression:
    expression '+' expression #suma
    | Numero                  #primaria
    ;

statement:
    'if' expression 'then' statement ('else' statement) ?   #if
    ;

Numero : [0-9]+;

WS : [ \t\n\r]+ -> skip ;