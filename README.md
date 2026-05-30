# 🌟 Genshin Impact Exploratory Data Analysis & Interactive Dashboard

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://aishtooru-exploratory-data-analysis-project.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Data Analysis](https://img.shields.io/badge/Data-EDA-86C8EA.svg)]()

An end-to-end Exploratory Data Analysis (EDA) project diving into the statistics, vision(elements), and weapons of **Genshin Impact** characters. This project aims to uncover interesting patterns from character attributes and present them through an interactive web dashboard.

## 📊 Project Overview

Raw datasets often hide fascinating stories. In this project, I performed data cleaning, handled missing values utilizing game domain knowledge, and conducted data visualization to explore the following key areas:

* **Demographics & Regions:** Analyzing the distribution of characters, their Visions, and weapon types across different regions in Teyvat.
* **Combat Attributes:** Investigating the distribution of weapon types based on Vision, as well as comparing Base ATK and Base HP distributions between 4-Star and 5-Star character rarities.
* **Character Design:** Examining the distribution of character models categorized by their Vision and respective regions.

## ✨ Key Features

* **Interactive Control Panel:** Users can dynamically filter character data based on Regions.
* **Minimalist UI/UX:** Data visualizations (Bar Charts, Heatmaps, Boxplots) are designed using a clean, monochromatic blue and white palette to provide a modern and uncluttered data-reading experience.
* **Automated Data Cleaning:** Integrated data cleaning logic that properly handles missing values for game-specific mechanics (e.g., *Arkhe* alignments or *Special Dishes*).

## 🛠️ Tech Stack

* **Data Manipulation:** `pandas`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Web Deployment:** `streamlit`

## 🚀 How to Run Locally

If you want to run this dashboard on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aishtooru/Exploratory-Data-Analysis-Project.git

2. **Navigate to the project directory:**
   ```bash
   cd Exploratory-Data-Analysis-Project

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

## 📂 Project Structure
```text
├── app.py             # Main application code for the Streamlit dashboard     
├── genshin_data.csv   # Raw dataset used for analysis    
├── requirements.txt   # List of required Python libraries
└── README.md          # Project documentation   
