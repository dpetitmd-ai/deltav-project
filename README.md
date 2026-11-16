# 🚀 Delta-V Project — Mars EVA & Rover Tactical Navigator (Arcadia Planitia)

[![Live Demo](https://img.shields.io/badge/Live_Demo-deltavproject.netlify.app-ff6b4a?style=for-the-badge&logo=netlify)](https://deltavproject.netlify.app)
[![PWA Offline](https://img.shields.io/badge/PWA-100%25_Offline_Ready-22c55e?style=for-the-badge)](https://deltavproject.netlify.app)
[![Cartography](https://img.shields.io/badge/Cartography-NASA_Mars_Trek_%7C_USGS_MOLA-22d3ee?style=for-the-badge)](https://trek.nasa.gov/mars/)

**Delta-V Project** is an interactive, dual-interface surface navigation and life-support telemetry system designed for human Extravehicular Activities (EVA) and pressurized/scout rover operations on Mars. 

Georeferenced at the **Arcadia Planitia** candidate human landing site (**`46.50° N, 128.50° W` / `231.50° E`**, MOLA elevation `-3,150 m`), the platform combines official NASA orbital datasets with a 100% offline-capable Progressive Web App (PWA) architecture, real-time physical GPS translation, and automated data synchronization.

---

## 🌟 Key Features

### 1. Dual Astronaut Interface (AR Helmet Visor + Forearm Cuff Tablet)
* **🥽 Augmented Reality Helmet HUD (`Key H`):** Projects an areographic compass ribbon, central targeting reticle, real-time metabolic and consumable bars, nearest resource radar, and high-visibility proximity hazard alerts directly over the terrain view.
* **⌚ Forearm Suit Cuff Display (`Key T`):** Interactive tactical control unit mounted on the astronaut's arm to configure terrain coefficients ($k$), elevation gain, ambient temperature, and surface mobility modes.

### 2. Multi-Layer Planetary Cartography & Embedded Offline Graticule
* **Embedded USGS MOLA Regional Map + Graticule (Offline Base64):** High-resolution colorized topography (`-57°S to +57°N`, `-180°W to +180°E`) with coordinate graticules and degree ticks baked directly into the application for zero-latency rendering in Airplane Mode.
* **NASA Mars Trek Live WMTS Layers (`Keys 1, 2, 3`):**
  * **MOLA Colorized Shaded Relief:** Global laser altimetry for slope and elevation awareness.
  * **Viking MDIM 2.1 True-Color Optical Mosaic:** Visual surface reference for crater rims and volcanic plains.
  * **THEMIS Day/Night Infrared (IR):** Geothermal inertia layer to distinguish consolidated bedrock ($k = 1.0$) from hazardous, unconsolidated fine regolith dust traps ($k = 1.5$).
* **5 Instant Tactical Presets (`Keys 4 to 8`):** Rapidly switch between regional geothermal overviews, official IAU nomenclature overlays (including *Arcadia Dorsa*, *Milankovic Crater*, *Acheron Fossae*, *Alba Fossae*, *Olympus Mons*, and the *USA Phoenix Lander*), and high-zoom optical landing zone inspections.

### 3. Combined Mobility Engine (Foot EVA + Rover + Walk-Back Contingency)
* Supports **Foot EVA Only**, **Rover Only**, and **Combined Mode (Rover transit + Foot EVA exploration)** with a customizable route split slider.
* **PLSS Life-Support Biomathematics:** Calculates round-trip duration, average slope angle ($\theta$), metabolic rate ($M$ in Watts), **PLSS Oxygen ($0.90\text{ kg}$ capacity)**, **Sublimator Cooling Water ($4.50\text{ L}$)**, **Suit Battery ($750\text{ Wh}$)**, and **Rover Battery ($12\text{ kWh}$)** with optional Rover Umbilical savings ($75\%$ PLSS conservation during transit).
* **NASA Safety Guardrails:** Automatically triggers a **Route Blocked Alert** if terrain slope exceeds **$30^\circ$** ($22^\circ$ for Rover rollover limit) or a **NASA 33% Reserve Warning** if any consumable drops below safe return margins, including emergency **Walk-Back** verification in case of rover mechanical failure.

### 4. Physical Satellite GPS Translation (`Earth → Mars`) & 100% Offline PWA
* Uses the mobile device's physical satellite receiver (`navigator.geolocation.watchPosition`) in **100% Offline / Airplane Mode**.
* Anchors the user's physical starting point on Earth to the **Black Cross (`+`) Landing Zone** in Arcadia Planitia and translates real-world walking distance into Martian areographic coordinates using planetary radius scaling ($R_{\text{Mars}} = 3,389.5\text{ km}$) and selectable field-testing scales (`1:1`, `1:50`, `1:100`, `1:500`).

### 5. ISRU Resource & Hazard Field Database (`GeoJSON` + `LocalStorage`)
* Pre-loaded and user-extensible catalog of **Arcadia Planitia** targets:
  * 💧 **Water / Subsurface Ice:** SHARAD radar glacial aquifers ($1.8\text{ m}$ depth), Milankovic Crater ice terraces, and fresh impact ejecta ice.
  * 💎 **Minerals & ISRU:** Olivine-rich basalt outcrops, hydrated phyllosilicates/clays, hematite/magnetite veins, and Alba Fossae hydrothermal sulfates.
  * 📍 **EVA Waypoints & Shelters:** Arcadia basaltic lava tubes (Solar Particle Event radiation shielding) and Arcadia Dorsa UHF/Ka-band relay stations.
  * ☠️ **Terrain Hazards:** Sharp ventifact boulder fields, Acheron Fossae steep tectonic scarps, and low-thermal-inertia regolith sinkage zones.

---

## ⌨️ Tactical Keyboard & D-Pad Controls

| Key / Control | Action |
| :---: | :--- |
| **`W` `A` `S` `D`** / **Arrows** | Manual step movement of the Astronaut / Rover across Arcadia Planitia |
| **`Spacebar`** | Start / Pause automated EVA route simulation |
| **`G`** | Toggle physical Satellite GPS tracking (Offline-capable) |
| **`M`** | Cycle mobility mode (`Foot EVA` → `Rover` → `Combined`) |
| **`H`** / **`T`** | Show / Hide **AR Helmet Visor** (`H`) or **Forearm Tablet** (`T`) |
| **`N`** | Toggle official Mars Trek Nomenclature & Mission Labels |
| **`R`** | Anchor / Return Astronaut to the Primary Landing Zone (`+`) |
| **`1` `2` `3`** | Switch base layers (`1`: MOLA, `2`: Optical Viking, `3`: THEMIS IR) |
| **`4` `5` `6` `7` `8`** | Activate Mars Trek Regional & Landing Zone Preset Views (`View 1` to `View 5`) |

---

## 🔄 Automated NASA Repository Synchronization (CI/CD)

This repository includes an automated **GitHub Actions** pipeline (`.github/workflows/nasa-sync.yml` + `sync_nasa.py`) that queries open NASA mission feeds and rover waypoint repositories every 6 hours, updating `nasa_live_data.geojson` and triggering an automatic production deployment to Netlify.

## 📦 Quick Deployment & Mobile Installation

1. **Web / Netlify:** Deploy directly from this repository or drag-and-drop `index.html` into [Netlify Drop](https://app.netlify.com/drop).
2. **Google Sites Integration:** Embed `index.html` directly; the built-in environment detector automatically displays a full-screen launcher banner and mobile QR code to bypass iframe geolocation restrictions.
3. **Install on Mobile / Suit Tablet:** Open [`https://deltavproject.netlify.app`](https://deltavproject.netlify.app), tap **📲 QR / Install / Offline**, preload the regional Mars Trek tiles into device cache, and select **Add to Home Screen** (iOS/Android) for standalone offline operation.
