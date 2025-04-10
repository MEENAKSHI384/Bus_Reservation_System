class Bus:
    def _init_(self, bus_number, route, total_seats):
        self.bus_number = bus_number
        self.route = route
        self.total_seats = total_seats
        self.available_seats = total_seats

class Reservation:
    def _init_(self, reservation_id, passenger_name, age, bus_number):
        self.reservation_id = reservation_id
        self.passenger_name = passenger_name
        self.age = age
        self.bus_number = bus_number

class BusManager:
    def _init_(self):
        self.buses = []

    def add_bus(self, bus_number, route, total_seats):
        self.buses.append(Bus(bus_number, route, total_seats))
        print(f"Bus {bus_number} added successfully!")

    def remove_bus(self, bus_number):
        bus = self.get_bus(bus_number)
        if bus:
            self.buses.remove(bus)
            print(f"Bus {bus_number} removed!")
        else:
            print("Bus not found!")

    def view_buses(self):
        if not self.buses:
            print("No buses available.")
            return
        print("Available Buses:")
        for bus in self.buses:
            print(f"Bus: {bus.bus_number} | Route: {bus.route} | Seats: {bus.available_seats}/{bus.total_seats}")

    def get_bus(self, bus_number):
        for bus in self.buses:
            if bus.bus_number == bus_number:
                return bus
        return None

class ReservationManager:
    def _init_(self, bus_manager):
        self.reservations = []
        self.bus_manager = bus_manager
        self.reservation_counter = 1

    def book_ticket(self, name, age, bus_number):
        bus = self.bus_manager.get_bus(bus_number)
        if not bus:
            print("Bus not found!")
            return
        if bus.available_seats == 0:
            print("Bus is full! No seats available.")
            return
        reservation = Reservation(self.reservation_counter, name, age, bus_number)
        self.reservations.append(reservation)
        self.reservation_counter += 1
        bus.available_seats -= 1
        print(f"Ticket Booked! Reservation ID: {reservation.reservation_id}")

    def cancel_ticket(self, reservation_id):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                self.reservations.remove(reservation)
                bus = self.bus_manager.get_bus(reservation.bus_number)
                if bus:
                    bus.available_seats += 1
                print(f"Ticket Canceled! ID: {reservation_id}")
                return
        print("Reservation not found!")

    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.")
            return
        print("Reservations:")
        for res in self.reservations:
            print(f"ID: {res.reservation_id} | Passenger: {res.passenger_name} | Age: {res.age} | Bus: {res.bus_number}")

def admin_menu(bus_manager):
    while True:
        print("\n=== Admin Panel ===")
        print("1. Add Bus")
        print("2. Remove Bus")
        print("3. View Buses")
        print("4. Back to Main Menu")
        choice = input("Choose option: ")

        if choice == '1':
            bus_no = int(input("Enter Bus Number: "))
            route = input("Enter Route: ")
            seats = int(input("Enter Total Seats: "))
            bus_manager.add_bus(bus_no, route, seats)
        elif choice == '2':
            bus_no = int(input("Enter Bus Number to Remove: "))
            bus_manager.remove_bus(bus_no)
        elif choice == '3':
            bus_manager.view_buses()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

def user_menu(reservation_manager):
    while True:
        print("\n=== User Panel ===")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Reservations")
        print("4. Back to Main Menu")
        choice = input("Choose option: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            bus_no = int(input("Enter Bus Number: "))
            reservation_manager.book_ticket(name, age, bus_no)
        elif choice == '2':
            res_id = int(input("Enter Reservation ID to Cancel: "))
            reservation_manager.cancel_ticket(res_id)
        elif choice == '3':
            reservation_manager.view_reservations()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

def main():
    bus_manager = BusManager()
    reservation_manager = ReservationManager(bus_manager)

    while True:
        print("\n=== Bus Reservation System ===")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            admin_menu(bus_manager)
        elif choice == '2':
            user_menu(reservation_manager)
        elif choice == '3':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice!")

if __name__ == "_main_":
    main()