import calendar
class Calendario: 
    def __init__(self, anno):
        self.anno = anno 
    def visualizza_mese(self, mese):
     """Visualizza il calendario di un mese specifico"""
     print(calendar.month(self.anno, mese))
    def visualizza_anno(self):
     """Visualizza il calendario di un anno completo"""
     print(calendar.calendar(self.anno))

calendario_2025 = Calendario(2025)
calendario_2025.visualizza_mese(1)
calendario_2025.visualizza_anno()