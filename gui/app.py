import rumps
import subprocess

class MacPilotApp(rumps.App):
    def __init__(self):
        super(MacPilotApp, self).__init__("🍎 macpilot")
        self.menu = [
            "Run Cleanup (Dry)",
            "Battery Status",
            "Privacy Scan",
            "Audit Scan",
            None,
            "Quit"
        ]

    @rumps.clicked("Run Cleanup (Dry)")
    def cleanup(self, _):
        subprocess.run(["python3", "macpilot.py", "clean"])

    @rumps.clicked("Battery Status")
    def battery(self, _):
        subprocess.run(["python3", "macpilot.py", "battery"])

    @rumps.clicked("Privacy Scan")
    def privacy(self, _):
        subprocess.run(["python3", "macpilot.py", "privacy"])

    @rumps.clicked("Audit Scan")
    def privacy(self, _):
        subprocess.run(["python3", "macpilot.py", "audit"])


    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    MacPilotApp().run()
