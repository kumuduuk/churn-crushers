import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(
    page_title="Bank Customer Churn Analysis",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and prepare data
@st.cache_data # Cache the data loading function to improve performance
def load_data():
    df = pd.read_csv('data/cleaned_data/bankchurners.csv')
    # Create churn binary column
    df['churn'] = df['customer_status'].apply(lambda x: 1 if x == 'Attrited Customer' else 0)
    return df

df = load_data()

# Sidebar for filters
st.sidebar.title("🔍 Filter Options")

# Demographic filters
st.sidebar.subheader("Demographic Filters")
age_range = st.sidebar.slider(
    "Age Range",
    min_value=int(df['age'].min()),
    max_value=int(df['age'].max()),
    value=(int(df['age'].min()), int(df['age'].max()))
)

income_filter = st.sidebar.multiselect(
    "Income Category",
    options=df['income_category'].unique(),
    default=df['income_category'].unique()
)

marital_filter = st.sidebar.multiselect(
    "Marital Status",
    options=df['marital_status'].unique(),
    default=df['marital_status'].unique()
)

# Behavioral filters
st.sidebar.subheader("Behavioral Filters")
utilization_filter = st.sidebar.multiselect(
    "Utilization Category",
    options=df['utilization_cat'].unique(),
    default=df['utilization_cat'].unique()
)

card_filter = st.sidebar.multiselect(
    "Card Category",
    options=df['card_category'].unique(),
    default=df['card_category'].unique()
)

# Apply filters
filtered_df = df[
    (df['age'].between(age_range[0], age_range[1])) &
    (df['income_category'].isin(income_filter)) &
    (df['marital_status'].isin(marital_filter)) &
    (df['utilization_cat'].isin(utilization_filter)) &
    (df['card_category'].isin(card_filter))
]

# Main dashboard
st.title("🏦 Bank Customer Churn Analysis Dashboard")
st.markdown("---")

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_customers = len(filtered_df)
    st.metric("Total Customers", total_customers)

with col2:
    churn_rate = filtered_df['churn'].mean() * 100
    st.metric("Churn Rate", f"{churn_rate:.1f}%")

with col3:
    avg_age = filtered_df['age'].mean()
    st.metric("Average Age", f"{avg_age:.1f} years")

with col4:
    avg_utilization = filtered_df['avg_utilization_ratio'].mean() * 100
    st.metric("Avg Utilization", f"{avg_utilization:.1f}%")

st.markdown("---")

# Descriptive Statistics Section
st.header("📊 Descriptive Statistics")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Churn Overview", "Demographic Analysis", "Behavioral Patterns", "Churn Calculator", "PowerBI Dashboard"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        # Churn by Income
        churn_income = filtered_df.groupby('income_category')['churn'].mean().reset_index()
        fig_income = px.bar(
            churn_income,
            x='income_category',
            y='churn',
            title='Churn Rate by Income Category',
            color='churn',
            color_continuous_scale='RdYlGn_r'
        )
        fig_income.update_layout(xaxis_title='Income Category', yaxis_title='Churn Rate')
        st.plotly_chart(fig_income, use_container_width=True)
    
    with col2:
        # Churn by Age Bracket
        churn_age = filtered_df.groupby('age_bracket')['churn'].mean().reset_index()
        fig_age = px.bar(
            churn_age,
            x='age_bracket',
            y='churn',
            title='Churn Rate by Age Bracket',
            color='churn',
            color_continuous_scale='RdYlGn_r'
        )
        fig_age.update_layout(xaxis_title='Age Bracket', yaxis_title='Churn Rate')
        st.plotly_chart(fig_age, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        # Churn by Education
        churn_edu = filtered_df.groupby('education_level')['churn'].mean().reset_index()
        fig_edu = px.bar(
            churn_edu,
            x='education_level',
            y='churn',
            title='Churn Rate by Education Level',
            color='churn',
            color_continuous_scale='RdYlGn_r'
        )
        fig_edu.update_layout(xaxis_title='Education Level', yaxis_title='Churn Rate')
        st.plotly_chart(fig_edu, use_container_width=True)
    
    with col2:
        # Churn by Marital Status
        churn_marital = filtered_df.groupby('marital_status')['churn'].mean().reset_index()
        fig_marital = px.bar(
            churn_marital,
            x='marital_status',
            y='churn',
            title='Churn Rate by Marital Status',
            color='churn',
            color_continuous_scale='RdYlGn_r'
        )
        fig_marital.update_layout(xaxis_title='Marital Status', yaxis_title='Churn Rate')
        st.plotly_chart(fig_marital, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        # Utilization vs Churn
        fig_util = px.box(
            filtered_df,
            x='churn',
            y='avg_utilization_ratio',
            color='churn',
            title='Utilization Ratio vs Churn Status'
        )
        st.plotly_chart(fig_util, use_container_width=True)
    
    with col2:
        # Months Inactive vs Churn
        fig_inactive = px.box(
            filtered_df,
            x='churn',
            y='months_inactive_12_mon',
            color='churn',
            title='Months Inactive vs Churn Status'
        )
        st.plotly_chart(fig_inactive, use_container_width=True)
    
    # Additional behavioral charts
    col3, col4 = st.columns(2)
    
    with col3:
        # Transaction count vs Churn
        fig_trans = px.box(
            filtered_df,
            x='churn',
            y='total_trans_ct',
            color='churn',
            title='Transaction Count vs Churn Status'
        )
        st.plotly_chart(fig_trans, use_container_width=True)
    
    with col4:
        # Number of products vs Churn
        fig_products = px.box(
            filtered_df,
            x='churn',
            y='no_of_products',
            color='churn',
            title='Number of Products vs Churn Status'
        )
        st.plotly_chart(fig_products, use_container_width=True)

with tab4:
    st.subheader("🏦 Bank Customer Churn Analyzer")
    st.markdown("Adjust the sliders to filter customers and see the churn percentage for that segment.")
    
    # Display dataset info
    total_customers = len(df)
    total_churned = df['churn'].sum()
    overall_churn_rate = (total_churned / total_customers) * 100
    
    st.sidebar.header("📊 Dataset Overview")
    st.sidebar.metric("Total Customers", f"{total_customers:,}")
    st.sidebar.metric("Churned Customers", f"{total_churned:,}")
    st.sidebar.metric("Overall Churn Rate", f"{overall_churn_rate:.1f}%")
    
    # Get min and max values for sliders
    utilization_min, utilization_max = 0.0, 1.0
    months_inactive_min, months_inactive_max = df['months_inactive_12_mon'].min(), df['months_inactive_12_mon'].max()
    contacts_min, contacts_max = df['contacts_count_12_mon'].min(), df['contacts_count_12_mon'].max()
    products_min, products_max = df['no_of_products'].min(), df['no_of_products'].max()
    trans_count_min, trans_count_max = df['total_trans_ct'].min(), df['total_trans_ct'].max()
    trans_amt_min, trans_amt_max = df['total_trans_amt'].min(), df['total_trans_amt'].max()
    age_min, age_max = df['age'].min(), df['age'].max()
    credit_min, credit_max = df['credit_limit'].min(), df['credit_limit'].max()
    
    st.subheader("🔧 Filter Customers")
    
    # Create two columns for sliders
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Usage Patterns**")
        
        utilization_range = st.slider(
            "Average Utilization Ratio",
            min_value=float(utilization_min),
            max_value=float(utilization_max),
            value=(0.0, 1.0),
            step=0.01,
            help="Filter by credit utilization ratio"
        )
        
        months_inactive_range = st.slider(
            "Months Inactive (12 months)",
            min_value=int(months_inactive_min),
            max_value=int(months_inactive_max),
            value=(int(months_inactive_min), int(months_inactive_max)),
            step=1,
            help="Filter by number of inactive months"
        )
        
        contacts_range = st.slider(
            "Contacts Count (12 months)",
            min_value=int(contacts_min),
            max_value=int(contacts_max),
            value=(int(contacts_min), int(contacts_max)),
            step=1,
            help="Filter by number of bank contacts"
        )
        
        products_range = st.slider(
            "Number of Products",
            min_value=int(products_min),
            max_value=int(products_max),
            value=(int(products_min), int(products_max)),
            step=1,
            help="Filter by number of bank products used"
        )
    
    with col2:
        st.write("**Transaction & Demographic**")
        
        trans_count_range = st.slider(
            "Transaction Count",
            min_value=int(trans_count_min),
            max_value=int(trans_count_max),
            value=(int(trans_count_min), int(trans_count_max)),
            step=1,
            help="Filter by total number of transactions"
        )
        
        trans_amt_range = st.slider(
            "Total Transaction Amount ($)",
            min_value=int(trans_amt_min),
            max_value=int(trans_amt_max),
            value=(int(trans_amt_min), int(trans_amt_max)),
            step=100,
            help="Filter by total transaction amount"
        )
        
        age_range = st.slider(
            "Age",
            min_value=int(age_min),
            max_value=int(age_max),
            value=(int(age_min), int(age_max)),
            step=1,
            help="Filter by customer age"
        )
        
        credit_range = st.slider(
            "Credit Limit ($)",
            min_value=int(credit_min),
            max_value=int(credit_max),
            value=(int(credit_min), int(credit_max)),
            step=500,
            help="Filter by credit limit"
        )
        
        gender_filter = st.selectbox(
            "Gender",
            options=["All", "Male", "Female"],
            index=0,
            help="Filter by gender"
        )
    
    # Calculate button
    if st.button("📊 Calculate Churn Percentage", type="primary", use_container_width=True):
        
        # Apply filters
        filtered_df = df.copy()
        
        # Apply range filters
        filters = {
            'avg_utilization_ratio': utilization_range,
            'months_inactive_12_mon': months_inactive_range,
            'contacts_count_12_mon': contacts_range,
            'no_of_products': products_range,
            'total_trans_ct': trans_count_range,
            'total_trans_amt': trans_amt_range,
            'age': age_range,
            'credit_limit': credit_range
        }
        
        for column, (min_val, max_val) in filters.items():
            filtered_df = filtered_df[
                (filtered_df[column] >= min_val) & 
                (filtered_df[column] <= max_val)
            ]
        
        # Apply gender filter
        if gender_filter != "All":
            # Assuming gender is stored as 'M' and 'F' in your dataframe
            gender_map = {"Male": "M", "Female": "F"}
            filtered_df = filtered_df[filtered_df['gender'] == gender_map[gender_filter]]
        
        # Calculate results
        segment_size = len(filtered_df)
        
        if segment_size > 0:
            churn_count = filtered_df['churn'].sum()
            churn_percentage = (churn_count / segment_size) * 100
            
            # Display results
            st.subheader("📈 Results")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Segment Size",
                    f"{segment_size:,}",
                    f"{((segment_size/total_customers)*100):.1f}% of total"
                )
            
            with col2:
                st.metric(
                    "Churn Count",
                    f"{churn_count:,}"
                )
            
            with col3:
                st.metric(
                    "Churn Percentage",
                    f"{churn_percentage:.1f}%",
                    f"{churn_percentage - overall_churn_rate:+.1f}% vs overall"
                )
            
            # Risk assessment
            st.subheader("🎯 Risk Assessment")
            if churn_percentage < overall_churn_rate - 5:
                st.success(f"✅ Below Average Risk ({(overall_churn_rate - churn_percentage):.1f}% lower than overall average)")
            elif churn_percentage > overall_churn_rate + 5:
                st.error(f"🔴 Above Average Risk ({(churn_percentage - overall_churn_rate):.1f}% higher than overall average)")
            else:
                st.warning(f"⚠️ Average Risk (Close to overall average of {overall_churn_rate:.1f}%)")
            
            # Show filter summary
            with st.expander("🔍 View Filter Summary"):
                st.write("**Applied Filters:**")
                for column, (min_val, max_val) in filters.items():
                    st.write(f"- {column.replace('_', ' ').title()}: {min_val} to {max_val}")
                if gender_filter != "All":
                    st.write(f"- Gender: {gender_filter}")
                
                st.write(f"\n**Segment represents {segment_size/total_customers*100:.1f}% of total customers**")
        
        else:
            st.warning("⚠️ No customers match the selected filters. Please adjust your criteria.")
    
    # Add some insights
    with st.expander("💡 How to interpret results"):
        st.markdown("""
        **Understanding Churn Percentage:**
        - This shows the percentage of customers who churned **within your selected filters**
        - Compare against the overall churn rate to see if your segment is higher/lower risk
        
        **Common Patterns to Explore:**
        - High utilization + low transactions = Higher risk
        - Many inactive months = Higher risk  
        - Few products + high contacts = Higher risk
        - Low credit limit + high utilization = Higher risk
        
        **Usage Tips:**
        - Start with broad ranges to see baseline churn
        - Narrow down ranges to identify high-risk segments
        - Compare different combinations to find patterns
        """)

with tab5:
    st.subheader("📊 PowerBI Dashboard Integration")

    # PowerBI embed code
    powerbi_embed_code = """
    <iframe title="Churn Crushers Dashboard" width="1140" height="541.25" 
            src="https://app.powerbi.com/reportEmbed?reportId=1f2680f0-7338-4a9a-94a9-a752d4578ec1&autoAuth=true&ctid=c233c072-135b-431d-af59-35e05babf941" 
            frameborder="0" allowFullScreen="true"></iframe>
    """

    # Display the PowerBI dashboard
    components.html(powerbi_embed_code, height=600, scrolling=True)


# Segmentation Analysis
st.header("🎯 Customer Segmentation")

col1, col2 = st.columns(2)

with col1:
    # Create risk segments based on multiple factors
    conditions = [
        # High risk conditions
        (filtered_df['avg_utilization_ratio'] > 0.7) | 
        (filtered_df['months_inactive_12_mon'] > 2) |
        (filtered_df['no_of_products'] < 2) |
        (filtered_df['total_trans_ct'] < 20),
        
        # Low risk conditions  
        (filtered_df['avg_utilization_ratio'] < 0.3) & 
        (filtered_df['months_inactive_12_mon'] < 2) &
        (filtered_df['no_of_products'] > 2) &
        (filtered_df['total_trans_ct'] > 40)
    ]
    
    choices = ['High', 'Low']
    filtered_df['risk_segment'] = np.select(conditions, choices, default='Medium')
    
    segment_counts = filtered_df['risk_segment'].value_counts()
    fig_segment = px.pie(
        values=segment_counts.values,
        names=segment_counts.index,
        title='Customer Risk Segmentation Distribution'
    )
    st.plotly_chart(fig_segment, use_container_width=True)

with col2:
    # Segment churn rates
    segment_churn = filtered_df.groupby('risk_segment')['churn'].mean().reset_index()
    fig_segment_churn = px.bar(
        segment_churn,
        x='risk_segment',
        y='churn',
        title='Churn Rate by Risk Segment',
        color='churn',
        color_continuous_scale='RdYlGn_r'
    )
    fig_segment_churn.update_layout(yaxis_title='Churn Rate', xaxis_title='Risk Segment')
    st.plotly_chart(fig_segment_churn, use_container_width=True)

# Additional segmentation insights
st.subheader("Segmentation Insights")
segmentation_col1, segmentation_col2, segmentation_col3 = st.columns(3)

with segmentation_col1:
    high_risk_count = len(filtered_df[filtered_df['risk_segment'] == 'High'])
    st.metric("High Risk Customers", high_risk_count)

with segmentation_col2:
    medium_risk_count = len(filtered_df[filtered_df['risk_segment'] == 'Medium'])
    st.metric("Medium Risk Customers", medium_risk_count)

with segmentation_col3:
    low_risk_count = len(filtered_df[filtered_df['risk_segment'] == 'Low'])
    st.metric("Low Risk Customers", low_risk_count)

# Retention Strategies
st.header("💡 Data-Driven Retention Strategies")

strategy_tab1, strategy_tab2, strategy_tab3 = st.tabs(["High Risk", "Medium Risk", "Low Risk"])

with strategy_tab1:
    st.subheader("🔴 High Risk Customers - Immediate Intervention")
    st.markdown("""
    **Characteristics:**
    - High credit utilization (>70%)
    - Extended account inactivity (>2 months) 
    - Limited product engagement (≤2 products)
    - Low transaction frequency
    
    **Retention Strategies:**
    - **Immediate proactive outreach** by dedicated relationship managers
    - **Personalized retention offers**: Fee waivers, rate reductions
    - **Product bundle recommendations**: Cross-sell additional services
    - **Credit limit increase considerations** for qualified customers
    - **Loyalty program enrollment** with immediate benefits
    - **Financial wellness programs** and counseling
    """)
    
    # High risk statistics
    high_risk_df = filtered_df[filtered_df['risk_segment'] == 'High']
    if not high_risk_df.empty:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("High Risk Churn Rate", f"{high_risk_df['churn'].mean()*100:.1f}%")
        with col2:
            st.metric("Avg Utilization", f"{high_risk_df['avg_utilization_ratio'].mean()*100:.1f}%")
        with col3:
            st.metric("Avg Products", f"{high_risk_df['no_of_products'].mean():.1f}")

with strategy_tab2:
    st.subheader("🟡 Medium Risk Customers - Preventive Care")
    st.markdown("""
    **Characteristics:**
    - Moderate utilization and activity levels
    - Some product engagement but room for growth
    - Occasional periods of lower activity
    
    **Retention Strategies:**
    - **Regular engagement communications**: Monthly newsletters, product updates
    - **Targeted cross-selling opportunities**: Based on usage patterns
    - **Customer satisfaction surveys**: Identify pain points early
    - **Educational content**: Product benefits, financial tips
    - **Periodic account reviews**: Proactive service check-ins
    - **Early warning system**: Monitor for risk factor changes
    """)

with strategy_tab3:
    st.subheader("🟢 Low Risk Customers - Retention & Growth")
    st.markdown("""
    **Characteristics:**
    - Healthy utilization patterns (<30%)
    - Consistent account activity
    - Multiple product relationships
    - High transaction engagement
    
    **Growth Strategies:**
    - **Upselling premium products**: Premium cards, investment services
    - **Referral program invitations**: Leverage satisfaction for acquisition
    - **Exclusive offers and benefits**: VIP treatment, early access
    - **Relationship manager assignment**: Dedicated support
    - **Long-term loyalty rewards**: Tiered benefits program
    - **Wealth management services**: For high-value customers
    """)

# Data summary
st.sidebar.markdown("---")
st.sidebar.subheader("Dataset Summary")
st.sidebar.write(f"Total Records: {len(df)}")
st.sidebar.write(f"Churn Rate: {df['churn'].mean()*100:.1f}%")
st.sidebar.write(f"Filtered Records: {len(filtered_df)}")


