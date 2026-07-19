from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+79235692584"),
    Smartphone("Motorolla", "Z-5", "+79056652332"),
    Smartphone("Apple", "13", "+79043633214"),
    Smartphone("Samsyng", "Galaxy A25", "+79082113699"),
    Smartphone("Xiaomi", "Mi 11 Lite 5G", "+79536622214")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.namber}")