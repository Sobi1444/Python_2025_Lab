import tkinter as tk
from random import randint


class KostkaGUI:
    def __init__(self):
        self.okno = tk.Tk()
        self.okno.title("Symulator rzutu kostka")
        self.okno.geometry("350x300")
        self.okno.config(bg="#2c3e50")

        self.stworz_interfejs()

    def stworz_interfejs(self):
        naglowek = tk.Label(self.okno, text="Rzut kostka",
                            font=("Courier", 18, "bold"),
                            bg="#2c3e50", fg="white")
        naglowek.pack(pady=15)

        # Wynik
        self.wynik_label = tk.Label(self.okno, text="—",
                                    font=("Arial", 80, "bold"),
                                    bg="#34495e", fg="#ecf0f1",
                                    width=5, height=2)
        self.wynik_label.pack(pady=20)

        # Przycisk
        btn = tk.Button(self.okno, text="RZUC",
                        command=self.wykonaj_rzut,
                        font=("Arial", 14),
                        bg="green", fg="white",
                        activebackground="#c0392b",
                        relief=tk.RAISED, bd=3)
        btn.pack(pady=15)

    def wykonaj_rzut(self):
        liczba = randint(1, 6)
        self.wynik_label.config(text=str(liczba))

    def uruchom(self):
        self.okno.mainloop()


# Program głowny
if __name__ == "__main__":
    aplikacja = KostkaGUI()
    aplikacja.uruchom()