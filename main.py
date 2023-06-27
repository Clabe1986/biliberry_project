from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html

st.set_page_config(page_title='Biliberry', page_icon='🪴', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---Use local CSS---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding = 'https://assets8.lottiefiles.com/packages/lf20_1plcwvk5.json'
img_contact_form_1 = Image.open('images/bili_jena_m_tromso.jpeg')
img_contact_form_2 = Image.open('images/tromso.png')
img_contact_form_3 = Image.open('images/jena.png')
img_contact_form_4 = Image.open('images/axel.png')
img_contact_form_5 = Image.open('images/laura.png')
img_contact_form_6 = Image.open('images/clabe.png')

with st.container():
    st.markdown("<h1 style='color: blue;'>Plant defence under Arctic light conditions</h1>", unsafe_allow_html=True)
    st.write(
        '''
        Increased temperatures in Subarctic and Arctic regions caused by climate change, especially in Scandinavia, lead us to expect an increase in agriculture and its yields in these regions. At the same time, pathogens and pests will reduce these yields again, as climate change will also favour the spread of such organisms into these regions. This means that the climate change-induced loss of previously agriculturally used areas in the South will most likely not be compensated by newly added areas in the North. On the contrary, new invasive pests may cause greater damage than locally occurring ones. However, this scenario may prove to be incorrect. 
        A number of studies show that with increasing latitude, the constitutive chemical defense present in plants increases, and with it their resistance to pests. The reason for this is unknown. We suspect that the length of the day in summer at high Northern latitudes plays a major role. It can positively influence the light-dependent accumulation of a plant hormone, jasmonate. This phytohormone then ensures the increased synthesis and accumulation of chemical defense substances, which provides the plants greater resistance. 
        Our proposal aims to uncover these connections. Field studies with naturally growing bilberries (wild forms of blueberries; Vaccinium myrtillus L.) under Arctic summer conditions in Norway (Tromsø: 69° N) including a long-lasting period of days with 24 h sunshine, in comparison with plants growing in Germany (Jena: 50° N) will show the impact of such light conditions on the plants’ defensive system. Comprehensive analyses include phenotypic leaf traits, targeted phytohormone determination, untargeted metabolomics, transcriptomics and controlled herbivore treatments. This will provide insights in understanding the mechanisms of light-dependent defense regulation in bilberries. Knowledge of the underlying molecular and phytochemical processes can help to increase the resistance of many plants and may have a transformative impact on plants in general and agriculture of crops in particular. 
        '''
    )
    st.markdown("[Click here to see more...](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9729949/)")

    st.write('##')
    st.image(img_contact_form_1)

# ---PROJECTS---
with st.container():
    st.header('What we plan to do')
    st.write(
            '''
            In order to study the impact of Arctic summer light conditions on the defense capacity of plants grown in the far North against present and invasive insect herbivores, we will combine experimental lab studies with field studies. The latter will be performed at two sites, one will be in Tromsø, Norway, the other in Jena, Germany. The plant of choice is the holoarctic shrub bilberry (Vaccinium myrtillus L.). Bilberry occurs naturally in both countries. In a reciprocal transplant experiment, we will first monitor the performance of bilberry plants in the field, grown under the respective light conditions in Jena and Tromsø. In parallel, the environmental weather and light conditions will be monitored as well. In a second step, we will analyse and compare the phytohormones, as well as metabolites and transcriptome changes of those plants. The use of modern techniques such as LC-MS/MS for metabolomics and RNAseq for transcriptomics provides the ideal experimental approaches. Third, based on the obtained results, we will perform a series of experiments with controlled herbivore infestation under the different light conditions and analyse the defensive responses by targeted metabolomics and gene expression analyses.
            '''
        )
with st.container():
    image_column, text_column = st.columns(2)
    with image_column:
        st.markdown("<h3 style='font-size: 20px;'><em>Jena, Germany (50° N)</em></h3>", unsafe_allow_html=True)
        st.image(img_contact_form_3)

    with text_column:
        st.markdown("<h3 style='font-size: 20px;'><em>Tromsø Norway, (69° N)</em></h3>", unsafe_allow_html=True)
        st.image(img_contact_form_2)

    # ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Please contact us!")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
      <form action="https://formsubmit.co/simiyu86wekesa@gmail.com" method="POST">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Your name" required>
          <input type="email" name="email" placeholder="Your email" required>
          <textarea name="message" placeholder="Your message here" required></textarea>
          <button type="submit">Send</button>
      </form>
      """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

with st.container():
    st.write('##')
    st.write('___')
    st.header('Publications and Presentations')
    st.write(
            '''
            Mithöfer, A., Riemann, M., Faehn, C. A., Mrazova, A., & Jaakola, L. (2022). Plant defense under Arctic light conditions: Can plants withstand invading pests?. Frontiers in plant science, 13, 1051107. https://doi.org/10.3389/fpls.2022.1051107.
            '''
        )

with st.container():
    st.write('##')
    st.write('___')
    axel, laura, clabe = st.columns(3)
    with axel:
        st.image(img_contact_form_4)
        text = "PD. Dr. Axel Mithöfer<br>Group Leader, <br>Research Group Plant Defense Physiology<br>Max Planck Institute for Chemical Ecology\n\n[For more information](https://www.ice.mpg.de/person/111877/2824)"
        st.markdown(f"<h3 style='font-size: 16px;'>{text}</h3>", unsafe_allow_html=True)

    with laura:
        st.image(img_contact_form_5)
        text = "Prof. Dr. Laura Jaakola<br>Department of Arctic and Marine Biology<br>UiT The Arctic University of Norway\n\n[For more information](https://en.uit.no/ansatte/person?p_document_id=301772)"
        st.markdown(f"<h3 style='font-size: 16px;'>{text}</h3>", unsafe_allow_html=True)

    with clabe:
        st.image(img_contact_form_6)
        #st.markdown("<h3 style='font-size: 20px;'><em>Dr. Clabe Wekesa</em></h3>", unsafe_allow_html=True)
        text = "Dr. Clabe Wekesa<br>Post Doctoral Fellow, <br>Research Group Plant Defense Physiology<br>Max Planck Institute for Chemical Ecology\n\n[For more information](https://www.ice.mpg.de/person/128684/2824)"
        st.markdown(f"<h3 style='font-size: 16px;'>{text}</h3>", unsafe_allow_html=True)









