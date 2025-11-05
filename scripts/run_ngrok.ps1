<#
Simple helper to run ngrok for a local Django dev server.

Usage (PowerShell):
  1. Start Django dev server in one terminal:
       python manage.py runserver 127.0.0.1:8000
  2. Run this script in another PowerShell window:
       .\scripts\run_ngrok.ps1

This will launch `ngrok http 8000` and open the ngrok web UI at http://127.0.0.1:4040
#>

param(
    [int]$Port = 8000
)

Write-Host "Starting ngrok for local port $Port..."

# Start ngrok in a new window so the current shell remains usable.
Start-Process ngrok -ArgumentList "http $Port"

# Wait a little for ngrok to start and then open the web UI
Start-Sleep -Seconds 2
$uiUrl = "http://127.0.0.1:4040"
try {
    Start-Process $uiUrl
    Write-Host "ngrok started; web UI at $uiUrl"
} catch {
    Write-Host "ngrok started but failed to open web UI automatically. Open $uiUrl manually."
}
