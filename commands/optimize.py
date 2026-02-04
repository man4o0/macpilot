import subprocess
from pathlib import Path
from rich.console import Console
from rich.table import Table
import os

console = Console()

def optimize_system():
    console.print("\n⚡ [bold yellow]macpilot Optimize Pro Report[/bold yellow]\n")

    # --- Top CPU Processes ---
    console.print("📌 [bold]Top Processes by CPU Usage[/bold]\n")
    try:
        result = subprocess.check_output(
            ["ps", "-axo", "pid,comm,%cpu,%mem"],
            text=True
        ).splitlines()
        table = Table(title="Top CPU Processes")
        table.add_column("PID")
        table.add_column("Command")
        table.add_column("CPU %")
        table.add_column("RAM %")
        for line in result[1:6]:
            parts = line.split(None, 3)
            if len(parts) == 4:
                pid, cmd, cpu, mem = parts[0], parts[1], parts[2], parts[3]
                table.add_row(pid, cmd[:40], cpu, mem)
        console.print(table)
    except Exception as e:
        console.print(f"❌ Error fetching CPU processes: {e}", style="red")

    # --- Top RAM Processes ---
    console.print("\n📌 [bold]Top Processes by RAM Usage[/bold]\n")
    try:
        result = subprocess.check_output(
            ["ps", "-axo", "pid=,comm=,%mem="],  # macOS-compatible
            text=True
        ).splitlines()

        lines = []
        for line in result:
            try:
                pid = line[:6].strip()
                mem = line[-6:].strip()
                cmd = line[6:-6].strip()
                lines.append((pid, cmd, float(mem)))
            except Exception:
                continue

        # Sort by RAM %
        lines.sort(key=lambda x: x[2], reverse=True)

        table = Table(title="Top RAM Processes")
        table.add_column("PID")
        table.add_column("Command")
        table.add_column("RAM %")
        for pid, cmd, mem in lines[:5]:
            table.add_row(pid, cmd[:40], f"{mem:.1f}")
        console.print(table)
    except Exception as e:
        console.print(f"❌ Error fetching RAM processes: {e}", style="red")

    # --- Disk Usage ---
    console.print("\n📌 [bold]Largest Folders in Home Directory[/bold]\n")
    try:
        home = Path.home()
        folders = [f for f in home.iterdir() if f.is_dir()]
        du_output = []
        for folder in folders:
            try:
                size = subprocess.check_output(["du", "-sh", str(folder)], text=True).split()[0]
                du_output.append((size, str(folder)))
            except Exception:
                continue
        # Sort by numeric size (approximation)
        du_output.sort(key=lambda x: int(''.join(filter(str.isdigit, x[0]))), reverse=True)
        table = Table(title="Disk Usage")
        table.add_column("Size")
        table.add_column("Folder")
        for size, folder in du_output[:5]:
            table.add_row(size, folder)
        console.print(table)
    except Exception as e:
        console.print(f"❌ Error fetching disk usage: {e}", style="red")

    # --- Login Items ---
    console.print("\n📌 [bold]Login Items[/bold]\n")
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
        console.print("⚠️ Unable to read login items (Full Disk Access may be required)")

    # --- Launch Agents / Daemons ---
    console.print("\n📌 [bold]Launch Agents & Daemons[/bold]\n")
    paths = ["/Library/LaunchAgents", "/Library/LaunchDaemons",
             str(Path.home() / "Library/LaunchAgents")]
    for path in paths:
        console.print(f"[underline]{path}[/underline]")
        if os.path.exists(path):
            items = os.listdir(path)
            if items:
                for f in items:
                    console.print(f"  • {f}")
            else:
                console.print("  ✅ None found")
        else:
            console.print("  ⚠️ Not found")

    # --- Recommendations ---
    console.print("\n💡 [bold green]Recommendations:[/bold green]")
    console.print("  • Remove unused login items in System Settings → Login Items")
    console.print("  • Consider uninstalling heavy apps you rarely use")
    console.print("  • Check background LaunchAgents you don’t need")
    console.print("\n✅ Optimization report complete.\n")
