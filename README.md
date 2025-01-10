# Calendario in Python

Questo progetto consiste in una semplice classe Python che permette di visualizzare il calendario di un mese specifico o di un anno intero. Utilizza il modulo `calendar` di Python per generare e visualizzare i calendari.

## Funzionalità

- Visualizzare il calendario di un mese specifico.
- Visualizzare il calendario di un anno intero.

## Struttura del Codice

### Classe `Calendario`

La classe `Calendario` contiene due metodi principali:

1. **`__init__(self, anno)`**:
   - Costruttore della classe che accetta un anno come parametro e lo memorizza come attributo della classe.

2. **`visualizza_mese(self, mese)`**:
   - Visualizza il calendario di un mese specificato dell'anno.

3. **`visualizza_anno(self)`**:
   - Visualizza il calendario completo dell'anno.

### Esempio d'Uso

```python
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

# Esempio di utilizzo
calendario_2025 = Calendario(2025)

# Visualizza il calendario di gennaio (mese 1) del 2025
calendario_2025.visualizza_mese(1)

# Visualizza il calendario completo dell'anno 2025
calendario_2025.visualizza_anno()
