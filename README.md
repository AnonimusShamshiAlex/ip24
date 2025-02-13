# ip24

Как работает программа:
Ввод диапазона сети: Пользователь вводит диапазон сети в формате CIDR (например, 192.168.1.0/24).
Ping каждого IP-адреса: Программа отправляет ICMP-запросы каждому IP-адресу в указанном диапазоне.
Список активных IP: Если устройство отвечает на запрос, его IP-адрес добавляется в список активных.
Вывод результата: Программа выводит количество найденных IP-адресов и их список.
Требования:
Python 3.6 или выше.
Установленная библиотека ipaddress (встроена в Python 3.3+).
Программа должна запускаться с правами администратора, если требуется доступ к сетевым утилитам.
