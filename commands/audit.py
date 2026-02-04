import sqlite3
from rich.console import Console
import os

console = Console()

TCC_DB = os.path.expanduser(
    "~/Library/Application Support/com.apple.TCC/TCC.db"
)

def permission_audit():
    console.print("\n🔍 macpilot Permission Auditor\n", style="bold cyan")

    try:
        conn = sqlite3.connect(TCC_DB)
        cursor = conn.cursor()

        cursor.execute("SELECT service, client, auth_value FROM access LIMIT 10;")

        console.print("\n✅ Permissions found:\n")

        for service, client, auth in cursor.fetchall():
            allowed = "Yes" if auth == 2 else "No"
            console.print(f"{service} → {client} → {allowed}")

        conn.close()

    except sqlite3.DatabaseError:
        console.print("\n❌ Access denied by macOS Privacy Protection.\n", style="bold red")
        console.print("To enable this feature:\n")
        console.print("1. System Settings → Privacy & Security")
        console.print("2. Full Disk Access")
        console.print("3. Enable Terminal")
        console.print("4. Restart Terminal\n")
