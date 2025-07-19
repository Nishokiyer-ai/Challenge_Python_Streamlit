import streamlit as st

st.title('Simple Calculator')

num1 = st.number_input('Enter first number:', value=0.0, format="%f")
num2 = st.number_input('Enter second number:', value=0.0, format="%f")
operation = st.selectbox('Select operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

if st.button('Calculate'):
    if operation == 'Add':
        result = num1 + num2
        st.success(f'Result: {num1} + {num2} = {result}')
    elif operation == 'Subtract':
        result = num1 - num2
        st.success(f'Result: {num1} - {num2} = {result}')
    elif operation == 'Multiply':
        result = num1 * num2
        st.success(f'Result: {num1} × {num2} = {result}')
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
            st.success(f'Result: {num1} ÷ {num2} = {result}')
        else:
            st.error('Error: Division by zero is not allowed.')
