import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ParkingSlot:
    def __init__(self, location, total_slots):
        self.location = location
        self.total_slots = total_slots
        self.available_slots = total_slots
        self.vehicle_count = {"Mobil": 0, "Motor": 0}

    def book_slot(self, vehicle_type):
        if self.available_slots > 0:
            self.available_slots -= 1
            self.vehicle_count[vehicle_type] += 1
            return True
        return False 

    def release_slot(self, vehicle_type):
        if self.vehicle_count[vehicle_type] > 0:
            self.available_slots += 1
            self.vehicle_count[vehicle_type] -= 1

class ParkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pembookingan Parkir")
        self.root.configure(bg="#2C3E50")
        
        self.parking_slots = {
            "Lantai 1": [
                ParkingSlot("Area A", 10),
                ParkingSlot("Area B", 15),
            ],
            "Lantai 2": [
                ParkingSlot("Area C", 20),
                ParkingSlot("Area D", 25),
            ],
            "Lantai 3": [
                ParkingSlot("Area E", 10),
                ParkingSlot("Area F", 10),
            ]
        }

        self.selected_vehicle_type = tk.StringVar(value="Mobil")
        self.selected_floor = None
        self.booking_time = None
        self.create_homepage()

    def create_homepage(self):
        self.clear_frame()
        tk.Label(
            self.root,
            text="Selamat Datang di Pembookingan Parkir",
            font=("Centaur", 20, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Pilih Kendaraan Anda:",
            font=("Centaur", 14),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=10)

        tk.Frame(self.root, bg="#2C3E50").pack(pady=5)
        tk.Radiobutton(
            self.root, text="Mobil", variable=self.selected_vehicle_type, value="Mobil",
            font=("Centaur", 14), bg="#34495E", fg="#ECF0F1",
            indicatoron=0, width=20, relief="raised"
        ).pack(pady=5)
        tk.Radiobutton(
            self.root, text="Motor", variable=self.selected_vehicle_type, value="Motor",
            font=("Centaur", 14), bg="#34495E", fg="#ECF0F1",
            indicatoron=0, width=20, relief="raised"
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Pilih Lantai",
            command=self.select_floor,
            font=("Centaur", 14, "bold"),
            bg="#1ABC9C", fg="#ECF0F1", width=20, relief="flat"
        ).pack(pady=15)
        tk.Button(
            self.root,
            text="Keluar",
            command=self.root.quit,
            font=("Centaur", 14, "bold"),
            bg="#E74C3C", fg="#ECF0F1", width=20, relief="flat"
        ).pack(pady=5)

    def select_floor(self):
        self.clear_frame()
        tk.Label(
            self.root,
            text="Pilih Lantai Parkir",
            font=("Centaur", 20, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=20)

        for floor in self.parking_slots.keys():
            tk.Button(
                self.root,
                text=f"{floor}",
                command=lambda f=floor: self.select_parking(f),
                font=("Centaur", 14, "bold"),
                bg="#3498DB", fg="#ECF0F1", width=20, relief="flat"
            ).pack(pady=10)

        tk.Button(
            self.root,
            text="Kembali",
            command=self.create_homepage,
            font=("Centaur", 14, "bold"),
            bg="#E67E22", fg="#ECF0F1", width=20, relief="flat"
        ).pack(pady=10)

    def select_parking(self, floor):
        self.selected_floor = floor
        self.clear_frame()
        tk.Label(
            self.root,
            text=f"Pilih Area Parkir - {floor}",
            font=("Centaur", 20, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=20)

        for idx, slot in enumerate(self.parking_slots[floor]):
            text = f"{slot.location} - Tersedia: {slot.available_slots}/{slot.total_slots}"
            tk.Button(
                self.root,
                text=text,
                command=lambda i=idx: self.book_slot(floor, i),
                font=("Centaur", 14),
                bg="#2980B9", fg="#ECF0F1", width=30, relief="flat"
            ).pack(pady=5)

        tk.Button(
            self.root,
            text="Kembali",
            command=self.select_floor,
            font=("Centaur", 14, "bold"),
            bg="#E67E22", fg="#ECF0F1", width=20, relief="flat"
        ).pack(pady=20)

    def book_slot(self, floor, index):
        selected_slot = self.parking_slots[floor][index]
        vehicle_type = self.selected_vehicle_type.get()

        if selected_slot.book_slot(vehicle_type):
            self.booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.show_ticket(vehicle_type, selected_slot.location, floor)
        else:
            messagebox.showwarning(
                "Yahh Pembookingan Gagal",
                f"Slot sudah penuh kak untuk kendaraan {vehicle_type} di {selected_slot.location}, {floor}."
            )

    def show_ticket(self, vehicle_type, location, floor):
        self.clear_frame()
        tk.Label(
            self.root,
            text="E-Ticket",
            font=("Courier New", 20, "bold"),
            bg="#2C3E50",
            fg="#1ABC9C"
        ).pack(pady=20)
        tk.Label(
            self.root,
            text=f"Tipe Kendaraan: {vehicle_type}",
            font=("Courier New", 14),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=10)
        tk.Label(
            self.root,
            text=f"Lantai: {floor}",
            font=("Courier New", 14),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=10)
        tk.Label(
            self.root,
            text=f"Lokasi Parkir: {location}",
            font=("Courier New", 14),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=10)
        tk.Label(
            self.root,
            text=f"Waktu Pembookingan: {self.booking_time}",
            font=("Courier New", 14),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=10)
        tk.Label(
            self.root,
            text="Booking ID: 2013214",
            font=("Courier New", 14),
            bg="#2C3E50",
            fg="#ECF0F1"
        ).pack(pady=10)
        tk.Button(
            self.root,
            text="Kembali ke Beranda",
            command=self.create_homepage,
            font=("Courier New", 14, "bold"),
            bg="#1ABC9C", fg="#ECF0F1", width=20, relief="flat"
        ).pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingApp(root)
    root.mainloop()
