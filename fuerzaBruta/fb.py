# ejemplo de cifrado cesar con Rot8: Mabw ma cv mrmuxtw i ncmzhi jzcbi lmt kqnzilw Kmaiz
# ejemplo de cifrado cesar con Rot17: Vjkf vj le vavdgcf r wlviqr silkr uvc tzwiruf Tvjri
# ejemplo de cifrado cesar con Rot0 Ftup ft vo fkfnqmp b gvfsab csvub efm djgsbep Dftbs
def cifradoAfin(caracter, a, b):
    if caracter.isalpha():
        if caracter.islower():
            caracter_index = (ord(caracter) - ord('a'))
            caracterDescifrado_index = (a * (caracter_index - b)) % 26
            caracterDescifrado = chr(caracterDescifrado_index + ord('a'))
            return caracterDescifrado
        elif caracter.isupper():
            caracter_index = (ord(caracter) - ord('A'))
            caracterDescifrado_index = (a * (caracter_index - b)) % 26
            caracterDescifrado = chr(caracterDescifrado_index + ord('A'))
            return caracterDescifrado
    return caracter

def descifradoFuerzaBruta(textoCifrado ):
    with open("descifrado.txt", 'w') as f:
        for a in range(1, 26):
            for b in range(26):
                textoDescifrado = ''.join(cifradoAfin(c, a, b) for c in textoCifrado)
                resultado = f"a={a}, b={b}: {textoDescifrado}\n"
                f.write(resultado)

with open("texto_cifrado.txt", "r") as file:
    textoCifrado = file.read()

print("Procesando...")

descifradoFuerzaBruta(textoCifrado)

print("El texto ha sido decifrado.")
