from guizero import App, TextBox, PushButton, Text
####WHILE
app = App("Sumatoria Sigma")
def calcular_sumatoria():
    n = int(input_numero.value)
    resultado = 0
    i = 2
    while i <= 2 * n:
        termino = 2 * (i - 1) + 2 * i
        resultado += termino
        i += 1
    resultado_text.value = (f"El resulado de la sumatoria es: {resultado}")

Text(app, text="Ingrese i:")
input_numero = TextBox(app)
calcular_button = PushButton(app, text="Calcular", command=calcular_sumatoria)
resultado_text = Text(app, text="Resultado: ")
app.display()