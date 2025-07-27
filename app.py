# Installer: pip install streamlit
import streamlit as st

def main():
    st.title("Détecteur de Faux Articles")
    st.write("Entrez un article pour vérifier son authenticité")
    
    # Input text
    article_text = st.text_area("Texte de l'article:", height=300)
    
    if st.button("Analyser"):
        if article_text:
            result = predict_fake_news(article_text, model_type='rf')
            
            st.subheader("Résultats:")
            
            if result['prediction'] == 'REAL':
                st.success(f"✅ Article probablement AUTHENTIQUE")
            else:
                st.error(f"❌ Article probablement FAUX")
            
            st.write(f"**Score d'authenticité:** {result['authenticity_percentage']}%")
            st.write(f"**Confiance du modèle:** {result['confidence_score']}%")
        else:
            st.warning("Veuillez entrer un texte à analyser")

if __name__ == "__main__":
    main()

# Lancer avec: streamlit run app.py