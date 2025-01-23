import hashlib

# Przykładowy ciąg znaków
album_jako_string = "272409"

# Obliczanie skrótu MD5
md5_hash = hashlib.md5(album_jako_string.encode()).hexdigest()

# Wyświetlenie wyniku
print("MD5 hash:", md5_hash)