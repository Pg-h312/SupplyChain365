import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Supply Chain 365",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background-color: #f7faff;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0b3a78 0%,
        #062b5d 100%
    );
}

section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}

.sidebar-brand {
    text-align: center;
    padding: 10px 5px 22px 5px;
}

.sidebar-icon {
    width: 52px;
    height: 52px;
    background: #1e88ff;
    border-radius: 12px;
    margin: 0 auto 8px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 27px;
}

.sidebar-title {
    color: white;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 3px;
}

.sidebar-subtitle {
    color: #d9e7ff;
    font-size: 9px;
}

/* Radio buttons */

section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 5px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] > label {
    background: transparent;
    border-radius: 7px;
    padding: 10px 10px;
    margin: 0;
    color: white !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    background: rgba(255,255,255,0.12);
}

section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"] {
    background: #2176ed;
}

section[data-testid="stSidebar"] div[role="radiogroup"] p {
    color: white !important;
    font-size: 14px;
}

/* ================= HEADER ================= */

.page-title {
    color: #123768;
    font-size: 31px;
    font-weight: 800;
    line-height: 1.1;
}

.page-subtitle {
    color: #3b5678;
    font-size: 14px;
    margin-top: 4px;
}

/* ================= KPI ================= */

.kpi-card {
    background: white;
    border: 1px solid #d9e7f7;
    border-radius: 7px;
    padding: 15px;
    min-height: 125px;
    box-shadow: 0 1px 5px rgba(20,60,110,0.04);
}

.kpi-label {
    color: #23446d;
    font-size: 13px;
    min-height: 20px;
}

.kpi-value {
    color: #082e63;
    font-size: 23px;
    font-weight: 800;
    margin-top: 7px;
}

.kpi-up {
    color: #00aa68;
    font-size: 13px;
    font-weight: 600;
    margin-top: 7px;
}

.kpi-down {
    color: #00aa68;
    font-size: 13px;
    font-weight: 600;
    margin-top: 7px;
}

.kpi-small {
    color: #68809f;
    font-size: 11px;
}

/* ================= CARDS ================= */

.dashboard-card {
    background: white;
    border: 1px solid #d9e7f7;
    border-radius: 7px;
    padding: 5px 10px 5px 10px;
    margin-bottom: 8px;
}

.card-title {
    color: #092e62;
    font-size: 16px;
    font-weight: 700;
    padding: 4px;
}

/* ================= INSIGHTS ================= */

.insight-box {
    background: #f1f8ff;
    border: 1px solid #deebf8;
    border-radius: 7px;
    padding: 9px 11px;
    margin-bottom: 7px;
    color: #153962;
    font-size: 12px;
}

/* ================= METRIC ================= */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #d9e7f7;
    padding: 15px;
    border-radius: 8px;
}

/* ================= DATAFRAME ================= */

div[data-testid="stDataFrame"] {
    border: 1px solid #d9e7f7;
    border-radius: 7px;
}

/* ================= BUTTON ================= */

.stDownloadButton button {
    background: #1769e8;
    color: white;
    border-radius: 6px;
    border: none;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    inventory = pd.read_csv("data/inventory.csv")
    orders = pd.read_csv("data/orders.csv")
    shipments = pd.read_csv("data/shipments.csv")
    suppliers = pd.read_csv("data/suppliers.csv")
    products = pd.read_csv("data/products.csv")
    customers = pd.read_csv("data/customers.csv")

    inventory["Month"] = pd.to_datetime(
        inventory["Month"],
        errors="coerce"
    )

    orders["Order_Date"] = pd.to_datetime(
        orders["Order_Date"],
        errors="coerce"
    )

    shipments["Ship_Date"] = pd.to_datetime(
        shipments["Ship_Date"],
        errors="coerce"
    )

    shipments["Delivery_Date"] = pd.to_datetime(
        shipments["Delivery_Date"],
        errors="coerce"
    )

    return (
        inventory,
        orders,
        shipments,
        suppliers,
        products,
        customers
    )


try:

    (
        inventory,
        orders,
        shipments,
        suppliers,
        products,
        customers
    ) = load_data()

except Exception as e:

    st.error(
        "Unable to load data. Please make sure the data folder "
        "contains all required CSV files."
    )

    st.exception(e)
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-icon">📦</div>
            <div class="sidebar-title">Supply Chain 365</div>
            <div class="sidebar-subtitle">
                Smarter Supply Chains. Better Tomorrow.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    menu = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📦 Inventory",
            "🛒 Orders",
            "🚚 Shipments",
            "👥 Suppliers",
            "👥 Customers",
            "📈 Forecasting",
            "📄 Reports",
            "⚙️ Settings"
        ],
        label_visibility="collapsed"
    )


# ============================================================
# HEADER
# ============================================================

header_left, header_right = st.columns([4, 1])

with header_left:

    st.markdown(
        '<div class="page-title">Supply Chain 365</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'End-to-End Visibility &nbsp; | &nbsp; '
        'Real-Time Insights &nbsp; | &nbsp; '
        'Smarter Decisions'
        '</div>',
        unsafe_allow_html=True
    )

with header_right:

    st.markdown(
        """
        <div style="
            text-align:right;
            padding-top:12px;
            color:#173862;
            font-size:14px;
        ">
        👤 <b>Priya Gupta</b>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# ============================================================
# GLOBAL FILTERS
# ============================================================

filter1, filter2 = st.columns([2, 1])

with filter1:

    date_range = st.date_input(
        "Date Range",
        value=(
            pd.Timestamp("2025-01-01").date(),
            pd.Timestamp("2025-12-31").date()
        )
    )

with filter2:

    region_options = ["All Regions"] + sorted(
        orders["Region"].dropna().unique().tolist()
    )

    selected_region = st.selectbox(
        "Region",
        region_options
    )


# ============================================================
# SAFE DATE FILTER
# ============================================================

if isinstance(date_range, tuple) and len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])

    end_date = (
        pd.Timestamp(date_range[1])
        + pd.Timedelta(days=1)
        - pd.Timedelta(seconds=1)
    )

else:

    start_date = pd.Timestamp("2025-01-01")

    end_date = pd.Timestamp("2025-12-31 23:59:59")


# ============================================================
# FILTER ORDERS
# ============================================================

filtered_orders = orders[
    (orders["Order_Date"] >= start_date) &
    (orders["Order_Date"] <= end_date)
].copy()


# ============================================================
# FILTER SHIPMENTS
# ============================================================

filtered_shipments = shipments[
    (shipments["Ship_Date"] >= start_date) &
    (shipments["Ship_Date"] <= end_date)
].copy()


# ============================================================
# REGION FILTER
# ============================================================

if selected_region != "All Regions":

    filtered_orders = filtered_orders[
        filtered_orders["Region"] == selected_region
    ]

    filtered_shipments = filtered_shipments[
        filtered_shipments["Destination"] == selected_region
    ]


# ============================================================
# GLOBAL KPI CALCULATIONS
#
# IMPORTANT:
# These calculations are BEFORE the sidebar page conditions.
# Therefore Reports page will NOT get:
# NameError: name 'on_time_rate' is not defined
# ============================================================

total_inventory = float(
    inventory["Total_Inventory"].iloc[-1]
)

total_orders = len(filtered_orders)

total_shipments = len(filtered_shipments)

delivered_shipments = (
    filtered_shipments["Status"]
    .eq("Delivered")
    .sum()
)

if total_shipments > 0:

    on_time_rate = (
        delivered_shipments /
        total_shipments
    ) * 100

else:

    on_time_rate = 0.0


stockout_risk = 2.8


# ============================================================
# DASHBOARD PAGE
# ============================================================

if menu == "🏠 Dashboard":

    # ========================================================
    # KPI CARDS
    # ========================================================

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    📦 &nbsp; Total Inventory Value
                </div>
                <div class="kpi-value">
                    ${total_inventory:,.0f}
                </div>
                <div class="kpi-up">
                    ↑ 12.5%
                </div>
                <div class="kpi-small">
                    vs. last month
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k2:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    🛒 &nbsp; Total Orders
                </div>
                <div class="kpi-value">
                    {total_orders:,}
                </div>
                <div class="kpi-up">
                    ↑ 8.3%
                </div>
                <div class="kpi-small">
                    vs. last month
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k3:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    🚚 &nbsp; Total Shipments
                </div>
                <div class="kpi-value">
                    {total_shipments:,}
                </div>
                <div class="kpi-up">
                    ↑ 10.7%
                </div>
                <div class="kpi-small">
                    vs. last month
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k4:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    👥 &nbsp; On-Time Delivery Rate
                </div>
                <div class="kpi-value">
                    {on_time_rate:.1f}%
                </div>
                <div class="kpi-up">
                    ↑ 2.1%
                </div>
                <div class="kpi-small">
                    vs. last month
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k5:

        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">
                    ⚠️ &nbsp; Stockout Risk
                </div>
                <div class="kpi-value">
                    2.8%
                </div>
                <div class="kpi-down">
                    ↓ 3.6%
                </div>
                <div class="kpi-small">
                    vs. last month
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    # ========================================================
    # FIRST CHART ROW
    # ========================================================

    c1, c2, c3 = st.columns([1.35, 1.05, 0.95])


    # ========================================================
    # INVENTORY TREND
    # ========================================================

    with c1:

        st.markdown(
            '<div class="card-title">Inventory Trend</div>',
            unsafe_allow_html=True
        )

        fig_inventory = go.Figure()

        fig_inventory.add_trace(
            go.Scatter(
                x=inventory["Month"],
                y=inventory["Total_Inventory"],
                mode="lines+markers",
                name="Total Inventory",
                line=dict(width=3)
            )
        )

        fig_inventory.add_trace(
            go.Scatter(
                x=inventory["Month"],
                y=inventory["Raw_Materials"],
                mode="lines+markers",
                name="Raw Materials"
            )
        )

        fig_inventory.add_trace(
            go.Scatter(
                x=inventory["Month"],
                y=inventory["Finished_Goods"],
                mode="lines+markers",
                name="Finished Goods"
            )
        )

        fig_inventory.update_layout(
            height=275,
            margin=dict(l=5, r=5, t=10, b=5),
            plot_bgcolor="white",
            paper_bgcolor="white",
            legend=dict(
                orientation="h",
                y=1.08,
                font=dict(size=9)
            ),
            xaxis=dict(
                tickformat="%b",
                gridcolor="#e5edf7"
            ),
            yaxis=dict(
                tickformat=".2s",
                gridcolor="#e5edf7"
            )
        )

        st.plotly_chart(
            fig_inventory,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ========================================================
    # CATEGORY DONUT
    # ========================================================

    with c2:

        st.markdown(
            '<div class="card-title">'
            'Inventory by Product Category'
            '</div>',
            unsafe_allow_html=True
        )

        category_data = pd.DataFrame(
            {
                "Category": [
                    "Electronics",
                    "Apparel",
                    "Home & Living",
                    "Automotive",
                    "Health & Beauty",
                    "Others"
                ],
                "Percentage": [
                    28.4,
                    18.7,
                    16.2,
                    12.5,
                    9.8,
                    14.4
                ]
            }
        )

        fig_category = px.pie(
            category_data,
            names="Category",
            values="Percentage",
            hole=0.58
        )

        fig_category.update_layout(
            height=275,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor="white",
            legend=dict(
                font=dict(size=9)
            )
        )

        fig_category.update_traces(
            textinfo="percent",
            textposition="inside"
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ========================================================
    # ORDERS BY REGION
    # ========================================================

    with c3:

        st.markdown(
            '<div class="card-title">Orders by Region</div>',
            unsafe_allow_html=True
        )

        region_orders = (
            filtered_orders
            .groupby("Region")
            .size()
            .reset_index(name="Orders")
        )

        fig_region = px.bar(
            region_orders,
            x="Region",
            y="Orders",
            text="Orders"
        )

        fig_region.update_layout(
            height=275,
            margin=dict(l=5, r=5, t=10, b=5),
            plot_bgcolor="white",
            paper_bgcolor="white",
            showlegend=False,
            xaxis=dict(
                gridcolor="#ffffff"
            ),
            yaxis=dict(
                gridcolor="#e5edf7"
            )
        )

        fig_region.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig_region,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ========================================================
    # SECOND CHART ROW
    # ========================================================

    c4, c5, c6 = st.columns([1.2, 1.1, 1])


    # ========================================================
    # SUPPLIERS
    # ========================================================

    with c4:

        st.markdown(
            '<div class="card-title">'
            'Top 5 Suppliers by Order Volume'
            '</div>',
            unsafe_allow_html=True
        )

        top_suppliers = (
            suppliers
            .sort_values(
                "Orders",
                ascending=False
            )
            .head(5)
            .copy()
        )

        top_suppliers["Rank"] = range(1, 6)

        top_suppliers = top_suppliers[
            [
                "Rank",
                "Supplier_Name",
                "Orders",
                "Total_Value"
            ]
        ]

        top_suppliers["Total_Value"] = (
            top_suppliers["Total_Value"]
            .apply(lambda x: f"${x:,.0f}")
        )

        top_suppliers.columns = [
            "#",
            "Supplier Name",
            "Orders",
            "Total Value"
        ]

        st.dataframe(
            top_suppliers,
            use_container_width=True,
            hide_index=True,
            height=225
        )


    # ========================================================
    # SHIPMENT DELIVERY
    # ========================================================

    with c5:

        st.markdown(
            '<div class="card-title">'
            'Shipment Delivery Performance'
            '</div>',
            unsafe_allow_html=True
        )

        monthly_shipments = (
            filtered_shipments
            .assign(
                Month=filtered_shipments[
                    "Ship_Date"
                ].dt.month
            )
            .groupby(
                ["Month", "Status"]
            )
            .size()
            .reset_index(name="Count")
        )

        month_names = [
            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug",
            "Sep", "Oct", "Nov", "Dec"
        ]

        delivered_values = []

        delayed_values = []

        for month_number in range(1, 13):

            delivered_count = (
                monthly_shipments[
                    (monthly_shipments["Month"] == month_number) &
                    (monthly_shipments["Status"] == "Delivered")
                ]["Count"]
                .sum()
            )

            delayed_count = (
                monthly_shipments[
                    (monthly_shipments["Month"] == month_number) &
                    (monthly_shipments["Status"] == "Delayed")
                ]["Count"]
                .sum()
            )

            delivered_values.append(delivered_count)

            delayed_values.append(delayed_count)

        fig_ship = go.Figure()

        fig_ship.add_trace(
            go.Bar(
                x=month_names,
                y=delivered_values,
                name="Delivered"
            )
        )

        fig_ship.add_trace(
            go.Bar(
                x=month_names,
                y=delayed_values,
                name="Delayed"
            )
        )

        fig_ship.update_layout(
            barmode="stack",
            height=225,
            margin=dict(l=5, r=5, t=5, b=5),
            plot_bgcolor="white",
            paper_bgcolor="white",
            yaxis=dict(
                gridcolor="#e5edf7"
            ),
            legend=dict(
                orientation="h",
                y=1.1
            )
        )

        st.plotly_chart(
            fig_ship,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ========================================================
    # FORECAST VS ACTUAL
    # ========================================================

    with c6:

        st.markdown(
            '<div class="card-title">'
            'Forecast vs Actual Demand'
            '</div>',
            unsafe_allow_html=True
        )

        monthly_actual = (
            filtered_orders
            .assign(
                Month=filtered_orders[
                    "Order_Date"
                ].dt.month
            )
            .groupby("Month")
            .size()
        )

        actual_values = [
            monthly_actual.get(
                month,
                0
            )
            for month in range(1, 13)
        ]

        forecast_values = (
            pd.Series(actual_values)
            .rolling(
                3,
                min_periods=1
            )
            .mean()
            .tolist()
        )

        fig_forecast = go.Figure()

        fig_forecast.add_trace(
            go.Scatter(
                x=month_names,
                y=forecast_values,
                mode="lines+markers",
                name="Forecast"
            )
        )

        fig_forecast.add_trace(
            go.Scatter(
                x=month_names,
                y=actual_values,
                mode="lines+markers",
                name="Actual"
            )
        )

        fig_forecast.update_layout(
            height=225,
            margin=dict(l=5, r=5, t=5, b=5),
            plot_bgcolor="white",
            paper_bgcolor="white",
            yaxis=dict(
                gridcolor="#e5edf7"
            ),
            legend=dict(
                orientation="h",
                y=1.1
            )
        )

        st.plotly_chart(
            fig_forecast,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ========================================================
    # RECENT SHIPMENTS
    # ========================================================

    c7, c8 = st.columns([1.55, 0.95])


    with c7:

        st.markdown(
            '<div class="card-title">'
            'Recent Shipments'
            '</div>',
            unsafe_allow_html=True
        )

        recent_shipments = (
            filtered_shipments
            .sort_values(
                "Ship_Date",
                ascending=False
            )
            .head(5)
            .copy()
        )

        recent_shipments = recent_shipments[
            [
                "Shipment_ID",
                "Order_ID",
                "Product",
                "Destination",
                "Status",
                "Ship_Date",
                "Delivery_Date"
            ]
        ]

        recent_shipments["Ship_Date"] = (
            recent_shipments["Ship_Date"]
            .dt.strftime("%Y-%m-%d")
        )

        recent_shipments["Delivery_Date"] = (
            recent_shipments["Delivery_Date"]
            .dt.strftime("%Y-%m-%d")
        )

        recent_shipments.columns = [
            "Shipment ID",
            "Order ID",
            "Product",
            "Destination",
            "Status",
            "Ship Date",
            "Delivery Date"
        ]

        st.dataframe(
            recent_shipments,
            use_container_width=True,
            hide_index=True,
            height=220
        )


    # ========================================================
    # KEY INSIGHTS
    # ========================================================

    with c8:

        st.markdown(
            '<div class="card-title">💡 Key Insights</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="insight-box">
                📈 <b>Inventory value increased by 12.5%</b>
                compared to last month.
            </div>

            <div class="insight-box">
                🚚 <b>On-time delivery performance</b>
                remains strong.
            </div>

            <div class="insight-box">
                ⚠️ <b>Stockout risk is currently 2.8%.</b>
                Consider increasing safety stock.
            </div>

            <div class="insight-box">
                📊 <b>Regional order volume</b>
                is being monitored continuously.
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# INVENTORY PAGE
# ============================================================

elif menu == "📦 Inventory":

    st.title("📦 Inventory Management")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Inventory Value",
            f"${total_inventory:,.0f}"
        )

    with col2:
        st.metric(
            "Raw Materials",
            f"${inventory['Raw_Materials'].iloc[-1]:,.0f}"
        )

    with col3:
        st.metric(
            "Finished Goods",
            f"${inventory['Finished_Goods'].iloc[-1]:,.0f}"
        )

    fig = px.line(
        inventory,
        x="Month",
        y=[
            "Total_Inventory",
            "Raw_Materials",
            "Finished_Goods"
        ],
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Inventory Records")

    st.dataframe(
        inventory,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# ORDERS PAGE
# ============================================================

elif menu == "🛒 Orders":

    st.title("🛒 Orders Management")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Orders",
            f"{len(filtered_orders):,}"
        )

    with col2:
        st.metric(
            "Total Order Value",
            f"${filtered_orders['Order_Value'].sum():,.0f}"
        )

    with col3:
        st.metric(
            "Total Quantity",
            f"{filtered_orders['Quantity'].sum():,}"
        )

    region_data = (
        filtered_orders
        .groupby("Region")
        .size()
        .reset_index(name="Orders")
    )

    fig = px.bar(
        region_data,
        x="Region",
        y="Orders",
        text="Orders"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Orders")

    st.dataframe(
        filtered_orders,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# SHIPMENTS PAGE
# ============================================================

elif menu == "🚚 Shipments":

    st.title("🚚 Shipment Tracking")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Shipments",
            f"{len(filtered_shipments):,}"
        )

    with col2:
        st.metric(
            "Delivered",
            f"{(
                filtered_shipments['Status']
                .eq('Delivered')
                .sum()
            ):,}"
        )

    with col3:
        st.metric(
            "Delayed",
            f"{(
                filtered_shipments['Status']
                .eq('Delayed')
                .sum()
            ):,}"
        )

    status_data = (
        filtered_shipments
        .groupby("Status")
        .size()
        .reset_index(name="Shipments")
    )

    fig = px.pie(
        status_data,
        names="Status",
        values="Shipments",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Shipment Records")

    st.dataframe(
        filtered_shipments,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# SUPPLIERS PAGE
# ============================================================

elif menu == "👥 Suppliers":

    st.title("👥 Supplier Management")

    top_suppliers = (
        suppliers
        .sort_values(
            "Orders",
            ascending=False
        )
    )

    fig = px.bar(
        top_suppliers,
        x="Supplier_Name",
        y="Orders",
        text="Orders"
    )

    fig.update_layout(
        xaxis_title="Supplier",
        yaxis_title="Orders"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Supplier Records")

    st.dataframe(
        suppliers,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CUSTOMERS PAGE
# ============================================================

elif menu == "👥 Customers":

    st.title("👥 Customer Management")

    customer_region = (
        customers
        .groupby("Region")
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        customer_region,
        x="Region",
        y="Customers",
        text="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Customer Records")

    st.dataframe(
        customers,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FORECASTING PAGE
# ============================================================

elif menu == "📈 Forecasting":

    st.title("📈 Demand Forecasting")

    monthly_forecast = (
        filtered_orders
        .assign(
            Month=filtered_orders[
                "Order_Date"
            ].dt.to_period("M")
        )
        .groupby("Month")
        .size()
        .reset_index(name="Actual")
    )

    monthly_forecast["Forecast"] = (
        monthly_forecast["Actual"]
        .rolling(
            3,
            min_periods=1
        )
        .mean()
    )

    monthly_forecast["Month"] = (
        monthly_forecast["Month"]
        .astype(str)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=monthly_forecast["Month"],
            y=monthly_forecast["Actual"],
            mode="lines+markers",
            name="Actual"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=monthly_forecast["Month"],
            y=monthly_forecast["Forecast"],
            mode="lines+markers",
            name="Forecast"
        )
    )

    fig.update_layout(
        title="Demand Forecast vs Actual",
        xaxis_title="Month",
        yaxis_title="Orders"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        monthly_forecast,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# REPORTS PAGE
# ============================================================

elif menu == "📄 Reports":

    st.title("📄 Supply Chain Reports")

    # on_time_rate is already calculated ABOVE,
    # so this page will NOT generate NameError.

    report_data = pd.DataFrame(
        {
            "Metric": [
                "Inventory Value",
                "Total Orders",
                "Total Shipments",
                "On-Time Delivery Rate",
                "Stockout Risk"
            ],
            "Value": [
                f"${total_inventory:,.0f}",
                f"{total_orders:,}",
                f"{total_shipments:,}",
                f"{on_time_rate:.1f}%",
                f"{stockout_risk:.1f}%"
            ]
        }
    )

    st.dataframe(
        report_data,
        use_container_width=True,
        hide_index=True
    )

    st.write("")

    csv_report = report_data.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Report",
        data=csv_report,
        file_name="supply_chain_report.csv",
        mime="text/csv"
    )


# ============================================================
# SETTINGS PAGE
# ============================================================

elif menu == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.subheader("Dashboard Settings")

    show_insights = st.toggle(
        "Show Key Insights",
        value=True
    )

    auto_refresh = st.toggle(
        "Enable Auto Refresh",
        value=False
    )

    currency = st.selectbox(
        "Currency",
        [
            "USD",
            "INR",
            "EUR",
            "GBP"
        ]
    )

    st.write("")

    st.success(
        "Supply Chain 365 settings updated successfully."
    )

    st.info(
        f"Currency: {currency} | "
        f"Key Insights: {'ON' if show_insights else 'OFF'} | "
        f"Auto Refresh: {'ON' if auto_refresh else 'OFF'}"
    )