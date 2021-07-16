# lfya-lab-encrypt-decrypt
Trabajo de Laboratorio de Lenguajes Formales y Autómatas 2021

Una funcion biyectiva tiene la forma:
f(x)=(ax+b) mod m

f será una biyección, si y solo si, mcd(a, n) = 1 (máximo común divisor)

Si esto pasa, podemos definir su inversa 
f−1(x) = (kx + c) mod n

Donde:
- k es un número entero tal que 1 = ak + nm para algún número entero m.
- c es un numero entero tal que, f(c) = 0

Calculamos mcd(a, n) para la función f(x) = (2x + 5) mod 95:
- mcd(2, 95) = 1, entonces f es una biyección

Buscamos la inversa f−1(x) = (kx + c) mod n con f(c) = 0:
- usando teorema de la division, despejamos c:
- (2c + 5) = 95C
- c = (95C - 5) / 2
- dar un valor a C de forma que c de entero:
- con C = 1, c = (95*1 - 5) / 2 = 90 / 2 = 45
- obtener el entero k tal que 1 = 2k + 95m para algun entero m
- despejando k y con m = -1, k = (1 - 95*(-1)) / 2 = 96 / 2 = 48
- k = 48, c = 45
- f−1(x) = (kx + c) mod n = (48x + 45) mod 95

Para probar el programa se debe poner un archivo llamado `input.txt` en la raiz del proyecto
Comando para encryptar:
`py encrypt.py` 

Comando para desencryptar (se necesita un archivo `output.txt`, resultado del comando anterior):
`py decrypt.py`


TODO variabilizar parametros