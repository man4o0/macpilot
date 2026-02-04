import platform
import subprocess
from rich.console import Console

console = Console()


def system_doctor():
    console.print("🩺 Running macOS Doctor...\n", style="bold yellow")

    console.print(f"System: {platform.mac_ver()[0]}")
    console.print(f"Machine: {platform.machine()}")

    console.print("\n📌 Disk Usage:")
    subprocess.run(["df", "-h"])

    console.print("\n📌 Top Processes:")
    subprocess.run(["top", "-l", "1", "-n", "5"])

    console.print("\n✅ Doctor check complete.")
