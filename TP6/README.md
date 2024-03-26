# TPC6: Gramtica Independente de Contexto

## Alexandra Santos, a94523

## Resumo

Exemplo da linguagem:

    ?a
    b=a*2/(27-3)
    !a+b
    c=a*b/(a/b)

Ter em conta:

- Prioridade dos operadores
- Garantir que é LL(1)
- Calcular os Look Ahead para todas as regras de produção

## Resolução

    T =  {'?', '!', '=', '+', '-', '*', '/', '(', ')', id, num}

    N = {S, Exp1, Exp2, Exp3, Op1, Op2}

    S = S

    P = {
    
        S -> '?' id             LA = {'?'}
        | '!' Exp1              LA = {'!'}
        | id '=' Exp1           LA = {id}

        Exp1 -> Exp2 Op1        LA = {'(', num, id}

        Op1 -> '+' Exp1         LA = {'+'}
            | '-' Exp1          LA = {'-'}
            | &                 LA = {')', $}

        Exp2 -> Exp3 Op2        LA = {'(', num, id}

        Op2 -> '*' Exp1         LA = {'*'}
            | '/' Exp1          LA = {'/'}
            | &                 LA = {'+', '-', ')', $}

        Exp3 -> '(' Exp1 ')'    LA = {'('}
            | num               LA = {num}
            | id                LA = {id}

    }