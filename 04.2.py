from guizero import App, TextBox, PushButton, Text
####FOR
app = App("Calculadora de Sumatoria")
def calcular_sumatoria():
    valor_i = int(input_i.value)
    resultado = 0

    for i in range(1, valor_i + 1):
        resultado += (i - 1) ** 3 + i ** 3

    resultado_text.value = f"Resultado: {resultado}"

i_text = Text(app, "Valor de i:")
input_i = TextBox(app, width=5)
calcular_button = PushButton(app, text="Calcular", command=calcular_sumatoria)
resultado_text = Text(app, "")
app.display()