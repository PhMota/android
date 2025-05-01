# from kivymd.app import MDApp
# from kivymd.uix.button import MDRaisedButton

# class MyApp(MDApp):
#     def build(self):
#         return MDRaisedButton(text="Click me", pos_hint={"center_x": 0.5, "center_y": 0.5})

# MyApp().run()

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window
import csv
import time

try:
    from plyer import accelerometer
except ImportError:
    accelerometer = None


class AccelerometerDisplay(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)
        self.label = MDLabel(text="Accelerometer: (x, y, z)", halign="center", font_style="H6")
        self.add_widget(self.label)

        self.data_log = []  # Stores timestamp + x, y, z

        # Try starting the accelerometer
        if platform == "android" and accelerometer:
            try:
                accelerometer.enable()
                Clock.schedule_interval(self.update, 0.1)
            except:
                self.label.text = "Failed to start accelerometer"
        else:
            self.label.text = "Accelerometer not available"

    def update(self, dt):
        val = accelerometer.acceleration
        if val != (None, None, None):
            x, y, z = val
            now = time.time()
            self.label.text = f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}"
            self.data_log.append((now, x, y, z))
            self.save_to_file()

    def save_to_file(self):
        filepath = self.get_output_path()
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "x", "y", "z"])
            writer.writerows(self.data_log)

    def get_output_path(self):
        from kivy.storage.jsonstore import JsonStore
        import os

        # Save in app's internal storage or external if available
        if platform == "android":
            from android.storage import primary_external_storage_path
            base = primary_external_storage_path()
        else:
            base = os.getcwd()

        folder = os.path.join(base, "AccelerometerLogs")
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, "accelerometer_log.csv")


class AccelerometerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return AccelerometerDisplay()


if __name__ == '__main__':
    AccelerometerApp().run()
