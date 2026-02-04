#!/usr/bin/env python3

import click
from rich.console import Console
from commands import clean_system
from commands.battery import battery_status
from commands.doctor import system_doctor
from commands.privacy import privacy_scan
from commands import permission_audit


console = Console()



@click.group()
def cli():
    """🍎 macpilot — Universal macOS Helper Tool"""
    pass


@cli.command()
@click.option("--delete", is_flag=True, help="Actually delete files")
def clean(delete):
    """🧹 Clean unnecessary cache/log files"""
    clean_system(delete=delete)


@cli.command()
def battery():
    """🔋 Show battery health info"""
    battery_status()


@cli.command()
def doctor():
    """🩺 Run macOS diagnostics"""
    system_doctor()

@cli.command()
def privacy():
    """🔒 Run privacy & security scan"""
    privacy_scan()

@cli.command()
def audit():
    """🔍 Audit macOS app permissions (Camera/Mic/Disk)"""
    permission_audit()

@cli.command()
def gui():
    """🖥️ Launch macpilot menu bar GUI"""


if __name__ == "__main__":
    cli()
