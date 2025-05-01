[app]

title = AccelerometerApp
package.name = accelerometerapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = kivy,kivymd,plyer,python3==3.10.12,hostpython3==3.10.12,pyjnius>=1.5.0
orientation = portrait
fullscreen = 1

# Permissions for accelerometer and saving files
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Optional: include Android's accelerometer support
android.features = android.hardware.sensor.accelerometer

# Minimum Android API level
android.minapi = 21

# Target API level (33 is Android 13)
android.api = 33

# Set architecture (arm64-v8a is preferred now)
android.arch = arm64-v8a

# Entry point of your app
entrypoint = main.py

# Optional: icon
# icon.filename = %(source.dir)s/icon.png

# Skip logcat if you don't want logs
# log_level = 2

# Don't strip Python if you're debugging
# android.strip = false

# Package name and version
package.version = 1.0.0

# Hide status bar (optional)
# android.hide_statusbar = 1

# Prevent backup (optional)
# android.allow_backup = 0

[buildozer]

log_level = 2
warn_on_root = 1
