import urllib.request
import json
from datetime import datetime, timezone

# Repositorios abiertos con telemetría de misiones y waypoints de la NASA (MMGIS / Mars 2020)
NASA_FEEDS = {
    "perseverance_waypoints": "https://raw.githubusercontent.com/stiles/mars-perseverance-waypoints/main/data/latest/waypoints.geojson",
    "mars_sites": "https://azmth.space/data/mars-sites.json"
}

output_geojson = {
    "type": "FeatureCollection",
    "name": "DeltaV_Project_NASA_Live_Sync",
    "metadata": {
        "project": "Delta-V Project",
        "region": "Arcadia Planitia & Global Mars",
        "last_nasa_sync_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    },
    "features": []
}

# 1. Descargar sitios de misiones activos
try:
    req = urllib.request.Request(NASA_FEEDS["mars_sites"], headers={'User-Agent': 'DeltaV-Project-Sync/1.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        sites = json.loads(resp.read().decode("utf-8"))
        if isinstance(sites, list):
            for s in sites:
                if "lat" in s and "lon" in s:
                    output_geojson["features"].append({
                        "type": "Feature",
                        "properties": {
                            "name": s.get("name", "NASA Mission Site"),
                            "category": "nasa_mission",
                            "status": s.get("status", "Active")
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(s["lon"]), float(s["lat"])]
                        }
                    })
except Exception as e:
    print(f"Aviso en mars_sites: {e}")

# 2. Descargar últimos waypoints de Rovers (NASA Mars 2020)
try:
    req = urllib.request.Request(NASA_FEEDS["perseverance_waypoints"], headers={'User-Agent': 'DeltaV-Project-Sync/1.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        rover_data = json.loads(resp.read().decode("utf-8"))
        if "features" in rover_data:
            # Agregamos los últimos 15 waypoints reportados por la NASA
            output_geojson["features"].extend(rover_data["features"][-15:])
except Exception as e:
    print(f"Aviso en rover_waypoints: {e}")

# 3. Guardar el archivo actualizado en el repositorio
with open("nasa_live_data.geojson", "w", encoding="utf-8") as f:
    json.dump(output_geojson, f, indent=2, ensure_ascii=False)

print("Sincronización con la NASA completada exitosamente.")
