"Er is misbruik op de parking: medewerkers geven hun badge door. We hebben Timed Anti-Passback nodig op de slagbomen."
[---SPLIT-DOSSIER---]
### 📑 1. EXECUTIVE SUMMARY & BUSINESS CASE

The proposed development of a Timed Anti-Passback feature for parking management addresses a critical issue of badge-sharing among employees, which leads to unauthorized parking space usage. This functionality is requested in an official tender and promises significant business value by enhancing security and operational efficiency in parking management systems. The solution is designed to be multi-tenant, allowing reuse across various sectors such as healthcare and corporate offices. The financial impact includes a project value of €15, with direct loadable value from customization/licensing at €4 and an expected annual recurring revenue of €2. The value chain benefits include immediate fraud prevention for end customers, competitive advantages in parking tenders for partners, and expanded software capabilities for Synguard.

### ⚖️ 2. STRATEGIC DIRECTOR EVALUATION MATRIX (WORKING METHOD)

- **Strategic Vision fit (Yes/No + Waarom):** Yes. This feature aligns with Synguard's strategic vision to enhance security and operational efficiency in access management systems. It expands the functionality of existing products and meets market demands for fraud prevention in parking management.

- **Technical Feasibility (High/Medium/Low + Waarom):** High. The implementation of Timed Anti-Passback is feasible within the existing SynCon Evo and SynApp architecture. The system's ability to operate independently during network outages ensures reliability, and the integration with the internal Synguard database supports seamless functionality.

- **Functional Sufficiency (Sufficient/Incomplete):** Sufficient. The scenarios and current pain points are clearly defined, with specific requirements such as adjustable time matrices per badge/group, override rights for management, and alerts for misuse attempts. This clarity minimizes the risk of misunderstandings during development.

- **Genericity & Multi-tenant Value (Generic/Customer Specific):** Generic. The solution is designed to be multi-tenant, providing value across different customer segments and industries, thereby enhancing its applicability and marketability.

### 🔧 3. FUNCTIONAL SPECIFICATIONS (BASE FOR STATEMENT OF WORK)

1. **The system shall** provide an adjustable time matrix for each badge or group, allowing operators to set a specific time block during which a badge cannot be reused after initial entry.

2. **The system shall** include override rights for management, enabling authorized personnel to bypass the Timed Anti-Passback restrictions when necessary.

3. **The system shall** generate alerts in real-time when a misuse attempt is detected, such as a badge being presented again within the restricted time frame.

4. **The system shall** operate independently at the controller level (SynCon Evo) to ensure functionality during network outages, maintaining parking management operations without interruption.

5. **The system shall** integrate seamlessly with the internal Synguard database and logic firmware on SynCon Evo, ensuring consistent data processing and management.

6. **The system shall** provide a user-friendly interface with a simple checkbox to activate the Timed Anti-Passback feature and an input field for setting the time limit in minutes at the door properties level.

These specifications serve as the foundation for the development team's technical analysis and subsequent implementation of the Timed Anti-Passback feature in Synguard's parking management systems.
[---SPLIT-DOSSIER---]
## Functional Requirements

### FR-001: Adjustable Time Matrix
**Traces to:** CN-001 — Fraud prevention in parking management

The system shall provide an adjustable time matrix for each badge or group, allowing operators to set a specific time block during which a badge cannot be reused after initial entry.

**Acceptance Criteria:**
- [ ] Operators can configure time blocks for badge reuse restrictions via the SynApp interface.
- [ ] System prevents badge reuse within the configured time block.
- [ ] Time matrix settings are stored and retrievable from the Synguard database.

### FR-002: Override Rights for Management
**Traces to:** CN-002 — Operational efficiency in parking management

The system shall include override rights for management, enabling authorized personnel to bypass the Timed Anti-Passback restrictions when necessary.

**Acceptance Criteria:**
- [ ] Management can override restrictions via a secure login in SynApp.
- [ ] System logs all override actions with timestamp and user ID.
- [ ] Override functionality is accessible only to users with appropriate permissions.

### FR-003: Real-Time Alerts for Misuse Attempts
**Traces to:** CN-003 — Security enhancement in parking management

The system shall generate alerts in real-time when a misuse attempt is detected, such as a badge being presented again within the restricted time frame.

**Acceptance Criteria:**
- [ ] System sends alerts to designated personnel via email or SMS.
- [ ] Alerts include details of the misuse attempt, such as badge ID and timestamp.
- [ ] System logs all alerts in the Synguard database for audit purposes.

### FR-004: Independent Operation at Controller Level
**Traces to:** CN-004 — Reliability during network outages

The system shall operate independently at the controller level (SynCon Evo) to ensure functionality during network outages, maintaining parking management operations without interruption.

**Acceptance Criteria:**
- [ ] SynCon Evo processes Timed Anti-Passback logic locally without network dependency.
- [ ] System maintains full functionality during network outages.
- [ ] System synchronizes data with SynApp once network connectivity is restored.

### FR-005: Seamless Integration with Synguard Database
**Traces to:** CN-005 — Consistent data processing and management

The system shall integrate seamlessly with the internal Synguard database and logic firmware on SynCon Evo, ensuring consistent data processing and management.

**Acceptance Criteria:**
- [ ] System updates database records in real-time with badge usage data.
- [ ] Integration supports bidirectional data flow between SynApp and SynCon Evo.
- [ ] System ensures data integrity during synchronization processes.

### FR-006: User-Friendly Interface for Feature Activation
**Traces to:** CN-006 — Ease of use for operators

The system shall provide a user-friendly interface with a simple checkbox to activate the Timed Anti-Passback feature and an input field for setting the time limit in minutes at the door properties level.

**Acceptance Criteria:**
- [ ] Operators can activate/deactivate the feature with a single click.
- [ ] Interface includes an input field for setting time limits in minutes.
- [ ] Changes to settings are immediately reflected in the system operations.

---

## Non-Functional Requirements

### NFR-001: Performance
**Traces to:** CN-004 — Reliability during network outages

The system shall process Timed Anti-Passback logic within 1 second of badge presentation under normal load conditions.

**Measurement Criteria:**
- **Target:** < 1 second processing time for 95th percentile
- **Minimum Acceptable:** < 2 seconds for 99th percentile
- **Measurement Method:** Application performance monitoring (APM)

**Acceptance Criteria:**
- [ ] System processes badge data within the specified time frame.
- [ ] Performance maintained with 100 concurrent badge presentations.
- [ ] Response time logged for monitoring.

### NFR-002: Security
**Traces to:** CN-003 — Security enhancement in parking management

The system shall encrypt all data transmissions between SynApp and SynCon Evo using AES-256 encryption.

**Measurement Criteria:**
- **Target:** AES-256 encryption for all data transmissions
- **Minimum Acceptable:** No unencrypted data transmissions
- **Measurement Method:** Security audit and penetration testing

**Acceptance Criteria:**
- [ ] All data transmissions are encrypted using AES-256.
- [ ] System passes security audits with no vulnerabilities.
- [ ] Encryption status logged for audit purposes.

### NFR-003: Usability
**Traces to:** CN-006 — Ease of use for operators

The system shall allow operators to configure Timed Anti-Passback settings within 3 minutes.

**Measurement Criteria:**
- **Target:** < 3 minutes configuration time
- **Minimum Acceptable:** < 5 minutes configuration time
- **Measurement Method:** Usability testing with operators

**Acceptance Criteria:**
- [ ] Operators can configure settings within the specified time frame.
- [ ] Interface provides clear instructions and feedback.
- [ ] Usability testing results logged for improvement.

---

## Traceability Matrix

| FR/NFR ID | Traces To CN | Description |
|-----------|--------------|-------------|
| FR-001 | CN-001 | Adjustable time matrix for badge reuse restrictions |
| FR-002 | CN-002 | Override rights for management |
| FR-003 | CN-003 | Real-time alerts for misuse attempts |
| FR-004 | CN-004 | Independent operation at controller level |
| FR-005 | CN-005 | Seamless integration with Synguard database |
| FR-006 | CN-006 | User-friendly interface for feature activation |
| NFR-001 | CN-004 | Performance requirements for processing logic |
| NFR-002 | CN-003 | Security requirements for data encryption |
| NFR-003 | CN-006 | Usability requirements for configuration |

---

*Created: [Date]*  
*Last Updated: [Date]*  
*Author: Requirements Team*