# Synguard Platform & Architecture (V.3.01)

## 1. Deployment Models
* **Cloud Solution:** 100% web-based, unlimited scalability, automatic upgrades, nightly backups, 99% uptime. Covers modules like visitor, parking, building, and key management. Uses HTTPS (Port 443) and dynamic cloud IP addresses (main, fallback, provider-fallback).
* **On-Premise:** Runs on Windows Server or Linux (Red Hat). Requires specific license requests and a customer-specific 'bespoke' after ordering. Default Application Port: 8443, Default Network Port: 8444. Requires a TLS certificate for the FQDN.

## 2. Technical Component Stack
* **Webserver:** Apache Tomcat
* **Database:** SQL Server OR PostgreSQL
* **Hardware Integration:** Connects to Synguard Controllers (SynCon Evo) via HTTPS, and supports integrations via OPC, XML SOAP, and REST API.

## 3. Software Licensing Model
* **Volume Licenses (Per Unit):** Active Employee, Wireless-Lock/Handles, Locker, Bio (Active Employee), Parking Space, View-Object, eCLIQ (Cylinder-lock), ANPR Camera.
* **Feature / Module Licenses (Flat Fee):** Visitor, View (Alarm handling), Milestone (CCTV), NetworkOptix (CCTV), Webservice (API), Employee-Webservice (API), MultiRealm, Event-Tree, OPC / SynApp.

## 4. Platform Presets & Configurations
* **Who (Employees & Users):** Fields include Realm, Employee Code, Contract Number, Identifications (Badge, Keycode, Fingerprint, Face, Misc. credentials). Supports Mifare Classic and Mifare DESFire.
* **When (Time Management):** Uses Timetables (e.g., Cleaning team 4AM-8AM), Calendar days, Holiday/Special day handling.
* **Where (Hardware Tree):** Network Items tree contains SynConEvo controller servers, Aperio TCP channels (Aperio Hub/Handle), Salto management, and specific input/output definitions.