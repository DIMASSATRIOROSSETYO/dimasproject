from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Pembelian tiket konser')

        self.jumlah_tiket = QLineEdit()

        self.labelinput1 = QLabel("Pilih jenis tiket")
        self.labelinput2 = QLabel("Masukkan jumlah tiket")
        self.hasil_label = QLabel("Total harga")
        self.result_label = QLabel()

        self.regular_button = QPushButton('Regular')
        self.regular_button.clicked.connect(lambda: self.set_ticket_type("regular"))
        self.vip_button = QPushButton('VIP')
        self.vip_button.clicked.connect(lambda: self.set_ticket_type("vip"))

        self.multiply_button = QPushButton('Beli')
        self.multiply_button.clicked.connect(self.multiply_numbers)

        layout = QVBoxLayout()
        layout.addWidget(self.labelinput1)
        layout.addWidget(self.regular_button)
        layout.addWidget(self.vip_button)
        layout.addWidget(self.labelinput2)
        layout.addWidget(self.jumlah_tiket)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.hasil_label)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.ticket_type = None

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type
        if ticket_type == "regular":
            self.regular_button.setStyleSheet("background-color: grey")
            self.vip_button.setStyleSheet("")
        elif ticket_type == "vip":
            self.regular_button.setStyleSheet("")
            self.vip_button.setStyleSheet("background-color: grey")

    def multiply_numbers(self):
        if self.ticket_type is None:
            self.result_label.setText("Pilih jenis tiket terlebih dahulu.")
            return

        jumlah_text = self.jumlah_tiket.text()
        try:
            jumlah = int(jumlah_text)
            if jumlah < 1:
                raise ValueError
        except ValueError:
            self.result_label.setText("Jumlah tiket harus lebih dari 0.")
            self.jumlah_tiket.clear()
            self.jumlah_tiket.setFocus()
            return

        if self.ticket_type == "regular":
            harga_tiket = 50000
        elif self.ticket_type == "vip":
            harga_tiket = 100000
        else:
            self.result_label.setText("Jenis tiket tidak valid.")
            return

        total_harga = harga_tiket * jumlah
        self.result_label.setText(f"Rp {total_harga}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
