from guizero import App, TextBox, PushButton, Text
####WHILE
app = App("Notación de Producto ∏") 
def calcular_productoria():
    n = int(input_numero.value)
    resultado_productoria = 1  
    for i in range(1, n + 1):
        termino = (i - 1) * i
        resultado_productoria *= termino
    resultado_productoria_text.value = f"El resultado de la notacion es: {resultado_productoria}"

Text(app, text="Ingrese i:")
input_numero = TextBox(app)
calcular_button = PushButton(app, text="Calcular", command=calcular_productoria)
resultado_productoria_text = Text(app, text="Resultado de la notación de producto: ")
app.display()