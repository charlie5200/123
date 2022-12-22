import streamlit as st
st.title("2022年最新發票對獎程式")
st.image("最新發票號碼.jpg")
num=st.text_input('輸入您的發票號碼')
ns = '11174120'
n1 = '59276913'                        
n2 = ['18079936','20591738','64500205']
n3 = ['ns','n1','n2']
if num == ns: st.write("對中 1000 萬元！")
if num == ns: st.image("恭喜中獎.jpg")
if num == n1: st.write("對中 200 萬元！")
if num == n1: st.image("恭喜中獎.jpg")

for i in n2:

    if num == i:
        st.write("對中 20 萬元！") 
        st.image("恭喜中獎.jpg")
        break
    elif num[-7:] == i[-7:]:
        st.write("對中 4 萬元！") 
        st.image("恭喜中獎.jpg")
        break
    elif num[-6:] == i[-6:]:
        st.write("對中 1 萬元！") 
        st.image("恭喜中獎.jpg")
        break
    elif num[-5:] == i[-5:]:
        st.write("對中 4000 元")  
        st.image("恭喜中獎.jpg")
        break
    elif num[-4:] == i[-4:]:
        st.write("對中 1000 元！")  
        st.image("恭喜中獎.jpg")
        break
    elif num[-3:] == i[-3:]:
        st.write("對中 200 元！")  
        st.image("恭喜中獎.jpg")
        break
    elif num[-2:] == i[-2:]:
        st.write("再接再厲")
        break
    elif num[-1:] == i[-1:]:
        st.write("再接再厲")
        break
    elif num[-0:] == i[-0:]:
        st.write("再接再厲")
        break
if num[-6:] == ns[-6:]:
    st.write("幸運之神與你擦肩而過")
