print("Tämä ohjelma muuntaa fahrenheitit celsius asteiksi.")
fahrenheit = input("Anna lämpötila fahrenheit yksikössä ")

celsius = (float(fahrenheit) - 32) * 5 / 9

print("Konversion tulos: " + str(celsius))