import fcntl
import socket
import struct
import urllib.request
from pathlib import Path

import yaml
from flask import Flask, render_template

app = Flask(__name__, static_folder="templates", static_url_path="/static")


class NetworkInterfaces:
    SIOCGIFADDR = 0x8915

    @staticmethod
    def _get_ip(ifname):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(
                fcntl.ioctl(
                    s.fileno(),
                    NetworkInterfaces.SIOCGIFADDR,
                    struct.pack("256s", ifname[:15].encode()),
                )[20:24]
            )
        except OSError:
            return None

    @staticmethod
    def _get_public_ip():
        try:
            resp = urllib.request.urlopen("https://ifconfig.me", timeout=3)
            return resp.read().decode().strip()
        except Exception:
            return None

    @classmethod
    def get_all(cls):
        ips = {}

        for iface in Path("/sys/class/net").iterdir():
            if iface.name == "lo":
                continue
            ip = cls._get_ip(iface.name)
            if ip:
                ips[iface.name] = ip

        public = cls._get_public_ip()
        if public:
            ips["public"] = public

        return ips or {"lo": "127.0.0.1"}

    @classmethod
    def get_default(cls):
        ips = cls.get_all()

        if "tun0" in ips:
            return ips["tun0"]

        for iface, ip in ips.items():
            if iface != "public":
                return ip

        return next(iter(ips.values()))


def load_payloads(path="payloads.yml"):
    return yaml.safe_load(Path(path).read_text())


@app.route("/")
def home():
    data = load_payloads()
    return render_template(
        "index.html",
        ips=NetworkInterfaces.get_all(),
        default_ip=NetworkInterfaces.get_default(),
        payloads=data["payloads"],
        listeners=data["listeners"],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
