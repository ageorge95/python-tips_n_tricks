import sys
import time
from PySide6.QtCore import QObject, Signal, Slot, QRunnable, QThreadPool
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QWidget
)


# 1. Define the Worker object that will do the background work
#    Note: It inherits from QObject to use signals and slots.
class Worker(QObject):
    # a) Define custom signals.
    #    'progress' will emit an integer (0-100).
    #    'finished' will emit with no data.
    progress = Signal(int)
    finished = Signal()

    # b) Use @Slot to define the method that will be run.
    @Slot()
    def run_task(self):
        """A long-running task."""
        print("Worker task started.")
        for i in range(1, 11):
            time.sleep(0.5)  # Simulate work being done

            # c) Emit the custom signal with the progress value
            self.progress.emit(i * 10)

        # d) Emit the finished signal when the task is done
        self.finished.emit()
        print("Worker task finished.")


# Create the main window
class CustomSignalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Signal Example")

        # Setup UI
        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start Task")

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Setup the worker and a thread for it to run in
        # This keeps the GUI responsive while the task runs!
        self.thread = QThreadPool()
        print(f"Multithreading with maximum {self.thread.maxThreadCount()} threads")

        # 2. Connect the button's clicked signal to our start method
        self.start_button.clicked.connect(self.run_worker_task)

    def run_worker_task(self):
        # Create a worker instance
        self.worker = Worker()

        # 3. Connect the worker's custom signals to the window's slots
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.task_finished)

        # Disable the button so we don't start multiple tasks
        self.start_button.setEnabled(False)
        self.progress_bar.setValue(0)

        # Execute the worker's task in the thread pool
        # For QThreadPool, we wrap the worker in a QRunnable,
        # but the signal/slot logic remains the same.
        # A simple way to do this is to make a runnable that calls the worker's method.
        class Runnable(QRunnable):
            def __init__(self, target):
                super().__init__()
                self.target = target

            def run(self):
                self.target()

        runnable = Runnable(self.worker.run_task)
        self.thread.start(runnable)

    # 4. Define the slots using the @Slot decorator
    @Slot(int)
    def update_progress(self, value):
        """This slot receives the integer from the worker's 'progress' signal."""
        self.progress_bar.setValue(value)

    @Slot()
    def task_finished(self):
        """This slot is called when the worker's 'finished' signal is emitted."""
        print("Main window notified that task is finished.")
        self.start_button.setEnabled(True)


# Main execution block
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomSignalWindow()
    window.show()
    sys.exit(app.exec())
