import os
import requests

# Estos valores vienen de los 'Secrets' de GitHub
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

def mantener_activo():
    # URL completa: https://tu-id.supabase.co/rest/v1/
    url = f"{SUPABASE_URL}" 
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Ping exitoso: Proyecto activo.")
        else:
            print(f"Respuesta del servidor: {response.status_code}")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    mantener_activo()