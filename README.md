# 📦 SupplyChain365 – Supply Chain Analytics Dashboard

An interactive **Supply Chain Management and Analytics Dashboard** built using **Python, Streamlit, Pandas, NumPy and Plotly**.

SupplyChain365 helps organizations monitor supply-chain operations through interactive KPIs, inventory analysis, supplier performance, order tracking, logistics analysis and business insights.

The application is designed to run locally with Streamlit and can also be deployed as a **Databricks App**.

---

## 🚀 Project Overview

SupplyChain365 provides a centralized dashboard for monitoring important supply-chain activities.

The dashboard helps users understand:

* 📦 Inventory performance
* 🏭 Supplier performance
* 🚚 Logistics and transportation
* 🛒 Orders and sales
* 📈 Demand trends
* 💰 Revenue and cost analysis
* ⚠️ Supply-chain risks
* 📊 Operational KPIs

Users can interact with filters and charts to analyze supply-chain performance dynamically.

---

## ✨ Key Features

### 📊 Executive Dashboard

The main dashboard provides high-level KPIs such as:

* Total Orders
* Total Products
* Total Inventory
* Total Revenue
* Average Lead Time
* Supplier Count
* Delivery Performance
* Risk Indicators

---

### 📦 Inventory Management

Monitor inventory-related metrics including:

* Current stock levels
* Available inventory
* Low-stock products
* Inventory value
* Reorder requirements
* Product-wise stock distribution

This helps identify potential stock-outs and excess inventory.

---

### 🏭 Supplier Analytics

Analyze supplier performance using:

* Supplier-wise orders
* Supplier delivery performance
* Average lead time
* Supplier costs
* Supplier reliability
* Supplier risk

This helps organizations identify high-performing and high-risk suppliers.

---

### 🚚 Logistics Analytics

Analyze transportation and logistics information including:

* Shipping costs
* Transportation modes
* Delivery times
* Shipping routes
* Carrier performance
* Average transportation time

---

### 🛒 Order Analytics

Track order-related information such as:

* Total orders
* Order quantities
* Order status
* Product-wise orders
* Regional orders
* Order trends over time

---

### 📈 Demand Analysis

The application provides demand-oriented analysis using historical supply-chain data.

Users can analyze:

* Product demand
* Demand trends
* Regional demand
* Product categories
* Order quantity trends

---

### 💰 Revenue & Cost Analysis

The dashboard provides financial insights through:

* Total revenue
* Manufacturing cost
* Shipping cost
* Supplier cost
* Product price
* Revenue by region
* Cost distribution

---

### ⚠️ Risk Monitoring

Supply-chain risks can be monitored using indicators such as:

* High lead time
* Low inventory
* Supplier delays
* Transportation delays
* High shipping costs
* Product shortages

---

## 🎛️ Interactive Filters

The dashboard supports interactive filtering based on available dataset columns.

Typical filters include:

* Region
* Product
* Supplier
* Category
* Transportation Mode
* Shipping Carrier
* Date
* Order Status

When filters are changed, the dashboard KPIs and visualizations update dynamically.

---

## 🛠️ Technology Stack

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Application development                    |
| Streamlit  | Interactive web dashboard                  |
| Pandas     | Data processing                            |
| NumPy      | Numerical operations                       |
| Plotly     | Interactive visualizations                 |
| Databricks | Cloud analytics and application deployment |
| Git        | Version control                            |
| GitHub     | Source-code repository                     |

Streamlit is used for the interactive dashboard layer, while Databricks Apps can host Streamlit applications.

---

## 📁 Project Structure

```text
SupplyChain365/
│
├── data/
│   └── supply_chain_data.csv
│
├── app.py
├── generate_data.py
├── requirements.txt
├── app.yaml
├── README.md
└── .gitignore
```

---

## 📄 File Description

### `app.py`

Main Streamlit application.

It contains:

* Dashboard UI
* Sidebar navigation
* Filters
* KPI cards
* Interactive Plotly charts
* Supply-chain analytics
* Data loading
* Business insights

---

### `generate_data.py`

Python script used to generate or prepare the supply-chain dataset.

Example:

```bash
python generate_data.py
```

The generated dataset is stored inside the `data` directory.

---

### `data/`

Contains the datasets used by the Streamlit dashboard.

Example:

```text
data/
└── supply_chain_data.csv
```

---

### `requirements.txt`

Contains the Python dependencies required to run the application.

Example:

```text
streamlit
pandas
numpy
plotly
```

---

### `app.yaml`

Defines how the Streamlit application starts when deployed as a Databricks App.

Example:

```yaml
command:
  - streamlit
  - run
  - app.py
```

Databricks' current Streamlit App documentation uses this type of `app.yaml` command to start the application.

---

## 💻 Run the Project Locally

### Step 1 – Clone the repository

```bash
git clone https://github.com/Pg-h312/SupplyChain365.git
```

### Step 2 – Open the project

```bash
cd SupplyChain365
```

### Step 3 – Create virtual environment

```bash
python -m venv venv
```

### Step 4 – Activate virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked, use:

```cmd
venv\Scripts\activate.bat
```

### Step 5 – Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6 – Generate dataset

```bash
python generate_data.py
```

### Step 7 – Run Streamlit

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

# ☁️ Deploy to Databricks Apps

SupplyChain365 can be deployed as a Streamlit-based Databricks App.

### Step 1 – Open Databricks

Open your Databricks workspace.

### Step 2 – Open Apps

Go to:

```text
Workspace → Apps
```

### Step 3 – Create App

Create a new Databricks App.

### Step 4 – Upload/Connect Project

Add the project files:

```text
app.py
app.yaml
requirements.txt
data/
```

### Step 5 – Configure the App

The `app.yaml` file should contain:

```yaml
command:
  - streamlit
  - run
  - app.py
```

### Step 6 – Deploy

Start/deploy the application.

Databricks Apps supports Streamlit applications and can also connect applications to Unity Catalog and SQL Warehouses when the required permissions and connectors are configured.

---

# 🧱 Databricks Architecture

```text
                ┌─────────────────────┐
                │      GitHub         │
                │  SupplyChain365     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     Databricks      │
                │      Workspace      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Databricks App    │
                │     Streamlit       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      Pandas         │
                │    Data Processing  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     Supply Chain    │
                │       Dataset       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Plotly Interactive │
                │    Visualizations   │
                └─────────────────────┘
```

---

# 📊 Dashboard Workflow

```text
Supply Chain Dataset
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
KPI Calculation
        ↓
Interactive Filters
        ↓
Plotly Visualizations
        ↓
Business Insights
        ↓
Streamlit Dashboard
```

---

# 🔍 Example Business Questions

SupplyChain365 can help answer questions such as:

### Inventory

* Which products have low inventory?
* Which products have excessive stock?
* What is the total inventory value?

### Suppliers

* Which supplier has the best delivery performance?
* Which supplier has the highest lead time?
* Which suppliers have high risk?

### Logistics

* Which transportation mode is most expensive?
* Which carrier has the highest shipping cost?
* Where are delivery delays occurring?

### Orders

* What is the total number of orders?
* Which products have the highest demand?
* Which regions generate the most orders?

### Finance

* What is total revenue?
* Which products generate the highest revenue?
* Which suppliers contribute the highest costs?

---

# 📈 Performance Considerations

The dashboard uses Pandas and Streamlit caching where appropriate to reduce unnecessary data loading and improve interactive performance.

For larger production datasets, the application can be extended to query Databricks SQL Warehouse or Unity Catalog rather than loading the complete dataset into the application. Databricks' Streamlit tutorial demonstrates this architecture using the Databricks SQL Connector for Python.

---

# 🔐 Security

Do not store the following directly in the GitHub repository:

```text
Passwords
API keys
Access tokens
Databricks tokens
Secrets
Database credentials
```

Use environment variables, Databricks secrets, or the appropriate Databricks authentication mechanism for production deployments.

---

# 🧪 Testing

Before deployment, test the application locally:

```bash
streamlit run app.py
```

Verify:

* Dashboard loads successfully
* All sidebar options work
* Filters work correctly
* KPI values update
* Charts update
* Dataset loads correctly
* No Python code is displayed in the dashboard
* No missing-file errors occur

---

# 🐛 Troubleshooting

### Streamlit not found

Run:

```bash
pip install streamlit
```

or:

```bash
pip install -r requirements.txt
```

---

### NumPy not found

Run:

```bash
pip install numpy
```

---

### Pandas not found

Run:

```bash
pip install pandas
```

---

### Plotly not found

Run:

```bash
pip install plotly
```

---

### Dataset not found

Check that the project contains:

```text
SupplyChain365/
│
├── app.py
└── data/
    └── supply_chain_data.csv
```

---

# 🔄 GitHub Workflow

After making changes:

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "Update SupplyChain365 dashboard"
```

```bash
git push origin main
```

---

# 🎯 Future Enhancements

Possible future improvements include:

* 🤖 Machine-learning demand forecasting
* ⚠️ Supplier risk prediction
* 📦 Inventory optimization
* 🚚 Delivery-delay prediction
* 🔮 Demand forecasting
* 🧠 AI-powered supply-chain recommendations
* 📊 Databricks SQL Warehouse integration
* 🗂️ Unity Catalog integration
* 📈 Real-time monitoring
* 🔔 Automated alerts
* 📑 Automated business reports

---

# 💼 Interview Explanation

### What is SupplyChain365?

**SupplyChain365 is an interactive supply-chain analytics application built using Python and Streamlit. It provides centralized monitoring of inventory, suppliers, orders, logistics, revenue, costs and operational risks through interactive KPIs and visualizations. The application can be deployed as a Databricks App for cloud-based analytics.**

### Technologies Used

```text
Python
    ↓
Pandas / NumPy
    ↓
Data Processing
    ↓
Plotly
    ↓
Streamlit
    ↓
Databricks Apps
    ↓
Interactive Supply Chain Dashboard
```

### Why Streamlit?

Streamlit makes it possible to quickly convert Python data-analysis logic into an interactive web application without building a separate frontend framework.

### Why Databricks?

Databricks provides a scalable analytics environment and supports deploying Streamlit applications through Databricks Apps. For larger implementations, the application can be connected to Unity Catalog and SQL Warehouses.

---

# 👩‍💻 Project

**Project Name:** SupplyChain365

**Domain:** Supply Chain Analytics

**Application:** Interactive Web Dashboard

**Frontend:** Streamlit

**Programming Language:** Python

**Visualization:** Plotly

**Data Processing:** Pandas / NumPy

**Cloud Platform:** Databricks

**Version Control:** Git / GitHub

---

## ⭐ Conclusion

SupplyChain365 provides a complete interactive view of supply-chain operations. It combines data processing, visualization and cloud application deployment to help users monitor operational performance and make data-driven supply-chain decisions.

---

````

### GitHub commands

After saving this as `README.md` inside `C:\Users\priya\SupplyChain365`, run:

```powershell
cd C:\Users\priya\SupplyChain365

git add README.md

git commit -m "Add SupplyChain365 README"

git push origin main
````

If your repository currently shows **`src refspec main does not match any`**, first make sure you have at least one commit:

```powershell
git add .
git commit -m "Initial SupplyChain365 project"
git branch -M main
git push -u origin main
```
