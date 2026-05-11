import requests

class IPTracer:
    def __init__(self):
        self.base_url = "https://ipapi.co/{}/json/"

    def trace(self, ip):
        try:
            url = self.base_url.format(ip) if ip else "https://ipapi.co/json/"
            response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
            
            if response.status_status == 200:
                return response.json()
            else:
                return {"error": "Gagal mengambil data dari server."}
        except Exception as e:
            return {"error": str(e)}
