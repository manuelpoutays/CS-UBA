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

bisiesto :: Int -> Bool
bisiesto n
    |n `mod` 100 == 0 && n `mod` 400 == 0 = True
    |n `mod` 4 == 0 && n `mod` 100 /= 0 = True
    |otherwise = False

factorial :: Int -> Int
factorial 0 = 0
factorial 1 = 1
factorial n = n*factorial(n-1)

--Meto un entero ->Calculo lista de divisores -> Recorro la lista 
esPrimo :: Int -> Int -> Bool
esPrimo n 0 = True
esPrimo n 1 = True
esPrimo n d
    |mod n d == 0 = False
    |otherwise = esPrimo n (d-1)
divisoresAux :: Int -> Int -> Int
divisoresAux n 0 = 0
divisoresAux n d
    |mod n d == 0 && esPrimo d (d-1) = 1 + divisoresAux n (d-1)
    |otherwise = divisoresAux n (d-1)
cantDivisoresPrimos :: Int -> Int
cantDivisoresPrimos n = divisoresAux n n

--Ej 3
--Los parametros de entrada de Either son del estilo aEntero (Left 1) o aEntero(Right True)
inverso :: Float -> Maybe Float
inverso 0 = Nothing
inverso n = Just (1/n)

aEntero :: Either Int Bool -> Int
aEntero (Left n) = n
aEntero (Right b) = if b then 1 else 0

--Ej 4
limpiar :: String->String->String
