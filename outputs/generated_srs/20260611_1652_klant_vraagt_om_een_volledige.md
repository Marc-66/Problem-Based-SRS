# STATUS: PENDING DIRECTORS REVIEW
# GENERATED ON: 2026-06-11 16:52:32

### 📑 1. EXECUTIVE SUMMARY & BUSINESS CASE

The integration of iLOQ RF wireless locks and cylinders into the Synguard ecosystem aims to streamline access management by enabling real-time management of access rights directly from SynApp without the need for physical wiring to doors. This initiative is driven by the need to compete with Nedap AEOS and AEOS Locker Management, offering a multi-tenant solution that can be leveraged across various sectors such as healthcare and government. The financial impact includes a total project value of €50,000, with a direct loadable value of €7,500 and an expected annual recurring revenue (ARR) of €12,000. The integration strengthens SynApp's position as a universal integration platform, enhancing software license value per door.

### ⚖️ 2. STRATEGIC DIRECTOR EVALUATION MATRIX (WORKING METHOD)

- **Strategic Vision fit (Yes + Waarom):** Yes, this integration aligns with Synguard's roadmap to enhance its access management solutions by incorporating cutting-edge wireless technology, thereby expanding its competitive edge and market reach.

- **Technical Feasibility (Medium + Waarom):** Medium. While the SynCon Evo and SynApp architecture are robust, the integration relies on currently unknown partner data and API documentation from iLOQ, which may pose challenges in achieving seamless cloud-to-cloud functionality.

- **Functional Sufficiency (Sufficient):** The scenarios and current pain points are clearly defined, allowing for a comprehensive understanding of the workflow and expected outcomes, minimizing the risk of misinterpretation.

- **Genericity & Multi-tenant Value (Generic):** This solution is generic and offers multi-tenant value, as it can be utilized by various customers across different sectors, enhancing its appeal and scalability.

### 🔧 3. FUNCTIONAL SPECIFICATIONS (BASE FOR STATEMENT OF WORK)

1. **The system shall enable bidirectional synchronization of persons and tokens between Synguard and iLOQ.**
2. **The system shall log real-time events in the Synguard logbook when an iLOQ lock is opened or denied.**
3. **The system shall visually display battery status and alarms of iLOQ locks in SynApp.**
4. **The system shall recognize iLOQ doors in the SynApp tree structure via a unique iLOQ icon.**
5. **The system shall process changes in access rights within 5 seconds via the API in the iLOQ system.**
6. **The system shall operate offline on the locks themselves, ensuring functionality without constant cloud connectivity.**

### 4. CONSTRAINTS & COMPLIANCE

- **Technical Constraints:** The integration must operate fully cloud-to-cloud via the iLOQ Cloud Gateway, eliminating the need for local server installations at the end customer site.
- **Compliance Standards:** The solution must adhere to relevant industry standards such as ISO 27001 for information security management, ensuring data protection and cybersecurity resilience.
- **Operational Constraints:** The system must maintain end-to-end security, ensuring encrypted communication between SynApp and iLOQ systems, and comply with any applicable local regulations regarding data privacy and security.