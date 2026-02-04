import subprocess
from rich.console import Console
from rich.table import Table

console = Console()


def optimize_system():
    console.print("\n⚡ macpilot Optimize Report\n", style="bold yellow")

    # --- Top CPU processes ---
    console.print("📌 Top Processes by CPU Usage:\n")

    try:
        result = subprocess.check_output(
            ["ps", "-arcwwwxo", "pid,command,%cpu,%mem"],
            text=True
        ).splitlines()

        table = Table(title="Top Running Processes")

        table.add_column("PID")
        table.add_column("Command")
        table.add_column("CPU %")
        table.add_column("RAM %")

        for line in result[1:6]:
            parts = line.split(None, 3)
            if len(parts) == 4:
                pid, cpu, mem, cmd = parts[0], parts[1], parts[2], parts[3]
                table.add_row(pid, cmd[:40], cpu, mem)

        console.print(table)

    except Exception as e:
        console.print(f"❌ Error fetching process list: {e}", style="red")

    # --- Login items ---
    console.print("\n📌 Login Items (Startup Apps):\n")

    try:
        login_items = subprocess.check_output(
            ["osascript", "-e",
             'tell application "System Events" to get the name of every login item'],
            text=True
        ).strip()

        if login_items:
            for item in login_items.split(", "):
                console.print(f"  • {item}")
        else:
            console.print("✅ No login items found.")

    except Exception:
        console.print("⚠️ Unable to read login items (permissions may be required).")

    console.print("\n✅ Optimization report complete.\n")
    console.print("Tip: Remove unnecessary startup apps in System Settings → Login Items.")
