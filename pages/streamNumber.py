import pandas as pd
import streamlit as st  # Import streamlit only once
import pickle
with open("dataframes.pkl", "rb") as f:
    dataframes = pickle.load(f)

def main():
    # Streamlit app definition
    st.title("Search ExcelSheets")

    # User input field
    user_input = st.text_input("Enter your Stream Number:")

    # Button to trigger script execution
    if st.button("Run Script"):
        # Find if user input exists in any sheet
        found = False
        for sheet_name, df in dataframes.items():
            if user_input in df.columns:
                found = True
                result_df = df[["Stream no.",' ', user_input]]
                result_df = pd.DataFrame(result_df.values)
                st.write(f"Sheet: {sheet_name}")
                st.dataframe(result_df, width=600)
                break  # Exit loop after finding the first match
        
        if not found:
            st.write("Stream Number not found in any sheet.")

if __name__ == '__main__':
    main()