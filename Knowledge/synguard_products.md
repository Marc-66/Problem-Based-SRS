# Synguard Eigen Producten Catalogus

## Core Software Modules
### Synguard Visitor Management (LIC-VISITOR)
- **Type:** Software Licentie Module.
- **Beschrijving:** Module voor het pre-registreren en beheren van externe gasten.
- **Compatibiliteit:** Werkt samen met alle ondersteunde QR- en BLE-lezers (zie partner catalogus).

## Hardware Controllers
### Synguard Master Controller (SMC-01)
- **Type:** Fysieke Main Controller.
- **Protocollen:** OSDP v2, Wiegand.
- **Max Capaciteit:** 4 fysieke lezers direct bekabeld.

# Synguard Eigen Producten & Architectuur Matrix

Dit document bevat de core softwareplatforms, modulaire hardware-architectuur en licentiemodules van Synguard. Het dient als de primaire bron van waarheid (Source of Truth) voor de AI-agent om technische ontwerpen te valideren.

---

## 1. Software Platforms (The Management Layer)

### SynApp
- **Type:** Web-based Centraal Management Platform.
- **Beschrijving:** De intuïtieve, browser-gebaseerde interface van Synguard voor het beheer van personen, toegangsrechten, tijdregistratie en bezoekers.
- **Relaties & Logica:** - Communiceert direct met de hardware controllers (SynCon Evo) via IP (HTTPS/Websockets).
  - Fungeert als de host voor alle functionele softwaremodules (licenties).
  - Kan via API's gekoppeld worden aan externe HR-systemen, Active Directory (Azure AD) en ERP-systemen.

---

## 2. Hardware Architecture (The Control Layer)

### SynCon Evo (Main Controller)
- **Type:** Modulaire IP-Controller / Master-paneel.
- **Beschrijving:** De nieuwste generatie hoogbeveiligde, intelligente controller die lokaal de beslissingen neemt (zelfs offline wanneer de verbinding met SynApp wegvalt).
- **Poorten & Interfaces:** Onboard Ethernet (IP), RS-485 bus voor uitbreidingsmodules.
- **Relaties & Logica:**
  - Stuurt via de RS-485 bus de sub-modules (SynCon Evo Extensions) aan.
  - Verwerkt protocollen zoals OSDP v2 (bevoorrecht) en Wiegand via de aangesloten lezer-modules.

### SynCon Evo Extension Modules (Sub-panelen)
- **Type:** Hardware Uitbreidingsmodules op DIN-rail.
- **Varianten:**
  - *SynCon Evo Reader Module:* Specifieke uitbreiding voor het fysiek bekabelen van badgelezers (bijv. STid, Idesco) via OSDP of Wiegand.
  - *SynCon Evo I/O Module:* Voor het aansturen van extra relais (sloten, slagbomen) en het inlezen van inputs (deurcontacten, drukknoppen).
- **Relaties:** Moet altijd via de RS-485 bus verbonden zijn met een master *SynCon Evo*.

---

## 3. Software Licenties & Functionele Modules

### LIC-BASE (Synguard Basislicentie)
- **Type:** Core Software Licentie.
- **Voorwaarde:** Altijd vereist voor elk Synguard project. Activeert het SynApp basisplatform en de communicatie met de eerste SynCon Evo controllers.

### LIC-VISITOR (Bezoekersbeheer)
- **Type:** Functionele Uitbreidingsmodule.
- **Beschrijving:** Module binnen SynApp voor pre-registratie, e-mailuitnodigingen en registratie van externe gasten.
- **Relaties & Logica:** Triggered automatisch de behoefte aan identificatiehardware aan de buitenschil (bijv. een QR-code lezer van Axis of poortsturing via kentekenherkenning van Nedap).

### LIC-LPR (Kentekenherkenning Integratie)
- **Type:** Integratiemodule.
- **Beschrijving:** Module voor het koppelen van ANPR/LPR camera's aan het centrale rechtenbeheer.
- **Relaties:** Koppelt kentekens rechtstreeks aan personen in SynApp en stuurt bij een match de *SynCon Evo I/O Module* aan die de slagboom opent.

### LIC-BIOMETRICS (Geavanceerde Identificatie)
- **Type:** Security Module.
- **Beschrijving:** Module voor het synchroniseren en beheren van biometrische templates.
- **Relaties:** Noodzakelijk zodra er in de hardware-laag gekozen wordt voor partners zoals Palmki (handpalm) of Suprema (gezicht/vingerafdruk).

### LIC-PARKING (Slim Parkeerbeheer)
- **Type:** Logistieke Module.
- **Beschrijving:** Beheert parkeercapaciteit, telt aanwezige voertuigen en regelt zone-toegang.
- **Relaties:** Integreert vaak nauw samen met partnersoftware *Commuty* en hardware van *Nedap*.

---

## 4. Architectuur & Validatie Regels (Harde restricties voor de AI)

- **Regel 1 (Offline Werking):** Alle kritieke toegangslogica (wie mag wanneer waarbinnen) MOET door SynApp naar de *SynCon Evo* worden gepusht. De AI mag nooit een requirement ontwerpen waarbij de fysieke deur afhankelijk is van een live internetverbinding om te openen.
- **Regel 2 (Modulariteit):** Een uitbreidingsmodule (Reader/IO) kan NOOIT direct met SynApp praten; er moet altijd een *SynCon Evo Master* tussen zitten.
- **Regel 3 (Licentie-afhankelijkheid):** Elk gebruik van een specifieke partnermodule (bijv. GoBright voor roombooking) vereist naast de partnerkoppeling ook de activering van de corresponderende functionele module in SynApp.