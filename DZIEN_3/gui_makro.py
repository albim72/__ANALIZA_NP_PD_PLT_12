import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

class ExcelAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatyzacja Excela")
        
        # Plik wejściowy
        Label(root, text="Plik wejściowy:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.input_file_entry = Entry(root, width=50)
        self.input_file_entry.grid(row=0, column=1, padx=10, pady=10)
        Button(root, text="Wybierz", command=self.choose_input_file).grid(row=0, column=2, padx=10, pady=10)
        
        # Plik wyjściowy
        Label(root, text="Plik wynikowy:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.output_file_entry = Entry(root, width=50)
        self.output_file_entry.grid(row=1, column=1, padx=10, pady=10)
        Button(root, text="Wybierz", command=self.choose_output_file).grid(row=1, column=2, padx=10, pady=10)
        
        # Przycisk przetwarzania
        Button(root, text="Przetwórz plik", command=self.process_file, bg="green", fg="white").grid(row=2, column=0, columnspan=3, pady=20)
        
    def choose_input_file(self):
        file_path = filedialog.askopenfilename(
            title="Wybierz plik Excela",
            filetypes=[("Pliki Excel", "*.xlsx *.xls")]
        )
        if file_path:
            self.input_file_entry.delete(0, "end")
            self.input_file_entry.insert(0, file_path)
    
    def choose_output_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Zapisz wynikowy plik Excela",
            defaultextension=".xlsx",
            filetypes=[("Pliki Excel", "*.xlsx")]
        )
        if file_path:
            self.output_file_entry.delete(0, "end")
            self.output_file_entry.insert(0, file_path)
    
    def process_file(self):
        input_file = self.input_file_entry.get()
        output_file = self.output_file_entry.get()
        
        if not input_file or not output_file:
            messagebox.showerror("Błąd", "Musisz wybrać plik wejściowy i miejsce zapisu pliku wynikowego.")
            return
        
        try:
            # Przetwarzanie pliku
            self.automatyzacja_excela_pandas(input_file, output_file)
            messagebox.showinfo("Sukces", f"Plik został zapisany jako: {output_file}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił problem: {e}")
    
    def automatyzacja_excela_pandas(self, plik_wejsciowy, plik_wyjsciowy):
        # Wczytaj dane z pliku Excel
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

# Tworzenie okna aplikacji
if __name__ == "__main__":
    root = Tk()
    app = ExcelAutomationApp(root)
    root.mainloop()
