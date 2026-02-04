import os
import shutil
from rich.console import Console

console = Console()

SAFE_TARGETS = [
    os.path.expanduser("~/Library/Caches"),
    os.path.expanduser("~/Library/Logs"),
]

def clean_system(delete=False):
    console.print("\n🧹 macpilot Cleanup Mode\n", style="bold green")

    total_removed = 0

    for folder in SAFE_TARGETS:
        if not os.path.exists(folder):
            continue

        console.print(f"📂 Target: {folder}")

        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)

            console.print(f"  ➜ Found: {item_path}")

            if delete:
                try:
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                    else:
                        os.remove(item_path)

                    total_removed += 1
                    console.print("    ✅ Deleted", style="green")

                except Exception as e:
                    console.print(f"    ❌ Failed: {e}", style="red")

    if delete:
        console.print(f"\n✅ Cleanup complete. Removed {total_removed} items.")
    else:
        console.print("\n⚠️ Dry-run only. Nothing deleted.")
        console.print("Run with: macpilot clean --delete")
