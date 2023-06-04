from tkinter import Tk, Label, Button, Entry, messagebox

class CoffeeShop:
    def __init__(self):
        self.menu = {
            "Espresso": 20000,
            "Cappuccino": 25000,
            "Latte": 30000,
            "Mocha": 35000,
            "Americano": 25000
        }
        self.orders = []
        self.total_price = 0

    def add_order(self, item, quantity):
        if item in self.menu:
            order_price = self.menu[item] * quantity
            self.orders.append((item, quantity, order_price))
            self.total_price += order_price
            messagebox.showinfo("Pesanan", f"{quantity} {item} berhasil ditambahkan dalam pesanan.")
        else:
            messagebox.showerror("Pesanan", f"{item} tidak tersedia dalam menu.")

    def view_order(self):
        if not self.orders:
            messagebox.showerror("Pesanan", "Lo kaga pesen apa-apaan, Fren.")
        else:
            order_summary = "Pesanan Lo:\n\n"
            for item, quantity, price in self.orders:
                order_summary += f"{item} x {quantity}: Rp. {price}\n"
            order_summary += f"\nJumlah harga: Rp. {self.total_price}"
            messagebox.showinfo("Pesanan", order_summary)

    def reset_order(self):
        self.orders = []
        self.total_price = 0
        messagebox.showinfo("Pesanan", "Pesanan lo diatur ulang.")


class Application:
    def __init__(self, window):
        self.window = window
        self.window.title("Tugas Akhir")
        self.window.geometry("300x320")

        self.menu_label = Label(window, text="KOPI TUGAS AKHIR", font=("Arial", 14, "bold"))
        self.menu_label.pack()
        
        self.menu_label = Label(window, text="Espresso, 20K", font=("Arial", 11, "bold"))
        self.menu_label.pack()
       
        self.menu_label = Label(window, text="Cappuccino, 25K", font=("Arial", 11, "bold"))
        self.menu_label.pack()

        self.menu_label = Label(window, text="Latte, 30K", font=("Arial", 11, "bold"))
        self.menu_label.pack()

        self.menu_label = Label(window, text="Mocha, 35K", font=("Arial", 11, "bold"))
        self.menu_label.pack()

        self.menu_label = Label(window, text="Americano, 25K", font=("Arial", 11, "bold"))
        self.menu_label.pack()

        self.label_item = Label(window, text="Mau pesen apa, Fren?")
        self.label_item.pack()
        self.entry_item = Entry(window)
        self.entry_item.pack()

        self.label_quantity = Label(window, text="Mau berapa, Fren?")
        self.label_quantity.pack()
        self.entry_quantity = Entry(window)
        self.entry_quantity.pack()

        self.button_add = Button(window, text="Tambahkan Pesanan Lo", command=self.add_to_order)
        self.button_add.pack()

        self.button_view = Button(window, text="Liat Pesanan Lo", command=self.view_order)
        self.button_view.pack()

        self.button_reset = Button(window, text="Atur Ulang Pesanan Lo", command=self.reset_order)
        self.button_reset.pack()

        self.coffee_shop = CoffeeShop()

    def add_to_order(self):
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()

        if not quantity:
            messagebox.showerror("Pesanan", "Masukkan pesanan lo dulu, Fren.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Pesanan", "Jumlah pesanan harus berupa angka, Fren.")
            return

        self.coffee_shop.add_order(item, quantity)

        self.entry_item.delete(0, 'end')
        self.entry_quantity.delete(0, 'end')

    def view_order(self):
        self.coffee_shop.view_order()

    def reset_order(self):
        self.coffee_shop.reset_order()


root = Tk()
app = Application(root)

root.mainloop()