import streamlit as st
from datetime import datetime
import os

st.title("Memo")

memo_list = ['newMemo'] + os.listdir('memo/')
fn = st.selectbox('choose a memo', memo_list)

content = ''
if fn != 'newMemo':
    with open(f'memo/{fn}', 'r', encoding='utf-8') as f:
        content = f.read()
else:
    fn = './memo/'+datetime.now().strftime('%Y%m%d_%H%M%S') + '.txt'

left, right = st.columns(2, )
with left:
    st.button('save')
with right:
    st.download_button(
        label="Download",
        data = content,
        file_name=fn,
        use_container_width=True
    )

txt = st.text_area("write memo", value=content)
button = st.button("Write in a file")
if button:
    try:

        #fn = './memo/'+datetime.now().strftime('%Y%m%d_%H%M%S') + '.txt'
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(txt)
            st.success("Memo is well stored!")
    except Exception as e:
        st.error('input is not saved.', e)