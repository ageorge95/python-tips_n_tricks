import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget
)

# Create a custom window class that inherits from QMainWindow
class SimpleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("PySide6 Signals and Slots")

        # Create a central widget and a layout to hold our other widgets
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 1. Create the widgets that will interact

        # This label will be our "slot" target. We'll change its text.
        self.my_label = QLabel("Press the button...")

        # This button will be our "signal" emitter.
        self.my_button = QPushButton("Click Me!")

        # 2. Make the connection
        #    - self.my_button is the object emitting the signal.
        #    - .clicked is the specific signal we care about.
        #    - .connect() is the function that makes the connection.
        #    - self.handle_button_click is the "slot" (the method to call).
        self.my_button.clicked.connect(self.handle_button_click)

        # Add the widgets to the layout
        layout.addWidget(self.my_label)
        layout.addWidget(self.my_button)

    # 3. Define the "slot" method
    # This method will be executed whenever the button's 'clicked' signal is emitted.
    def handle_button_click(self):
        print("Button was clicked! The slot method is running.")
        self.my_label.setText("Signal received! The text has changed.")
        # We can also disable the button after it's clicked once
        self.my_button.setEnabled(False)


# Main execution block
if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create an instance of our window
    window = SimpleWindow()
    window.show() # Make the window visible

    # Start the application's event loop
    sys.exit(app.exec())
