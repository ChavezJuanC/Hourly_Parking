# 🚗 Sistema de Cobro para Estacionamiento (Parking Charge Calculator)

Este es un programa sencillo en Python desarrollado para el cálculo de tarifas de estacionamiento basándose en el tiempo total transcurrido. El sistema procesa entradas en formato de horas y minutos (`HH:MM`), aplicando una tarifa base por la primera hora y cobrando fracciones adicionales de 15 minutos.

---

## 📌 ¿Cómo funciona la lógica de cobro?

El cálculo del total a pagar se divide en dos partes: **horas completas** e **intervalos de 15 minutos**.

1. **Tarifa Base:** $20.00 MXN (cubre la primera hora de uso).
2. **Hora Adicional:** $20.00 MXN por cada hora extra después de la primera.
3. **Fracciones de 15 minutos:** $5.00 MXN por cada fracción transcurrida (se redondea hacia arriba usando cálculo de intervalos).

| Tiempo de Estancia | Desglose del Cobro | Total a Pagar |
| :--- | :--- | :--- |
| **00:10** | Tarifa base ($20) + 1 fracción ($5) | **$25.00** |
| **01:00** | Tarifa base ($20) + 0 fracciones | **$20.00** |
| **01:15** | Tarifa base ($20) + 1 fracción ($5) | **$25.00** |
| **02:30** | Tarifa base ($20) + 1 hr extra ($20) + 2 fracciones ($10) | **$50.00** |

---

## 🛠️ Requisitos e Instalación

No necesitas instalar librerías externas. El script utiliza únicamente módulos nativos del lenguaje.

* **Python 3.10** o superior (necesario para el soporte de anotaciones de tipo `|`).

### Ejecución

1. Clona el repositorio o descarga el archivo `.py`:
   ```bash
   https://github.com/ChavezJuanC/Hourly_Parking.git
  
