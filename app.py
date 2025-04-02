from flask import Flask, render_template
import threading
import webbrowser
import socket
from flaskwebgui import FlaskUI
app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def index():
    return render_template("dashboard.html")  # 请确保 templates 文件夹里有 dashboard.html

# 获取本机真实局域网 IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 连接一个外部地址，但不发送数据，从而获取本机地址
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def open_browser():
    ip = get_local_ip()
    url = f"http://{ip}:5000"
    print("✅ 本机访问地址：", url)
    webbrowser.open(url)

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    # host 设置为 0.0.0.0，监听所有地址（包括你局域网 IP）
    # app.run(host='0.0.0.0', port=5000, debug=False)

    FlaskUI(app=app, server="flask").run()