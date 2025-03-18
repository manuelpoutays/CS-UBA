--Ej1
{- 
    null	[a] -> Bool	¿Está vacía la lista?
    head	[a] -> a	Primer elemento
    tail	[a] -> [a]	Todo excepto el primer elemento
    init	[a] -> [a]	Todo excepto el último elemento
    last	[a] -> a	Último elemento
    take	Int -> [a] -> [a]	Primeros n elementos
    drop	Int -> [a] -> [a]	Elimina primeros n elementos
    (++)	[a] -> [a] -> [a]	Concatena dos listas
    concat	[[a]] -> [a]	Une una lista de listas
    reverse	[a] -> [a]	Invierte la lista
    elem	Eq a => a -> [a] -> Bool	¿El elemento está en la lista?
-}
--Ej2
valorAbsoluto :: Float -> Float
valorAbsoluto n
    |n<0 = -n
    |n>=0 = n