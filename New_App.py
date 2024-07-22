import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy.stats import ttest_ind

# Generate example data
np.random.seed(42)
data = {
    'Group': np.random.choice(['GroupA', 'GroupB'], size=200),
    'Value': np.random.normal(loc=10, scale=5, size=200),
    'Category': np.random.choice(['Cat1', 'Cat2', 'Cat3'], size=200)
}

df = pd.DataFrame(data)

# Title
st.title('Interactive Streamlit Dashboard with Statistical Significance')

# Sidebar for filters
st.sidebar.header('Filter Options')

# Add filters
selected_group = st.sidebar.selectbox('Select Group:', df['Group'].unique())
selected_category = st.sidebar.selectbox('Select Category:', df['Category'].unique())

# Filter data based on selections
filtered_df = df[(df['Group'] == selected_group) & (df['Category'] == selected_category)]

# Perform t-test between GroupA and GroupB
group_a = df[df['Group'] == 'GroupA']['Value']
group_b = df[df['Group'] == 'GroupB']['Value']
t_stat, p_value = ttest_ind(group_a, group_b)

# Determine significance
significance = ''
if p_value < 0.05:
    significance = '*'  # You can use more stars for lower p-values (e.g., '**' for p < 0.01)

# Plotting interactive chart
fig = px.scatter(filtered_df, x='Group', y='Value', color='Category', title='Interactive Chart')

# Add significance annotation
annotation_text = f'T-test p-value: {p_value:.3f} {significance}'
fig.add_annotation(x=0.5, y=1.1, xref='paper', yref='paper', 
                   text=annotation_text, showarrow=False, font=dict(size=12, color='red'))

# Display the chart
st.plotly_chart(fig)

# Show filtered data
st.write('Filtered Data:', filtered_df)
