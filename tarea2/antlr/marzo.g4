grammar marzo;

program : expression+ | statement+;

expression: 
    expression '+' expression   #suma
    | Numero                    #primaria
    | Variable                  #var
    ;

statement:
    'int' Variable          #declaracion
    | Variable '=' expression #asignacion
    ;

// A continuación los tokens (comienzan con mayúscula)
Numero : [0-9]+;
Variable : [a-z]+;
WS : [ \t\n\r]+ -> skip ;


