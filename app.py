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
        height=400,
        placeholder="Bijvoorbeeld: 'The Belgian vraagt om een bezoekersmodule bij project X. Ze willen dat gasten via een QR-code binnenkomen bij de slagboom...'"
    )
    generate_button = st.button("🚀 Genereer Requirements Pijplijn", type="primary")

with col2:
    st.markdown("### 📤 AI Agent Output")
    
    if generate_button and client_input:
        with st.spinner("AI is de Synguard Kennisbank en SRS-methodiek aan het toepassen..."):
            
            # --- STAP 1: AFLEIDEN VAN CUSTOMER PROBLEMS (HET WAAROM) ---
            prompt_step1 = f"""
            Je bent de Synguard AI Requirements Agent. Jouw taak is om de klantinput te analyseren conform deze methodiek:
            
            {cp_skill}
            
            Gebruik de Synguard product- en partnercontext om entiteiten te begrijpen, maar focus je HIER puur op de PROBLEMEN van de klant (Subject, Verb, Object, Penalty).
            
            Synguard Producten:
            {synguard_products}
            
            Input van de klant:
            {client_input}
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