import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Streamlit UI
st.title("Simple Calculator")

# Select operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# User input for numbers
num1 = st.number_input("Enter first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter second number:", value=0.0, step=0.1)

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    # Display result
    st.write(f"The result is: {result}")
