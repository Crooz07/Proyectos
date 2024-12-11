class HistorialNavegador:
    def __init__(self):
        self.historial = []

    def visitar(self, url):
        self.historial.append(url)

    def atras(self):
        if self.historial:
            return self.historial.pop()
        return None


historial = HistorialNavegador()
historial.visitar("google.com")
historial.visitar("youtube.com")
print("Historial atrás:", historial.atras())
