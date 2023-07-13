import streamlit as st

st.header("Day 2: 会用st.write")

st.write("st.write")

st.header("Day 3: 会用st.header 和 button")

st.header('st.header')

if st.button('按键上的字'):
     st.write('点击后显示')
else:
     st.write('没点击显示')
        
        
import numpy as np
import altair as alt
import pandas as pd

st.header("Day 5: 各类write输出格式")
# 样例 1

st.write('Hello, *World!* :sunglasses:')

# 样例 2

st.write(1234)

# 样例 3

df = pd.DataFrame({
     '第一列': [1, 2, 3, 4],
     '第二列': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

# 生成两百个 在±3范围的数据，a,b,c三列数据都存在
df2 = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")


st.caption('一般用于解释上述文本.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


code = '''
# 代码形式
def hello():
    print("Hello, Streamlit!")
    '''
st.code(code, language='python')


st.text('text 直接输出',help = "st.text")


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''',help = "数学公式 st.latex")

st.write("密码隐私:", st.secrets["password"])
