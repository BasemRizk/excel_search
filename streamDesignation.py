import pandas as pd
import streamlit as st  # Import streamlit only once
import pickle
with open("stream.pkl", "rb") as f:
    dataframes = pickle.load(f)
with open("Unique_stream.pkl", "rb") as f:
    streams = pickle.load(f)
streams=sorted(streams)
def main():
    # Streamlit app definition
    st.title("Search ExcelSheets")

    # User input field
    #user_input = st.text_input("Enter your Stream Number:")
    user_input = st.selectbox(label='Search by stream designation:',options=streams,index=None,placeholder="Select stream")
    # Button to trigger script execution
    if st.button("Run Script"):
        # Find if user input exists in any sheet
        found = False
        for sheet_name, df in dataframes.items():
            if user_input in df.columns:
                found = True
                result_df = df[["Stream designation","", user_input]]
                result_df = pd.DataFrame(result_df.values)
                threshold = len(result_df)-2
                empty_string_counts = result_df.eq('').sum()
                columns_to_drop = empty_string_counts[empty_string_counts > threshold].index
                result_df = result_df.drop(columns=columns_to_drop)
                st.write(f"Sheet: {sheet_name}")
                st.dataframe(result_df, width=800)
                #break  # Exit loop after finding the first match
        
        if not found:
            st.write("Stream Number not found in any sheet.")

if __name__ == '__main__':
    main()