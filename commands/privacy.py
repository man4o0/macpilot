import subprocess
from rich.console import Console

console = Console()

def privacy_scan():
    console.print("\n🔒 macpilot Privacy & Security Scan\n", style="bold magenta")

    console.print("\n📌 Gatekeeper Status:")
    subprocess.run(["spctl", "--status"])

    console.print("\n📌 Firewall Status:")
    subprocess.run(
        ["defaults", "read", "/Library/Preferences/com.apple.alf", "globalstate"]
    )

    console.print("\n📌 Apps with Camera Access (TCC Database):")
    console.print("⚠️ Full TCC scan coming soon...")

    console.print("\n✅ Privacy scan complete.\n")
