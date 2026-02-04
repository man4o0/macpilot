import subprocess
from rich.console import Console

console = Console()


def battery_status():
    console.print("🔋 Battery Health Report\n", style="bold cyan")

    try:
        result = subprocess.check_output(
            ["system_profiler", "SPPowerDataType"],
            text=True
        )
        console.print(result)

    except Exception as e:
        console.print(f"Error reading battery info: {e}", style="bold red")
