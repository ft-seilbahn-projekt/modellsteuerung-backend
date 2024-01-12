# DIPS

```
1 - deskemergsb - Taster Nothalt Stationsbetrieb
2 - deskemerg - Taster Nothalt
3 - deskwrn - Taster Halt
4 - deskcis - Taster CIS
5 - deskgo - Taster Start
6 - deskqs - Taster Quittieren System
7 - deskqb - Taster Quittieren Betrieb
8 - deskser - Taster Servicebetrieb
9 - deskfg - Taster Fahrgastbetrieb
10 - desksta - Taster Stationsbesetzung
11 - deskon - Taster Ein/Aus
12 - deskcall - Taster Durchsage
13 - deskrw - Taster Rückwärts
14 - deskvw - Taster Vorwärts
15 - cablelocin - Kabelposition OK
16 - spcwfrwrn - Spinelli Spanwagen Warnung vorne
```

# Elemente

## Lampen

- Blau: LEDQuittierenSystem
- Gelb: LEDQuittierenBetrieb
- ftPixel: Schlüsselschalter
- Weiß: An/Aus
- Blau: Starten

## Taster

- Slider: Wahltaster Geschwindigkeit (links: 1, rechts: 3)
- Schiebetaster links: Schlüsselschalter
- Schalter rechts: Komfortregelung (Besetzung)

## ftPixel oben

| Reihe | Spalte | Funktion                                                                     |
|-------|--------|------------------------------------------------------------------------------|
| 1     | 1      | Ampel Links Feuerfahrt                                                       |
| 1     | 2      | Ampel Links ???                                                              |
| 1     | 3      | Ampel Links ???                                                              |
| 1     | 4      | Seilposition Out                                                             |
| 2     | 1      | Ampel Rechts Feuerfahrt                                                      |
| 2     | 2      | Ampel Rechts ???                                                             |
| 2     | 3      | Ampel Rechts ???                                                             |
| 2     | 4      | Seilposition In                                                              |
| 3     | 1      | LED Förderung (nur simulation - osimf)                                       |
| 3     | 2      | LED Bahnsteig (nur simulation - osimb)                                       |
| 3     | 3      | LED Flugsicherung (nur simulation - osimfl)                                  |
| 3     | 4      | LED TOP (nur simulation - osimn)                                             |
| 4     | 1      | (Simulation - osimfa) Status Fahrt (Speed-Gradient von rot=off zu grün=fast) |
| 4     | 2      | (Simulation - osimmnot) Systemstatus (Grün=Ok, Gelb=Warn, Rot=Fatal)         |
| 4     | 3      | (Simulation - osimlock) Lock-Status (Rot=Locked)                             |

# Ungebunden

**uselessguy**

- deskspdp
- emergi
- cablelocout
- spcclampclosed
- spcwfrend
- spcwbend
- spcwbwrn
- spcclamp

**next_to_power**

- spfntc
- m1ntc
- m2ntc
- m3ntc
- lucclamp

**kelda**

- lubntc
- lufkey
- lubemerg
- lucclampclosed

**errgehbeh**

- lufntc
