from json import load

file_name = open("m_lista.json", encoding="utf-8")
content = load(file_name)

for item in content:
    ip = item ["ip_address"]
    prefix = int(ip.split(".")[0])
    print(ip)

