# temponizer-client

Python-klientbibliotek til Temponizer API'et — en dansk platform til arbejdsstyrke- og vagtplanlægning — med OAuth2-autentificering og adgang til medarbejdere, institutioner og vagtplaner.

> Denne klient er ikke officielt støttet eller godkendt af Temponizer. Brug på eget ansvar.

## Nuværende funktionalitet

- OAuth2-autentificering via password grant flow med klientcredentials
- Hent én medarbejder efter ID (`hent_medarbejder`) eller alle medarbejdere (`hent_alle_medarbejdere`)
- Hent én institution efter ID (`hent_institution`) eller alle institutioner (`hent_alle_institutioner`)
- Hent vagtplaner filtreret på type og datointerval via `PlanType`-enum (`hent_vagtplan`):
  `RECENT`, `UPCOMING`, `ONGOING`, `HELD_UNAPPROVED`, `HELD_APPROVED`, `OBSERVE`, `CANCELLED_FILLED`, `EXCLUDED_FROM_INVOICING`
- Al funktionalitet tilgængeligt via `TemponizerClientManager`-facaden, der latsyinitialiserer delklienter

## Installation

```bash
uv add git+https://github.com/odense-rpa/temponizer-client
```

## Forudsætninger

- Python ≥ 3.13
- Adgang til en Temponizer-instans med OAuth2-klientcredentials

## Konfiguration

Opret en `.env`-fil (se `env.example`) med følgende variabler:

| Variabel | Beskrivelse |
|---|---|
| `INSTANCE` | Subdomæne til instansen — API-URL bygges som `<INSTANCE>.temponizer.dk` |
| `CLIENT_ID` | OAuth2-klient-ID |
| `CLIENT_SECRET` | OAuth2-klienthemmelighed |
| `MAIL` | Brugernavn (e-mail) til OAuth2 password grant |
| `PASSWORD` | Adgangskode til OAuth2 password grant |

## Brug

```python
import os
from datetime import date
from dotenv import load_dotenv
from temponizer_client import TemponizerClientManager

load_dotenv()

manager = TemponizerClientManager(
    instance=os.environ["INSTANCE"],
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    username=os.environ["MAIL"],
    password=os.environ["PASSWORD"],
)

# Hent alle medarbejdere
medarbejdere = manager.medarbejder.hent_alle_medarbejdere()

# Hent én medarbejder efter ID
medarbejder = manager.medarbejder.hent_medarbejder(42)

# Hent alle institutioner
institutioner = manager.institutioner.hent_alle_institutioner()

# Hent kommende vagtplaner i et datointerval
planer = manager.vagtplaner.hent_vagtplan(
    startdato=date(2025, 1, 1),
    slutdato=date(2025, 1, 31),
    plantype=TemponizerClientManager.PlanType.UPCOMING,
)
```

## Licens

MIT
