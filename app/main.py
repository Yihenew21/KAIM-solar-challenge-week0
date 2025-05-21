import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
from scipy.stats import f_oneway, kruskal

st.set_page_config(page_title="Solar Cross-Country Dashboard", layout="centered")

st.image("app/static/logo.png", width=120)

@st.cache_data
def load_data():
    benin = pd.read_csv('data/benin_clean.csv')
    sierra = pd.read_csv('data/sierraleone_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    return pd.concat([benin, sierra, togo], ignore_index=True)

df = load_data()

st.title("Cross-Country Solar Potential Dashboard")
st.markdown("""
Compare solar metrics (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo.\
Select countries and metrics to explore differences in solar potential.
""")

# Sidebar widgets for country and metric selection
with st.sidebar:
    st.header("Filters")
    countries = st.multiselect(
        "Select countries:",
        options=df['Country'].unique(),
        default=list(df['Country'].unique())
    )
    metric = st.selectbox(
        "Select metric:",
        options=['GHI', 'DNI', 'DHI'],
        index=0
    )

filtered = df[df['Country'].isin(countries)]

# Boxplot
st.subheader(f"Boxplot of {metric} by Country")
fig, ax = plt.subplots()
sns.boxplot(x='Country', y=metric, hue='Country', data=filtered, palette='Set2', legend=False)
ax.set_xlabel('Country')
ax.set_ylabel(metric)
st.pyplot(fig)

# Summary Table
st.subheader(f"Summary Table for {metric}")
sumtab = filtered.groupby('Country')[metric].agg(['mean', 'median', 'std']).round(2)
st.dataframe(sumtab)

# Visual Summary: Bar chart of average GHI
st.subheader("Average GHI by Country")
avg_ghi = filtered.groupby('Country')['GHI'].mean().sort_values(ascending=False)
st.bar_chart(avg_ghi)

if len(countries) > 1:
    ghi_groups = [filtered[filtered['Country'] == c]['GHI'].dropna() for c in countries]
    anova_stat, anova_p = f_oneway(*ghi_groups)
    kruskal_stat, kruskal_p = kruskal(*ghi_groups)
    st.info(f"**ANOVA p-value:** {anova_p:.4g} | **Kruskal–Wallis p-value:** {kruskal_p:.4g}")

if 'Region' in filtered.columns:
    st.subheader("Top Regions by Average GHI")
    top_regions = filtered.groupby(['Country', 'Region'])['GHI'].mean().reset_index()
    top_regions = top_regions.sort_values('GHI', ascending=False).head(10)
    st.dataframe(top_regions)

st.subheader(f"Histogram of {metric}")
fig2, ax2 = plt.subplots()
for country in countries:
    sns.histplot(filtered[filtered['Country'] == country][metric], label=country, kde=True, ax=ax2, element='step', stat='density')
ax2.legend()
st.pyplot(fig2)

csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name='filtered_solar_data.csv',
    mime='text/csv'
)

st.markdown("---")
st.markdown("""
**How to use:**
- Use the sidebar to select countries and the metric to compare.
- The boxplot and summary table update automatically.
- The bar chart always shows average GHI for the selected countries.
""")

st.markdown("""
---
### Key Observations
- Benin shows the highest median GHI, but also the greatest variability.
- Sierra Leone has the lowest average GHI among the three countries.
- The ANOVA/Kruskal–Wallis p-values indicate that differences in GHI between countries are statistically significant (p < 0.05).
""") 