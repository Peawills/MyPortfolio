# MyPortfolio

## Troubleshooting: "You're accessing the development server over HTTPS" error

If you see log lines like:

```
code 400, message Bad request version ('\x00\x02\x01\x00...')
You're accessing the development server over HTTPS, but it only supports HTTP.
```

This means a client (your browser or a tunnel) tried to speak HTTPS/TLS to Django's built-in development server, which only speaks plain HTTP. This is an environment/proxy mismatch (not a Django bug).

Quick fixes

- Use HTTP locally: open the site with an explicit http:// URL (for example `http://127.0.0.1:8000` or `http://localhost:8000`). If the browser upgrades to HTTPS automatically, try an Incognito/Private window or clear HSTS/site permissions for the domain.

- Use ngrok for HTTPS endpoints (recommended when testing webhooks or external services):

	1. Run the Django dev server from your project root:

	```powershell
	python manage.py runserver 127.0.0.1:8000
	```

	2. In a separate terminal run ngrok to create an HTTPS tunnel:

	```powershell
	ngrok http 8000
	```

	3. Use the https:// URL ngrok prints for external callbacks; ngrok will forward TLS to your local HTTP server.

- If you require HTTPS for local development, use a TLS-terminating proxy (Caddy or nginx) or `django-extensions` `runserver_plus` with a certificate. For production-like TLS, prefer a proper server (nginx/Caddy) in front of Django.

Notes

- If you are using a custom hostname or tunnel domain, ensure that hostname is allowed in `ALLOWED_HOSTS` (in `portfolio/settings.py`) while testing. Be careful: do not set `ALLOWED_HOSTS=['*']` in production.
- These fixes are meant for local development only.

Quick PowerShell helper

There is a small helper script under `scripts/run_ngrok.ps1` that runs ngrok and opens the ngrok web UI. See `scripts/run_ngrok.ps1` for usage.
