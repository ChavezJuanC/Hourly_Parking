from math import ceil;
from datetime import datetime;

# Constantes de tarifa
BASE_CHARGE: float = 20.00;
HOURLY_RATE: float = 20.00;
ADDITIONAL_15MIN_RATE: float = 5.00;

# Variables globales
totalHours: int = 0;
total15MinIntervals: int = 0;
totalCost: float = 0.0;
# Declaración de variable para almacenar el objeto datetime
totalTime: datetime | None = None;

# Solicita al usuario el tiempo total transcurrido
def requestTotalTime() -> datetime:
    while True:
        try:
            # Lectura de la entrada
            total_time = input("Tiempo total(HH:MM):");
            # Conversión del formato de texto a obj datetime
            hm_obj = datetime.strptime(total_time, "%H:%M");
            return hm_obj;

        # Captura de error por formato de hora incorrecto
        except ValueError:
            print("Favor de verificar formato de HH:MM");
            # Reintentar la lectura hasta obtener una entrada válida

# Calcula la cantidad de fracciones de 15 minutos a cobrar
def set15MinIntervals(total_minutes: int) -> int:
    # Calcula las fracciones de 15 minutos cobrables mediante redondeo hacia arriba.
    # Desde que se arrebasa el minuto, se cobran los proximos 15 minutos.
    return ceil(total_minutes / 15);

# Calcula el costo total según las horas y fracciones transcurridas
def calculateTotalCost(t_hours: int, t_intervals: int, h_rate: float, additional_15min_rate: float, base_rate: float) -> float:
    # Previene horas negativas cuando t_hours es 0
    billed_hours = max(0, t_hours - 1);
    return ((base_rate) + (billed_hours * h_rate) + (t_intervals * additional_15min_rate));

def main():
    programRunning: bool = True;

    while programRunning:
        # Variables globales
        global totalHours, total15MinIntervals, totalCost, HOURLY_RATE, ADDITIONAL_15MIN_RATE, totalTime, BASE_CHARGE;

        # Obtención del tiempo
        totalTime = (requestTotalTime());
        totalHours = (totalTime.hour);
        total15MinIntervals = set15MinIntervals(totalTime.minute);

        # Cálculo del total a pagar
        totalCost = calculateTotalCost(totalHours, total15MinIntervals, HOURLY_RATE, ADDITIONAL_15MIN_RATE, BASE_CHARGE);

        # Mostrar total al usuario
        print("Total: ${}".format(f"{totalCost:05.2f}"))

        # Continuidad
        wishToContinue = input("(1) para continuar, (Cualquier otra tecla para terminar) para terminar: ");
        if (wishToContinue == "1"):
            programRunning = True;
        else:
            programRunning = False;

# Programa principal, no módulo.
if __name__ == "__main__":
    main()