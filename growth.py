import streamlit as st
import pandas as pd
import os
from io import BytestIO


st.set_page_config(page_title= "Data Sweeper",layout='wide')

#Custom Css
st.markdown(
    """
    <style>
    .stApp{
         background-color: black;
        color: whitw;
        }</style>
    
    
    """,

    unsafe_allow_html=True

)
#title and description
st.title("☢ DataSweeper Sterling Integrator By Shabina Naz")
st.write("Tranform Your Files between CSV and Excel formats with built-in data cleaning and visualization creating the project for quarter 3❤")

#file uploader
uploaded_files = st.file_uploader("upload your files (accepts CSV or Excel):", type=["CVS","XLSX"], accept_multiple_files=(True))

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lowes()

        if file_ext == ".csv":
            df = pd.read_csv(fike)
        elif file_ext == "xlsx":
            df = pd.read_excel(file)

        else:
            st.error(f"unsupported file type: {file_ext}")
            continue

        #file details
        st.write("⚛ Preview the head of the Dataframe")
        st.dataframe(df.head())


        #data cleaning options
        st.subheader("🕳 Data Cleaning Options")
        if st.checkbox(f"clean data for {file.name}"):
            col1, col2 = st.colums(2)
            
            with col1:
                if st.button(f"Reamove duplicates from the file : {file.name}"):
                    df.drop_duplictaes(inplace=True)
                    st.write("✅uploaded_files")

            with col2:
                if st.button(f"fill missing values for {file.name}"):
                   numeric_cols = df.select_dtypes(includes=['number']).colums
                   df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                   st.write("💟 Missing values have been filled!")




        st.subheader("select colums to keep")

        colums = st.multiselect(f"choose colums for {file.name}", df.colums, defult=df.colums)
        df =df[colums]



        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, "2"])

        st.subheader("Conversion Option") 
        conversion_type = st.radio(f"Convert{file.name} to:", ["CVS", "Excel"], key=file.name)   
        if st.button(f"Convert{file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to.csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".scv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(
                 label=f"Download {file.name} as {conversion_type}",
                 data=buffer,
                 file_name=file_name,
                 mime=mime_type

            )
st.success("✔ All files Processed Successfully!")

          





