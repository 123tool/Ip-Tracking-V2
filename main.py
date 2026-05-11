import sys
import time
from assets.ui import banner, clear, P, C, G, R, W, Y
from core.tracer import IPTracer

def display_info(data):
    if "error" in data:
        print(f"{R}[!] Error: {data['error']}{W}")
        return

    fields = [
        ("IP Address", "ip"),
        ("Network", "network"),
        ("Version", "version"),
        ("City", "city"),
        ("Region", "region"),
        ("Region Code", "region_code"),
        ("Country", "country_name"),
        ("Country Code", "country_code"),
        ("Country Capital", "country_capital"),
        ("TLD", "country_tld"),
        ("Continent", "continent_code"),
        ("Postal Code", "postal"),
        ("Latitude", "latitude"),
        ("Longitude", "longitude"),
        ("Timezone", "timezone"),
        ("UTC Offset", "utc_offset"),
        ("Calling Code", "country_calling_code"),
        ("Currency", "currency"),
        ("Currency Name", "currency_name"),
        ("Languages", "languages"),
        ("ASN", "asn"),
        ("Organization", "org"),
    ]

    print(f"\n{G}>>> Details for target IP: {P}{data.get('ip')}{W}")
    print("-" * 45)

    for label, key in fields:
        val = data.get(key, "None")
        color = R if "country" in label.lower() or "ip" in label.lower() else C
        print(f"{color}{label.lower().replace(' ', '_')} : {W}{val}")

def main():
    clear()
    banner()
    
    tracer = IPTracer()
    
    target = input(f"{P}Enter target IP {W}(leave blank for yours): {G}")
    print(f"{Y}[*] Fetching intelligence data...{W}")
    time.sleep(1)

    data = tracer.trace(target)
    display_info(data)

    print(f"\n{G}Do you want to continue? [y/n]{W}")
    cont = input(">> ").lower()
    if cont == 'y':
        main()
    else:
        print(f"{P}Developer, Spy-E!{W}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Hunter mode off.{W}")
