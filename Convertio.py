import customtkinter as ctk

class View:
    def __init__(self) -> None:
        """
        This class creates a GUI for converting numbers between different bases.
        """
        
        self.base = None
        self.app = ctk.CTk()
        self.frame = ctk.CTkFrame(self.app, width=400, height=600)
        self.app.iconbitmap(default="icon.ico")
        self.app.geometry('500x700')
        self.app.title("Convertio")
        self.frame.place(in_=self.app, anchor="center", relx=0.5, rely=0.5)

        title = ctk.CTkLabel(self.frame, text="Convertio", font=ctk.CTkFont(family="Helvetica", size=36, weight="bold"))
        self.numEntry = ctk.CTkEntry(self.frame, placeholder_text='Number', width=200)
        label = ctk.CTkLabel(self.frame, text="Number base:", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"))
        base = ctk.CTkComboBox(self.frame, values=['2', '8', '10', '16'], command=self.baseSelect, width=60)
        convertbtn = ctk.CTkButton(self.frame, text="Convert", command=lambda: self.convert(self.numEntry.get()))
        responselabel = ctk.CTkLabel(self.frame, text="Converted number:", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"))
        self.responsebox = ctk.CTkTextbox(self.frame, width=200, height=80)

        title.pack(padx=10, pady=10)
        self.numEntry.pack(padx=10, pady=10)
        label.pack(padx=5, pady=5)
        base.pack(padx=10, pady=10)
        convertbtn.pack(padx=10, pady=10)
        responselabel.pack(padx=10, pady=10)
        self.responsebox.pack(padx=10, pady=10)
        self.app.mainloop()

    def baseSelect(self, e):
        # This function is called when the user selects a new base
        self.base = e

    def convert(self, num):
        # Ensure that Decrypt is initialized and used correctly
        if self.base is not None:
            decryptor = Decrypt()
            results = decryptor.convertall(num, int(self.base))
            results = f'Decimal: {results[0]}\nHexadecimal: {results[1]}\nOctal: {results[2]}\nBinary: {results[3]}'
            self.responsebox.delete(1.0, ctk.END)
            self.responsebox.insert(ctk.END, results)

class Decrypt:
    # This class contains the logic for converting numbers between different bases
    def __init__(self) -> None:
        self.hexAlphabet = [str(x) for x in range(1, 10)] + ["A", "B", "C", "D", "E", "F"]

    def convertall(self, num, base):
        try:
            decimalNum = self.baseToDecimal(num, base)
            hexNum = self.decimalToBase(decimalNum, 16)
            octNum = self.decimalToBase(decimalNum, 8)
            binNum = self.decimalToBase(decimalNum, 2)

            results = [decimalNum, hexNum, octNum, binNum]
        except Exception as e:
            return 
        return results

    def decimalToBase(self, num, base):
        rest = []
        while num > 0:
            rest.append(num % base)
            num = num // base

        if base == 16:
            result = [self.hexAlphabet[index-1] for index in reversed(rest)]
            result = ''.join(map(str, result))
            return result

        result = ''.join(map(str, reversed(rest)))
        return result

    def baseToDecimal(self, num, base):
        num = list(reversed(str(num)))
        decimal = []
        for j, nu in enumerate(num):
            if base == 16 and nu.upper() in self.hexAlphabet:
                i = self.hexAlphabet.index(nu.upper()) + 1
            else:
                i = int(nu)
            decimal.append(i * (base ** j))
        return sum(decimal)

if __name__ == "__main__":
    view = View()
