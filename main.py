import streamlit as st

# Calculator functions
def add(x, y, z, w):
    return x + y + z + w

def subtract(x, y, z, w):
    return x - y - z - w

def multiply(x, y, z, w):
    return x * y * z * w

def divide(x, y, z, w):
    if y == 0 or z == 0 or w == 0:
        return "Error: Division by zero is not allowed."
    return x / y / z / w

# Streamlit UI
st.title("Simple Calculator (Four Numbers)")

# Select operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# User input for numbers
num1 = st.number_input("Enter first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter second number:", value=0.0, step=0.1)
num3 = st.number_input("Enter third number:", value=0.0, step=0.1)
num4 = st.number_input("Enter fourth number:", value=0.0, step=0.1)

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2, num3, num4)
    elif operation == "Subtract":
        result = subtract(num1, num2, num3, num4)
    elif operation == "Multiply":
        result = multiply(num1, num2, num3, num4)
    elif operation == "Divide":
        result = divide(num1, num2, num3, num4)
    
    # Display result
    st.write(f"The result is: {result}")
