from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "55555555555"),
    Smartphone("Motorolla", "Z-5", "22222222222"),
    Smartphone("Apple", "13", "66666666666"),
    Smartphone("Samsyng", "Galaxy A25", "33333333333"),
    Smartphone("Xiaomi", "Mi 11 Lite 5G", "88888888888")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.namber}")