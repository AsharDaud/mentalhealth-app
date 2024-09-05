import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="Apllication System",
    page_icon=":brain:"
)


st.title("Contact Page")

with st.form(key='contact_form'):
        email = st.text_input("E-mail :e-mail:", placeholder="Ketik alamat e-mail anda disini...")
        message = st.text_area("Pesan :email:", height=150, placeholder="Ketik pesan anda disini...")
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            if '@' not in email:
                st.error(":warning: Email harus mengandung '@'. Silakan masukkan alamat email yang valid.")
            elif message.strip() == "":
                st.error(":warning: Pesan tidak boleh kosong. Silakan ketik pesan anda.")
            else:
                st.success(":white_check_mark: Terima kasih! Pesan anda telah diterima.")
            # Here you can add code to handle the submitted form, like sending an email or saving the data

st.divider()

st.subheader("Contact Info :rotating_light:")
st.caption("Berikut adalah informasi terkait kontak developer.")

col1, col2, col3 = st.columns(3)

with col1:
    with st.popover(" :e-mail: Contact e-mail"):
       st.subheader(" :e-mail: e-mail")
       st.markdown("Silahkan hubungi saya lewat :arrow_lower_left:")
       st.write(" :envelope_with_arrow: ashardaud11@gmail.com")

with col2:
    with st.popover(" :calling: Contact Phone"):
        st.subheader(" :calling: Phone")
        st.markdown("Silahkan hubungi saya lewat :arrow_lower_left:")
        st.write(" :phone: https://wa.me/6289529851046")


with col3:
    with st.popover(" :round_pushpin: Pin Address"):
         data = pd.DataFrame({
             'lat': [-7.8269],
             'lon': [112.6958]
             })
         layer = pdk.Layer(
            'ScatterplotLayer',
                    data,
                    get_position='[lon, lat]',
                    get_radius=100,
                    get_color=[255, 0, 0],
                    pickable=True
                )
         view_state = pdk.ViewState(
                latitude=-7.8269,
                longitude=112.6958,
                zoom=13,
                pitch=50
            )
         r = pdk.Deck(layers=[layer], initial_view_state=view_state)
         st.pydeck_chart(r)
         



