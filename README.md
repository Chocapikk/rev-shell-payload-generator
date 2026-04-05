# Rev Shell Payload Generator

Generates reverse shell payloads for Bash, Python, Netcat, PHP, Perl, Ruby, Lua, PowerShell, Socat and more.

Features:
- Automatic network interface detection (no subprocess, pure Python)
- Real-time payload generation (no page reload)
- Multiple payload types with syntax highlighting
- Encoding tab with chainable encoders (URL, Base64, Hex, HTML entities, Unicode, ROT13...)
- Ready-to-copy listener commands (nc, rlwrap, socat, pwncat-vl, Metasploit, rustcat, ncat SSL)
- Payloads defined in YAML for easy extension
- Click-to-copy on any payload or command

Usage:

1. Install dependencies:
   ```
   pip install flask pyyaml
   ```

2. Start the server:
   ```
   python3 revshell.py
   ```

3. Open your browser and go to:
   http://127.0.0.1:5000

4. Select your interface, port, and payload type. Everything updates in real-time.

Adding payloads:

Edit `payloads.yml` to add new payloads or listeners. No Python changes needed.

Requirements:
- Python 3.x
- Flask
- PyYAML

Notes:
This tool is intended for penetration testing and educational use only.
Only use it on systems you own or have explicit permission to test. Of course 😉

---

stlth_r4k3r 🇦🇺🫂❤️‍🔥🇫🇷 Chocapikk
