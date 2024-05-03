{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPo7FNY1iDIeMxiOktGm6gJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aipelsi/ElsaH/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pandas==1.3.5 numpy==1.23.5 scikit-learn==0.24.2 tensorflow==2.6.0 streamlit==1.11.0 gdown==4.4.0\n",
        "import streamlit as st\n",
        "from tensorflow.keras.models import load_model\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "import pandas as pd\n",
        "import gdown\n",
        "\n",
        "# Function to download and load the model\n",
        "@st.cache(allow_output_mutation=True)\n",
        "def load_my_model():\n",
        "    url = 'https://drive.google.com/uc?id=1VPaz8JOudnGOwJw-IjhRYYSmk7SnHtDB'\n",
        "    output = 'my_model.h5'\n",
        "    gdown.download(url, output, quiet=False)\n",
        "    model = load_model(output)\n",
        "    return model\n",
        "\n",
        "model = load_my_model()\n",
        "\n",
        "# Function to preprocess input\n",
        "def preprocess(data):\n",
        "    df = pd.DataFrame([data])\n",
        "    scaler = StandardScaler()\n",
        "    scaled_df = scaler.fit_transform(df)\n",
        "    return scaled_df\n",
        "\n",
        "# Custom CSS to style the app\n",
        "st.markdown(\n",
        "    \"\"\"\n",
        "    <style>\n",
        "    .reportview-container {\n",
        "        background: url(\"https://source.unsplash.com/weekly?water\");  # Example background image\n",
        "        background-size: cover;\n",
        "    }\n",
        "    .big-font {\n",
        "        font-size:28px !important;\n",
        "        font-weight: bold;\n",
        "    }\n",
        "    </style>\n",
        "    \"\"\", unsafe_allow_html=True)\n",
        "\n",
        "st.markdown('<p class=\"big-font\">Loan Repayment Prediction App</p>', unsafe_allow_html=True)\n",
        "\n",
        "# Input Section\n",
        "with st.form(\"my_form\"):\n",
        "    st.write(\"## Enter Loan Details\")\n",
        "\n",
        "    col1, col2 = st.columns(2)\n",
        "    with col1:\n",
        "        payroll_proceed = st.number_input('Payroll Proceed', min_value=0.0, max_value=1000000.0, value=5000.0, step=100.0)\n",
        "        jobs_reported = st.number_input('Number of Employees (Jobs Reported)', min_value=0, max_value=1000, value=10, step=1)\n",
        "    with col2:\n",
        "        nonprofit = st.selectbox('NonProfit Status', ['Yes', 'No'])\n",
        "\n",
        "    submitted = st.form_submit_button(\"Predict\")\n",
        "    if submitted:\n",
        "        input_data = {\n",
        "            'PAYROLL_PROCEED': payroll_proceed,\n",
        "            'JobsReported': jobs_reported,\n",
        "            'NonProfit': 1 if nonprofit == 'Yes' else 0\n",
        "        }\n",
        "\n",
        "        processed_data = preprocess(input_data)\n",
        "        prediction = model.predict(processed_data)\n",
        "        if prediction[0][0] > 0.5:\n",
        "            st.success('The loan is likely to be paid back.')\n",
        "        else:\n",
        "            st.error('There is a high risk the loan will not be paid back.')\n"
      ],
      "metadata": {
        "id": "_N-FY0vtRLAK"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}