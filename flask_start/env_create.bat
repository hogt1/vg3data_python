@echo off
py -3 -m venv env
pip install -r requirements.txt
@echo "Du har nå opprettet et virtualt miljø for Python!"
@echo "Nødvendige pakker ble installert med: pip install -r requirements.txt"