import pandas as pd

def automatyzacja_excela_pandas(plik_wejsciowy, plik_wyjsciowy):
    # Wczytaj dane z pliku Excel (zakładamy, że dane są w pierwszym arkuszu)
    df = pd.read_excel(plik_wejsciowy)
    
    # Dodaj nową kolumnę z przekształconymi danymi
    df["Podwojone Wartości"] = df["Wartości"] * 2
    
    # Zapisz dane do nowego pliku z formatowaniem i wykresem
    with pd.ExcelWriter(plik_wyjsciowy, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Przetworzone Dane")
        
        # Pobierz obiekt workbook i worksheet
        workbook = writer.book
        worksheet = writer.sheets["Przetworzone Dane"]
        
        # Dodaj formatowanie nagłówków
        header_format = workbook.add_format({"bold": True, "align": "center", "bg_color": "#D3D3D3"})
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
        
        # Ustaw szerokość kolumn automatycznie
        for i, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(i, i, max_len)
        
        # Dodaj wykres słupkowy
        chart = workbook.add_chart({"type": "column"})
        chart.add_series({
            "name": "Podwojone Wartości",
            "categories": ["Przetworzone Dane", 1, 0, len(df), 0],  # Kategorie z pierwszej kolumny
            "values": ["Przetworzone Dane", 1, 2, len(df), 2],      # Dane z trzeciej kolumny
        })
        chart.set_title({"name": "Podwojone Wartości"})
        chart.set_x_axis({"name": "Kategorie"})
        chart.set_y_axis({"name": "Wartości"})
        worksheet.insert_chart("E2", chart)

    print(f"Plik został zapisany jako: {plik_wyjsciowy}")

# Przykład użycia:
plik_wejsciowy = "dane.xlsx"  # Plik wejściowy z danymi
plik_wyjsciowy = "dane_przetworzone.xlsx"  # Plik wynikowy
automatyzacja_excela_pandas(plik_wejsciowy, plik_wyjsciowy)
