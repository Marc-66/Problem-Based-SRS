import streamlit as st
import os
from openai import OpenAI
from openai.lib.azure import AzureOpenAI
from dotenv import load_dotenv

# Netjes de API-key laden
load_dotenv()
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

if azure_api_key or azure_endpoint:
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        azure_deployment=azure_deployment,
        api_version=azure_api_version,
        api_key=azure_api_key,
    )
else:
    client = OpenAI(api_key=openai_api_key)

# Hulpfunctie om lokale Markdown-bestanden in te lezen voor de AI-context
def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Laad de Synguard specifieke kennis in
synguard_products = read_file("knowledge/synguard_products.md")
tech_partners = read_file("knowledge/technology_partners.md")
cp_skill = read_file("skills/customer-problems/SKILL.md")
fr_skill = read_file("skills/functional-requirements/SKILL.md")

# UI Opzet via Streamlit
st.set_page_config(page_title="Synguard AI Requirements Agent", layout="wide")
st.title("🛡️ Synguard AI Requirements Architect")
st.subheader("Vertaal ongestructureerde klantvragen automatisch naar technische specificaties")

# Splitst het scherm in een invoer- en uitvoerkolom
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 📥 Klant Input")
    client_input = st.text_area(
        "Plak hier de e-mail, transcriptie of ruwe aanvraag van de klant/integrator:",
        height=200,
        placeholder="Bijvoorbeeld: 'The Belgian vraagt om een bezoekersmodule bij project X...'"
    )
    
    development_type = st.selectbox(
        "Wat voor type ontwikkelingsverzoek is dit?",
        [
            "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
            "2. Back-end Software integrations with 3rd party solution",
            "3. New Software functionality impacting flow/operation/logic/UI",
            "4. New functionality related to Mobile app or Cloud",
            "5. New requirements related to Cyber Security or local Compliance",
            "6. New requirement related to AI & Data specific"
        ]
    )

    # --- DE BUSINESS VALUE EXPANDER (VISUELE VELDEN OP HET SCHERM) ---
    with st.expander("💼 Commerciële Impact & Business Value (Optioneel)"):
        st.markdown("#### Commerciële Driver")
        business_driver = st.radio(
            "Wat is de primaire reden voor deze aanvraag?",
            [
                "Requested in Official Tender",
                "Requested as 'Custom Work' via Partner",
                "Required to win the Project/End Customer",
                "Required to Onboard new Partner",
                "Required to compete with competitor",
                "Requested by the Partner to become more competitive",
                "Request is based on market or technology trend",
                "New Idea to increase the overall value of Synguard"
            ]
        )
        
        is_customer_specific = st.radio(
            "Is dit specifiek voor één klant of herbruikbaar?",
            ["Customer Specific (Unique)", "Usable by other customers as well (Multi-tenant)"]
        )
        
        st.markdown("#### Markt & Verticalen")
        verticals = st.multiselect(
            "Voor welke specifieke Vertical(s) is dit bedoeld?",
            ["Government", "Data Centre", "Hospital / Healthcare", "Logistics", "School / Education", "Offices / Corporate"]
        )
        
        benchmark_competitor = st.text_input("Wat is de best concurrerende oplossing ter benchmark?", placeholder="Nedap AEOS")
        
        st.markdown("#### Links & Referenties")
        link_project = st.text_input("Link naar Eindklant / Project / Tender:")
        link_product = st.text_input("Link naar Productdata / API documentatie:")
        
        st.markdown("#### Financiële Cijfers")
        total_project_value = st.number_input("Totale Projectwaarde náást deze aanvraag (in €):", min_value=0, value=0, step=1000)
        chargeable_value = st.number_input("Wat kunnen we hiervoor rekenen (Licentie, Maatwerk in €):", min_value=0, value=0, step=500)
        potential_yearly_revenue = st.number_input("Potentiële nieuwe omzet voor Synguard per jaar (in €):", min_value=0, value=0, step=1000)

        st.markdown("---")
        st.markdown("#### 🎯 Business Value Proposition")
        
        resolved_problem = st.text_area(
            "Wat lost deze aanvraag concreet op?",
            placeholder="Bijvoorbeeld: Voorkomt handmatige dubbele invoer..."
        )
        
        value_end_customer = st.text_area(
            "Welke waarde krijgt de EINDKLANT?",
            placeholder="Bijvoorbeeld: Betere User Experience..."
        )
        
        value_partner = st.text_area(
            "Welke waarde krijgt de PARTNER/INTEGRATOR?",
            placeholder="Bijvoorbeeld: Kan grotere enterprise tenders winnen..."
        )
        
        value_synguard = st.text_area(
            "Welke waarde krijgt SYNGUARD hierdoor?",
            placeholder="Bijvoorbeeld: Blijft de brand reference..."
        )

        # --- NIEUW: FUNCTIONAL DESCRIPTION EXPANDER ---
    with st.expander("📝 Functional Description & Scenarios (Technisch)"):
        st.markdown("#### 1.1 Functionele Beschrijving & Context")
        
        current_situation = st.text_area(
            "Huidige situatie & Pijnpunten (Current Situation):",
            placeholder="Bijvoorbeeld: We hebben nu 3 receptionisten nodig en het duurt 20 minuten per bezoeker..."
        )
        
        overall_workflow = st.text_area(
            "Algemene Workflow / User Scenario (Wie doet wat, wat is het resultaat?):",
            placeholder="Bijvoorbeeld: Als host nodig ik een bezoeker uit via Outlook. Bezoeker krijgt QR-code..."
        )
        
        desired_functionality = st.text_area(
            "Lijst van Gewenste Functionaliteiten (Bullet list van specifieke eisen):",
            placeholder="- De integratie met NX moet bidirectioneel zijn\n- Virtuele knop in NX UI om deur te openen\n- Video-bookmark linken aan access event"
        )
        
        st.markdown("#### External Integrations (Indien van toepassing)")
        integration_details = st.text_area(
            "Details over externe integratie (Systeemnaam, Doel, Data-uitwisseling, API beschikbaar?):",
            placeholder="Systeem: iLOQ S5\nDoel: Sleutels realtime synchroniseren\nAPI: Ja, REST API documentatie beschikbaar via link."
        )
        
        st.markdown("#### Kwaliteit & Randvoorwaarden")
        ui_ux_expectations = st.text_input("UI/UX Verwachtingen (Lay-out, voorkeuren):", placeholder="Operator moet een event binnen 3 klikken kunnen verwerken.")
        acceptance_criteria = st.text_area("Acceptatiecriteria (Wanneer is de oplossing 'goed genoeg'?):", placeholder="- Updates moeten realtime worden verzonden\n- Feature werkt op desktop en mobiel")
        constraints_conditions = st.text_area("Restricties & Condities (IT-infrastructuur, security, deadlines):", placeholder="Moet voldoen aan ISO 27001; Deadline voor oplevering is Q4 2026.")
        
        st.markdown("#### 1.2 Officiële Teksten & Externe Documenten")
        tender_text = st.text_area("Specifieke Aanbestedingstekst / Tender / Compliance tekst:", placeholder="Plak hier de letterlijke paragrafen uit het lastenboek...")
        
    generate_button = st.button("🚀 Genereer Requirements Pijplijn", type="primary")

with col2:
    st.markdown("### 📤 AI Agent Output")
    
    if generate_button and client_input:
        with st.spinner("AI is de Synguard Kennisbank en SRS-methodiek aan het toepassen..."):
            
            # --- DEFINITIEVE PROMPT INCLUSIEF FUNCTIONELE DETAILS ---
            prompt_step1 = f"""
            Je bent de Synguard AI Requirements Agent. Jouw taak is om de klantinput, de commerciële context én de functionele specificaties te synthetiseren tot een formeel Software Requirements Specification (SRS) blauwdruk voor engineering.
            
            === 1. CLASSIFICATIE ===
            Type Ontwikkeling: {development_type}
            
            === 2. BUSINESS VALUE & ROI ===
            - Primaire Driver: {business_driver}
            - Herbruikbaarheid: {is_customer_specific}
            - Doelgroep (Verticals): {', '.join(verticals) if verticals else 'Niet gespecificeerd'}
            - Benchmark Concurrent: {benchmark_competitor}
            - Financiële Impact: 
              * Totale overige projectwaarde: €{total_project_value}
              * Direct laadbare waarde (Maatwerk/Licentie): €{chargeable_value}
              * Verwachte jaarlijkse herhalende omzet (ARR): €{potential_yearly_revenue}
            - Waarde Keten: Eindklant ({value_end_customer}), Partner ({value_partner}), Synguard ({value_synguard})
            
            === 3. FUNCTIONAL REQUIREMENTS & SCENARIOS ===
            - Huidige situatie & Pijn: {current_situation}
            - Gewenste algemene workflow: {overall_workflow}
            - Specifieke functionele eisen: {desired_functionality}
            - Integratie details: {integration_details}
            - UI/UX & Acceptatie: {ui_ux_expectations} | Criteria: {acceptance_criteria}
            - Restricties & Condities: {constraints_conditions}
            - Lastenboek / Tender tekst: {tender_text}
            
            === 4. METHODIEK INSTRUCTIES ===
            {cp_skill}
            
            === 5. RAUWE INLINE INPUT ===
            {client_input}
            
            Genereer een gestructureerd technisch rapport met de volgende vaste onderdelen:
            1. **Executive Summary & Business Case**: Analyseer de ROI en geef advies aan de Sales & Product Director over goedkeuring (gebaseerd op ARR en herbruikbaarheid).
            2. **Current vs Desired Situation**: Breng de pijn en de oplossing in kaart.
            3. **Functional Specifications (SRS)**: Schrijf formele "The system shall..." requirements op basis van de ingevoerde workflows, gewenste functionaliteiten en acceptatiecriteria. Maak onderscheid tussen core flows en integratie-eisen.
            4. **Constraints & Compliance**: Formuleer de harde technische en compliancy-restricties (bijv. UK CAPS of ISO standaarden).
            """
            
            response_step1 = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt_step1}],
                temperature=0.2,
            )
            customer_problems_output = response_step1.choices[0].message.content

            # --- STAP 2: VERTAAL NAAR FUNCTIONELE REQUIREMENTS (HET WAT) ---
            prompt_step2 = f"""
            Je bent de Synguard AI Requirements Agent. Op basis van de zojuist geïdentificeerde Customer Problems ga je nu de harde technische requirements opstellen conform deze methodiek:
            
            {fr_skill}
            
            Zorg dat je hardware (SynCon Evo, lezers) en software (SynApp licenties) correct matcht met behulp van deze bronnen:
            Synguard Eigen Producten: {synguard_products}
            Technologie Partners: {tech_partners}
            
            Geïdentificeerde Customer Problems:
            {customer_problems_output}
            """
            
            response_step2 = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt_step2}],
                temperature=0.2,
            )
            functional_requirements_output = response_step2.choices[0].message.content

            # Toon de resultaten in mooie, overzichtelijke tabbladen
            tab1, tab2 = st.tabs(["🎯 1. Customer Problems (Why)", "⚙️ 2. Technical Requirements (What)"])
            
            with tab1:
                st.markdown(customer_problems_output)
                
            with tab2:
                st.markdown(functional_requirements_output)
                
    elif generate_button and not client_input:
        st.warning("Vul eerst een klantvraag in aan de linkerkant.")
    else:
        st.info("Vul de klantinput in en klik op de knop om de demo te starten.")