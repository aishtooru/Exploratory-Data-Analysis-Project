import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

st.set_page_config(
    page_title="Genshin Impact Exploratory Data Analysis Dashboard",
    page_icon='📊',
    layout='wide'
)

# Load Data and Data Cleaning
@st.cache_data
def load_data():
    df = pd.read_csv('genshin_characters.csv')

    df['arkhe'] = df['arkhe'].fillna('None')
    df['special_dish'] = df['special_dish'].fillna('No Dish')
    category_col = ['region', 'limited', 'affiliation', 'ascension_boss_material']

    for col in category_col:
        df[col] = df[col].fillna('Unknown')
    
    return df

df = load_data()

region_palettes = ["#D7C8C9", "#EFD77B", "#6B8A79", "#DFA9A1", "#A9CBB7", "#F2B5D4", "#B3E5FC"]
vision_palettes= ["#EFD77B", "#5B7E3C", "#a0d7e4", "#D51C39", "#567bd2", "#b08fc2", "#75c2aa" ]
weapon_palettes = ["#88AD6F", "#9B177E", "#2A1458", "#EFAF1B", "#5C9EAD"]
sns.set_theme(style="whitegrid")
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['figure.facecolor'] = 'white'

# Sidebar for filters
st.sidebar.header("Filter Characters")
st.sidebar.markdown("Use the filters below to explore the Genshin Impact characters dashboard.")

list_region = df['region'].unique().tolist()
selected_regions = st.sidebar.multiselect(
    "Select Region(s):",
    options=list_region,
    default=list_region
)

# Filter the DataFrame based on selected regions
df_filtered = df[df['region'].isin(selected_regions)]

# Main Dashboard
st.title("Genshin Impact Exploratory Data Analytics Dashboard")
st.markdown("---")

# Metrics
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric(label="Total Characters", value=len(df_filtered))
with col_m2:
    st.metric(label="Selected Regions", value=len(selected_regions))
with col_m3:
    st.metric(label="Vision Types", value=df_filtered['vision'].nunique() if 'vision' in df_filtered.columns else 7)
with col_m4:
    st.metric(label="Weapon Types", value=df_filtered['weapon_type'].nunique() if 'weapon_type' in df_filtered.columns else 7)
# Visualizations
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    st.subheader("Character Distribution by Region")
    if not df_filtered.empty:
        fig, ax = plt.subplots(figsize=(8,5))
        sns.countplot(
            data=df_filtered,
            y='region',
            order=df_filtered['region'].value_counts().index,
            palette=sns.color_palette(region_palettes),
            hue='region',
            legend=False,
            ax=ax
        )

        for p in ax.patches:
            width = p.get_width()
            if width > 0:
                ax.text(width + 0.2, p.get_y() + p.get_height()/2. + 0.1, '{:1.0f}'.format(width), ha="center")
        
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlabel("Number of Characters")
        plt.ylabel("Region")
        st.pyplot(fig)

    else:
        st.warning("No characters found for the selected regions. Please adjust your filters.")

with col_graph2:
    st.subheader("Character Distribution by Vision")
    if not df_filtered.empty:
        fig, ax = plt.subplots(figsize=(8,5))

        vision_col = 'vision' if  'vision' in df_filtered.columns else 'Unknown'

        sns.countplot(
            data=df_filtered,
            x='region',
            hue=vision_col,
            palette=sns.color_palette(vision_palettes),
            order=df_filtered['region'].value_counts().index,
            ax=ax
        )
        plt.xlabel("Region")
        plt.ylabel("Number of Characters")
        plt.legend(title="Vision", loc='upper right')
        st.pyplot(fig)
    else:
        st.warning("No characters found for the selected regions. Please adjust your filters.")

st.markdown("---")
col_graph3, col_graph4 = st.columns(2)
with col_graph3:
    st.subheader("Weapon Type Distribution by Vision")
    fig2, ax2 = plt.subplots(figsize=(8,5))
    if not df_filtered.empty:
        sns.countplot(
                data=df_filtered,
                x='vision',
                hue='weapon_type',
                palette=sns.color_palette(weapon_palettes),
                order=df_filtered['vision'].value_counts().index,
                ax=ax2
            )
        plt.xlabel("Vision")
        plt.ylabel("Number of Characters")
        plt.legend(title="Weapon Type",  loc='upper right', bbox_to_anchor=(1.05, 1.1))
        st.pyplot(fig2)
    else:
        st.warning("No weapon types found for the selected vision. Please adjust your filters.")

with col_graph4:
    st.subheader("Weapon Type Distribution by Region")
    fig2, ax2 = plt.subplots(figsize=(8,5))
    if not df_filtered.empty:
        sns.countplot(
                data=df_filtered,
                x='region',
                hue='weapon_type',
                palette=sns.color_palette(weapon_palettes),
                order=df_filtered['region'].value_counts().index,
                ax=ax2
            )
        plt.xlabel("Region")
        plt.ylabel("Number of Characters")
        plt.legend(title="Weapon Type", loc='upper right', bbox_to_anchor=(1.05, 1.1))
        st.pyplot(fig2)
    else:
        st.warning("No weapon types found for the selected region. Please adjust your filters.")

st.markdown("---")
col_graph5, col_graph6 = st.columns(2)
with col_graph5:
    st.subheader("Base ATK Distribution by Star Rarity")
    fig3, ax3 = plt.subplots(figsize=(8,5))
    if not df_filtered.empty:
        sns.boxplot(
        data=df_filtered,
        x='star_rarity',
        y='atk_90_90',
        palette=sns.color_palette('pastel'),
        ax=ax3
        )
        plt.xlabel("Star Rarity")
        plt.ylabel("Base ATK at Level 90")

        sns.stripplot(
            data=df_filtered,
            x='star_rarity',
            y='atk_90_90',
            color='black',
            alpha=0.5,
            jitter=True,
            ax=ax3
        )
        st.pyplot(fig3)
    else:
        st.warning("No characters found.")

with col_graph6:
    st.subheader("Base HP  Distribution by Star Rarity")
    fig3, ax3 = plt.subplots(figsize=(8,5))
    if not df_filtered.empty:
        sns.boxplot(
        data=df_filtered,
        x='star_rarity',
        y='hp_90_90',
        palette=sns.color_palette('pastel'),
        ax=ax3
        )
        plt.xlabel("Star Rarity")
        plt.ylabel("Base HP at Level 90")

        sns.stripplot(
            data=df_filtered,
            x='star_rarity',
            y='hp_90_90',
            color='black',
            alpha=0.5,
            jitter=True,
            ax=ax3
        )
        st.pyplot(fig3)
    else:
        st.warning("No characters found.")


st.markdown("---")
col_graph7, col_graph8 = st.columns(2)
with col_graph7:
    st.subheader("Model Characters by Region")
    fig4, ax4 = plt.subplots(figsize=(8,5))
    if not df_filtered.empty:
        sns.countplot(
        data=df_filtered,
        x='region',
        palette=sns.color_palette('pastel'),
        hue='model',
        ax=ax4
        )
        plt.xlabel("Region")
        plt.ylabel("Number of Characters")
        plt.legend(title='Model', bbox_to_anchor=(1.05, 1), loc='upper left')

        st.pyplot(fig4)
    else:
        st.warning("No characters found.")

with col_graph8:
    st.subheader("Model Characters by Vision")
    fig4, ax4 = plt.subplots(figsize=(8,5))
    if not df_filtered.empty:
        sns.countplot(
        data=df_filtered,
        x='vision',
        palette=sns.color_palette(vision_palettes),
        hue='model',
        ax=ax4
        )
        plt.xlabel("Vision")
        plt.ylabel("Number of Characters")
        plt.legend(title='Model', bbox_to_anchor=(1.05, 1), loc='upper left')

        st.pyplot(fig4)
    else:
        st.warning("No characters found.")


st.markdown("---")
with st.expander("View Raw Data"):
    st.dataframe(df_filtered, use_container_width=True)