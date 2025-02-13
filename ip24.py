import os
import platform
from ipaddress import ip_network
from subprocess import Popen, PIPE

def ping(ip):
    """
    Функция для выполнения команды ping.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    process.communicate()
    return process.returncode == 0

def scan_network(network):
    """
    Сканирование сети на активные IP-адреса.
    """
    active_ips = []
    for ip in ip_network(network, strict=False).hosts():
        if ping(ip):
            active_ips.append(str(ip))
    return active_ips

if __name__ == "__main__":
    # Укажите диапазон сети, например, 192.168.1.0/24
    network_range = input("Введите диапазон сети (например, 192.168.1.0/24): ")
    print("Сканирование сети...")
    active_ips = scan_network(network_range)
    print(f"Найдено {len(active_ips)} активных IP-адресов:")
    for ip in active_ips:
        print(ip)
