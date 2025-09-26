# PR - Business Intelligence Platform

A comprehensive business intelligence platform powered by machine learning that provides intelligent recommendations, data analysis, and insights to drive business growth.

## 🌟 Features

- **AI-Powered Recommendations**: Generate intelligent business recommendations using machine learning
- **Advanced Data Analysis**: Comprehensive data analysis with statistical insights
- **Interactive Dashboard**: Real-time metrics and performance tracking
- **Multi-format Data Support**: Support for CSV, Excel, and JSON data formats
- **Customer Analytics**: Customer segmentation and behavioral analysis
- **Sales Optimization**: Sales performance analysis and optimization recommendations
- **Marketing Intelligence**: Campaign analysis and marketing optimization
- **Operations Insights**: Operational efficiency analysis and recommendations

## 📋 Requirements

- Python 3.9+ (Python 3.13 supported)
- Flask 3.0+
- pandas 2.1+
- scikit-learn 1.4+
- numpy 1.26+
- matplotlib 3.8+
- seaborn 0.13+
- plotly 5.17+

**Note**: If you're using Python 3.13, make sure to use the updated package versions to avoid compatibility issues.

## 🚀 Quick Start

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd pr

# Or download and extract the ZIP file
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
PR/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── config.py                       # Configuration settings
├── models/
│   ├── __init__.py
│   ├── recommendation_engine.py    # Core ML recommendation logic
│   └── data_analyzer.py           # Data analysis utilities
├── static/
│   ├── css/
│   │   └── style.css              # Frontend styling
│   └── js/
│       └── main.js                # Frontend JavaScript
├── templates/
│   ├── base.html                  # Base template
│   ├── dashboard.html             # Main dashboard
│   └── recommendations.html       # Recommendations page
├── data/
│   ├── sample_sales_data.csv      # Sample sales dataset
│   ├── sample_customer_data.csv   # Sample customer dataset
│   ├── sample_marketing_data.csv  # Sample marketing dataset
│   └── sample_operations_data.csv # Sample operations dataset
├── tests/
│   ├── __init__.py
│   └── test_recommendations.py    # Test cases
└── README.md                      # This file
```

## 🎯 Complete User Journey & Features

### 📊 Dashboard Page - Your Business Command Center
<img width="3672" height="1653" alt="image" src="https://github.com/user-attachments/assets/61525db6-bd97-40b1-aa32-e47f35c1bdcc" />
<img width="2850" height="1572" alt="image" src="https://github.com/user-attachments/assets/1a675ccb-c613-415d-a951-907559b2094d" />
<img width="2817" height="1221" alt="image" src="https://github.com/user-attachments/assets/d393a5bd-5fa2-4027-be14-4a4ec5229fe7" />
<img width="2841" height="1092" alt="image" src="https://github.com/user-attachments/assets/88a0efbf-981a-414c-8ec1-4f1ff90f1a2d" />
<img width="1176" height="1341" alt="image" src="https://github.com/user-attachments/assets/f36bdcf2-74a8-4627-b1cd-cb99e1c7f5f2" />

The dashboard is your main hub for monitoring business performance and accessing key features.

**What You See:**
- **Key Performance Metrics**: Real-time display of critical business KPIs
  - Total Sales: Current revenue performance ($125,000)
  - Total Customers: Active customer base (1,250 customers)
  - Average Order Value: Per-transaction value ($85.50)
  - Conversion Rate: Success rate of customer interactions (3.2%)

- **Quick Action Center**: One-click access to core features
  - 📊 **Get Recommendations**: Launch AI-powered business insights
  - 🔍 **Run Analysis**: Deep-dive into your data patterns
  - 📁 **Upload Data**: Import your own business data for analysis

- **Recent Activity Monitor**: Track what's happening in your system
  - Real-time feed of completed analyses
  - Status tracking (Completed, In Progress, Pending)
  - Impact measurement of implemented recommendations

- **Performance Visualizations**: 
  - **Sales Performance Chart**: Trend analysis showing 15% monthly growth
  - **Customer Analytics**: Segment breakdown (High Value: 25%, Regular: 60%, New: 15%)
  - **Key Insights**: Actionable takeaways like "Peak sales time: 2-4 PM"

- **System Health Dashboard**: Monitor platform status
  - ML Models: Online and optimized
  - Data Pipeline: Active and processing
  - API Services: Healthy and responsive

**What It Does:** Provides immediate visibility into business health and serves as the launch point for deeper analysis.

*[Insert Dashboard Screenshot Here]*

---

### 🎯 Recommendations Page - AI-Powered Business Intelligence

This is where the magic happens - AI analyzes your data and provides actionable business recommendations.

**Page Structure:**

#### 1. **Recommendation Generator (Top Section)**
**What You Control:**
- **Recommendation Type**: Choose focus area
  - General Business Insights
  - Sales Optimization  
  - Customer Retention
  - Product Development
  - Marketing Strategy

- **Time Period**: Select analysis window
  - Last 7 Days: Short-term trends
  - Last 30 Days: Monthly patterns (default)
  - Last 90 Days: Quarterly insights
  - Last Year: Annual analysis

- **Confidence Threshold**: Set minimum reliability (70% default)
  - Higher threshold = fewer but more reliable recommendations
  - Lower threshold = more recommendations with varying confidence

**What It Does:** Configures the AI engine to generate targeted recommendations based on your specific needs and data timeframe.

#### 2. **Current Recommendations (Main Content)**
**Live AI-Generated Insights:**

**Example Recommendation Cards:**

**🎯 Optimize Product Mix** (Confidence: 92.3%)
- **Category**: Product Strategy
- **What It Means**: AI identified high-ROI products in your inventory
- **Actionable Items**:
  - Increase inventory for Product A (highest ROI)
  - Bundle Product B with complementary items
  - Consider discontinuing low-performing Product X
  - Launch targeted promotion for Product C
- **Actions**: Implement | Save for Later | Dismiss

**👥 Customer Retention Strategy** (Confidence: 87.1%)
- **Category**: Customer Management
- **What It Means**: AI found at-risk customer segments through behavioral analysis
- **Actionable Items**:
  - Create loyalty program for high-value customers
  - Send personalized re-engagement emails
  - Offer exclusive discounts to dormant customers
  - Implement win-back campaigns for churned customers
- **Actions**: Implement | Save for Later | Dismiss

**📈 Marketing Channel Optimization** (Confidence: 78.9%)
- **Category**: Marketing Strategy
- **What It Means**: AI analyzed channel performance vs customer acquisition cost
- **Actionable Items**:
  - Increase social media advertising budget by 25%
  - Reduce traditional advertising spend
  - Focus on content marketing for organic growth
  - Implement referral program incentives
- **Actions**: Implement | Save for Later | Dismiss

#### 3. **Recommendation History (Bottom Section)**
**Track Your Success:**
- **Implementation Record**: See which recommendations you've acted on
- **Impact Measurement**: Track actual results (e.g., "+$15K savings", "+12% CTR")
- **Status Monitoring**: View progress of in-flight recommendations
- **Success Analytics**: Overall implementation rate and ROI

**What It Does:** Provides accountability and learning - shows the real business impact of AI recommendations over time.

*[Insert Recommendations Page Screenshots Here]*

#### 4. **Success Metrics Dashboard**
**Performance Tracking:**
- **89.4% Implementation Success Rate**: How often recommendations work
- **$47K Total Value Generated**: Cumulative business impact
- **23 Recommendations This Month**: Volume of AI insights provided

**Recommendation Categories Breakdown:**
- Sales Optimization: 40% of recommendations
- Customer Retention: 25% of recommendations  
- Marketing: 20% of recommendations
- Operations: 15% of recommendations

**What It Means:** The AI is successfully identifying high-impact opportunities across all areas of your business, with nearly 9 out of 10 recommendations delivering measurable results.

---

### 🔄 End-to-End Workflow: From Data to Action

**Step 1: Data Foundation**
- Upload your business data (CSV/Excel files) or use included sample data
- System automatically processes and validates the data
- Creates baseline metrics visible on dashboard

**Step 2: AI Analysis** 
- Machine learning models analyze patterns in your data
- Identifies correlations, trends, and anomalies
- Segments customers and products automatically
- Calculates confidence scores for each insight

**Step 3: Recommendation Generation**
- AI generates specific, actionable recommendations
- Each recommendation includes confidence level and expected impact
- Recommendations span sales, marketing, customer retention, and operations
- Prioritized by potential business value

**Step 4: Implementation Tracking**
- Mark recommendations as implemented
- System tracks actual results vs predicted impact
- Learn which types of recommendations work best for your business
- Continuous improvement of AI accuracy

**Step 5: Business Impact**
- Monitor ROI from implemented recommendations
- View success metrics and cumulative value generated
- Use insights to inform future business strategy
- Scale successful recommendations across similar scenarios

**The Complete Value Proposition:**
This platform transforms raw business data into actionable intelligence, helping you make data-driven decisions with confidence. Whether you're optimizing product mix, improving customer retention, or reallocating marketing spend, the AI provides specific guidance backed by statistical analysis of your actual business data.

## 📊 Sample Data

The application comes with sample datasets to help you get started:

### Sales Data (`sample_sales_data.csv`)
- Product sales volumes and revenue
- Regional performance data
- Profit margins and costs
- Time-series sales data

### Customer Data (`sample_customer_data.csv`)
- Customer demographics and behavior
- Purchase history and patterns
- Loyalty status and lifetime value
- Geographic distribution

### Marketing Data (`sample_marketing_data.csv`)
- Campaign performance metrics
- Channel effectiveness data
- ROI and conversion tracking
- Budget allocation insights

### Operations Data (`sample_operations_data.csv`)
- Operational efficiency metrics
- Process performance data
- Resource utilization
- Quality and downtime tracking

## 🔧 Configuration

### Environment Variables

You can customize the application by setting these environment variables:

```bash
# Security
SECRET_KEY=your-secret-key-here

# Database (if needed)
DATABASE_URL=sqlite:///app.db

# Debug Mode
FLASK_DEBUG=True
```

### Configuration File

Modify `config.py` to customize:
- Model cache size
- Recommendation limits
- Data file paths
- Processing parameters

## 📈 Detailed Usage Guide

### 🎯 Generating AI Recommendations (Step-by-Step)

**Scenario**: You want to improve sales performance

1. **Navigate to Recommendations Page**
   - Click "Recommendations" in the main navigation
   - Or click "📊 Get Recommendations" from Dashboard

2. **Configure Your Analysis**
   - **Recommendation Type**: Select "Sales Optimization"
   - **Time Period**: Choose "Last 30 Days" for monthly trends
   - **Confidence Level**: Set to 80% for high-quality insights

3. **Generate Recommendations**
   - Click "🎯 Generate Recommendations"
   - AI analyzes your sales data patterns
   - System generates 3-5 actionable recommendations

4. **Review AI Insights**
   - Each recommendation shows confidence score
   - Read specific action items
   - Review expected business impact

5. **Take Action**
   - Click "Implement" for immediate action
   - Click "Save for Later" to bookmark
   - Click "Dismiss" if not relevant

**Expected Output**: AI-generated recommendations like "Focus on Product A (highest margin)" with specific steps to increase revenue.

### 📁 Uploading and Analyzing Your Business Data

**Scenario**: You have your own sales data to analyze

1. **Prepare Your Data File**
   - Format: CSV or Excel (.xlsx)
   - Required columns vary by data type:
     - **Sales Data**: product_id, sales_volume, revenue, date
     - **Customer Data**: customer_id, purchase_history, demographics
     - **Marketing Data**: campaign_name, spend, conversions, ROI

2. **Upload Process**
   - Click "📁 Upload Data" from any page
   - Select your prepared file
   - System validates data format
   - Automatic processing begins

3. **View Processing Results**
   - Check "Recent Activity" on Dashboard
   - Status changes from "Processing" to "Completed"
   - New metrics appear in dashboard

4. **Generate Custom Recommendations**
   - Go to Recommendations page
   - AI now uses YOUR data instead of sample data
   - Recommendations become specific to your business

**Example**: Upload customer purchase history → AI identifies high-value customer segments → Recommends targeted retention strategies.

### 🔍 Running Deep Data Analysis

**Scenario**: You want to understand patterns in your data

1. **Initiate Analysis**
   - Click "🔍 Run Analysis" from Dashboard
   - System performs comprehensive statistical analysis
   - Processing typically takes 30-60 seconds

2. **Analysis Components**
   - **Statistical Summary**: Mean, median, standard deviation
   - **Correlation Analysis**: Which metrics influence each other
   - **Outlier Detection**: Unusual data points that need attention
   - **Clustering**: Natural customer/product groupings
   - **Distribution Analysis**: Data patterns and trends

3. **View Results**
   - Results appear in expandable sections on Dashboard
   - Interactive charts show key findings
   - Written insights explain what the numbers mean

4. **Business Applications**
   - Use correlation insights for pricing strategies
   - Apply clustering results for customer segmentation
   - Address outliers as potential problems or opportunities

**Example Output**: "Strong correlation (0.85) between customer age and purchase frequency. Consider age-based marketing campaigns."

### 🔄 End-to-End Business Optimization Workflow

**Complete 30-Day Improvement Cycle:**

**Week 1: Data Foundation**
- Upload your business data
- Review dashboard metrics baseline
- Run initial analysis to understand current state

**Week 2: AI-Driven Insights**
- Generate recommendations across all categories
- Prioritize high-confidence, high-impact suggestions
- Create implementation timeline

**Week 3: Implementation**
- Execute top 3 recommendations
- Mark as "Implemented" in system
- Monitor early results

**Week 4: Results & Optimization**
- Track actual impact vs predicted impact
- Generate new recommendations based on recent changes
- Plan next month's optimization cycle

**Continuous Improvement**: Each cycle improves AI accuracy as it learns what works for your specific business.

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
python -m pytest tests/
# or
python tests/test_recommendations.py
```

### Test Coverage

The test suite covers:
- Recommendation engine functionality
- Data analysis algorithms
- Integration workflows
- Error handling
- Data validation

## 🔒 Security Considerations

- Change the default `SECRET_KEY` in production
- Implement proper authentication for multi-user environments
- Validate uploaded data files
- Use HTTPS in production deployments
- Regularly update dependencies

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

For production, consider using:
- **Gunicorn**: `gunicorn -w 4 app:app`
- **Docker**: Create a Dockerfile for containerization
- **Cloud Platforms**: Deploy to AWS, Google Cloud, or Azure
- **Reverse Proxy**: Use Nginx for production serving

### Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📚 API Documentation

### Endpoints

#### GET `/`
Main dashboard page

#### GET `/recommendations`
Recommendations management page

#### POST `/api/recommendations`
Generate new recommendations
```json
{
  "type": "sales",
  "data": {...},
  "confidence_threshold": 0.8
}
```

#### POST `/api/analysis`
Run data analysis
```json
{
  "data": {...},
  "analysis_type": "comprehensive"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

### Common Issues

**Python 3.13 Compatibility Issues**
If you get errors like `AttributeError: module 'pkgutil' has no attribute 'ImpImporter'`:
```bash
# First upgrade pip and essential tools
python -m pip install --upgrade pip setuptools wheel

# Then install requirements
pip install -r requirements.txt
```

**Alternative: Use Python 3.11 or 3.12**
If you continue having issues with Python 3.13:
```bash
# Create virtual environment with older Python version
python3.11 -m venv venv
# or
python3.12 -m venv venv
```

**Import Errors**
```bash
pip install -r requirements.txt
```

**Port Already in Use**
```bash
# Change the port in app.py
app.run(debug=True, port=5001)
```

**Data Loading Issues**
- Ensure CSV files are properly formatted
- Check file permissions
- Verify data paths in config.py

**Model Training Errors**
- Ensure sufficient numeric data
- Check for missing values
- Verify data types

### Getting Help

- Check the test suite for usage examples
- Review the sample data formats
- Examine the configuration options
- Look at the browser console for JavaScript errors

## 🔄 Updates and Maintenance

### Regular Tasks
- Update Python dependencies
- Review and update sample data
- Monitor system performance
- Back up recommendation history
- Update ML models with new data

### Version History
- v1.0.0: Initial release with core features
- Future releases will include enhanced ML models and additional data sources

---

**Built with ❤️ using Flask, scikit-learn, and modern web technologies**


