import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import pickle
import os
from config import Config

class RecommendationEngine:
    """
    Core ML recommendation engine for generating business recommendations
    """
    
    def __init__(self):
        self.config = Config()
        self.model = None
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def load_data(self, data_type='sales'):
        """Load sample data based on type"""
        data_files = {
            'sales': 'sample_sales_data.csv',
            'customer': 'sample_customer_data.csv',
            'marketing': 'sample_marketing_data.csv',
            'operations': 'sample_operations_data.csv'
        }
        
        file_path = self.config.DATA_DIR / data_files.get(data_type, 'sample_sales_data.csv')
        
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            # Return sample data if file doesn't exist
            return self._generate_sample_data(data_type)
    
    def _generate_sample_data(self, data_type):
        """Generate sample data for demonstration"""
        np.random.seed(42)
        
        if data_type == 'sales':
            return pd.DataFrame({
                'product_id': range(1, 101),
                'sales_volume': np.random.randint(10, 1000, 100),
                'revenue': np.random.uniform(100, 10000, 100),
                'profit_margin': np.random.uniform(0.1, 0.5, 100)
            })
        elif data_type == 'customer':
            return pd.DataFrame({
                'customer_id': range(1, 201),
                'age': np.random.randint(18, 80, 200),
                'purchase_frequency': np.random.randint(1, 50, 200),
                'total_spent': np.random.uniform(50, 5000, 200)
            })
        else:
            return pd.DataFrame({
                'id': range(1, 51),
                'value': np.random.uniform(0, 100, 50),
                'category': np.random.choice(['A', 'B', 'C'], 50)
            })
    
    def train_model(self, data):
        """Train the recommendation model"""
        try:
            # Prepare features and target
            features = data.select_dtypes(include=[np.number]).drop(columns=['id'], errors='ignore')
            if len(features.columns) < 2:
                raise ValueError("Insufficient numerical features for training")
            
            X = features.iloc[:, :-1]  # All columns except last as features
            y = features.iloc[:, -1]   # Last column as target
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            # Train model
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_scaled, y)
            self.is_trained = True
            
            return True
        except Exception as e:
            print(f"Error training model: {e}")
            return False
    
    def generate_recommendations(self, input_data):
        """Generate recommendations based on input data"""
        try:
            # Load and prepare data
            sales_data = self.load_data('sales')
            customer_data = self.load_data('customer')
            
            # Train model if not already trained
            if not self.is_trained:
                self.train_model(sales_data)
            
            # Generate recommendations based on patterns in data
            recommendations = []
            
            # Product recommendations
            top_products = sales_data.nlargest(5, 'revenue')['product_id'].tolist()
            recommendations.append({
                'type': 'product',
                'title': 'Top Revenue Generating Products',
                'items': [f"Product {pid}" for pid in top_products],
                'confidence': 0.85
            })
            
            # Customer segment recommendations
            high_value_customers = customer_data.nlargest(5, 'total_spent')['customer_id'].tolist()
            recommendations.append({
                'type': 'customer',
                'title': 'High Value Customers to Focus On',
                'items': [f"Customer {cid}" for cid in high_value_customers],
                'confidence': 0.78
            })
            
            # Business insights
            avg_margin = sales_data['profit_margin'].mean()
            recommendations.append({
                'type': 'insight',
                'title': 'Business Insights',
                'items': [
                    f"Average profit margin: {avg_margin:.2%}",
                    "Consider focusing on high-margin products",
                    "Implement customer retention strategies"
                ],
                'confidence': 0.92
            })
            
            return recommendations[:self.config.RECOMMENDATION_LIMIT]
            
        except Exception as e:
            return [{'type': 'error', 'message': f'Error generating recommendations: {e}'}]
    
    def calculate_similarity(self, data1, data2):
        """Calculate similarity between datasets"""
        try:
            # Ensure both datasets have numerical data
            num_data1 = data1.select_dtypes(include=[np.number])
            num_data2 = data2.select_dtypes(include=[np.number])
            
            if num_data1.empty or num_data2.empty:
                return 0.0
            
            # Calculate cosine similarity
            similarity = cosine_similarity(
                num_data1.mean().values.reshape(1, -1),
                num_data2.mean().values.reshape(1, -1)
            )
            return float(similarity[0][0])
            
        except Exception as e:
            print(f"Error calculating similarity: {e}")
            return 0.0
