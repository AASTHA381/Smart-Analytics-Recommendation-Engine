import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import json

class DataAnalyzer:
    """
    Data analysis utilities for business intelligence
    """
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=2)
        
    def analyze(self, data):
        """Perform comprehensive data analysis"""
        if isinstance(data, dict):
            # Convert dict to DataFrame if needed
            df = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            df = data
        else:
            raise ValueError("Data must be a dictionary or DataFrame")
        
        analysis_results = {
            'basic_stats': self.basic_statistics(df),
            'correlation_analysis': self.correlation_analysis(df),
            'distribution_analysis': self.distribution_analysis(df),
            'outlier_detection': self.detect_outliers(df),
            'clustering_analysis': self.clustering_analysis(df)
        }
        
        return analysis_results
    
    def basic_statistics(self, df):
        """Generate basic statistical summary"""
        try:
            numeric_df = df.select_dtypes(include=[np.number])
            if numeric_df.empty:
                return {'message': 'No numeric columns found for statistical analysis'}
            
            stats = {
                'shape': df.shape,
                'numeric_columns': len(numeric_df.columns),
                'missing_values': df.isnull().sum().to_dict(),
                'summary_stats': numeric_df.describe().to_dict()
            }
            return stats
        except Exception as e:
            return {'error': f'Error in basic statistics: {e}'}
    
    def correlation_analysis(self, df):
        """Analyze correlations between numeric variables"""
        try:
            numeric_df = df.select_dtypes(include=[np.number])
            if len(numeric_df.columns) < 2:
                return {'message': 'Insufficient numeric columns for correlation analysis'}
            
            correlation_matrix = numeric_df.corr()
            
            # Find strong correlations
            strong_correlations = []
            for i in range(len(correlation_matrix.columns)):
                for j in range(i+1, len(correlation_matrix.columns)):
                    corr_value = correlation_matrix.iloc[i, j]
                    if abs(corr_value) > 0.7:  # Strong correlation threshold
                        strong_correlations.append({
                            'var1': correlation_matrix.columns[i],
                            'var2': correlation_matrix.columns[j],
                            'correlation': round(corr_value, 3)
                        })
            
            return {
                'correlation_matrix': correlation_matrix.to_dict(),
                'strong_correlations': strong_correlations
            }
        except Exception as e:
            return {'error': f'Error in correlation analysis: {e}'}
    
    def distribution_analysis(self, df):
        """Analyze distribution of numeric variables"""
        try:
            numeric_df = df.select_dtypes(include=[np.number])
            if numeric_df.empty:
                return {'message': 'No numeric columns found for distribution analysis'}
            
            distribution_stats = {}
            for column in numeric_df.columns:
                data = numeric_df[column].dropna()
                distribution_stats[column] = {
                    'mean': float(data.mean()),
                    'median': float(data.median()),
                    'std': float(data.std()),
                    'skewness': float(data.skew()),
                    'kurtosis': float(data.kurtosis())
                }
            
            return distribution_stats
        except Exception as e:
            return {'error': f'Error in distribution analysis: {e}'}
    
    def detect_outliers(self, df):
        """Detect outliers using IQR method"""
        try:
            numeric_df = df.select_dtypes(include=[np.number])
            if numeric_df.empty:
                return {'message': 'No numeric columns found for outlier detection'}
            
            outliers = {}
            for column in numeric_df.columns:
                data = numeric_df[column].dropna()
                Q1 = data.quantile(0.25)
                Q3 = data.quantile(0.75)
                IQR = Q3 - Q1
                
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                column_outliers = data[(data < lower_bound) | (data > upper_bound)]
                outliers[column] = {
                    'count': len(column_outliers),
                    'percentage': round((len(column_outliers) / len(data)) * 100, 2),
                    'values': column_outliers.tolist()[:10]  # Limit to first 10 outliers
                }
            
            return outliers
        except Exception as e:
            return {'error': f'Error in outlier detection: {e}'}
    
    def clustering_analysis(self, df):
        """Perform clustering analysis on numeric data"""
        try:
            numeric_df = df.select_dtypes(include=[np.number])
            if len(numeric_df.columns) < 2:
                return {'message': 'Insufficient numeric columns for clustering analysis'}
            
            # Prepare data
            data_clean = numeric_df.dropna()
            if len(data_clean) < 3:
                return {'message': 'Insufficient data points for clustering'}
            
            # Scale data
            scaled_data = self.scaler.fit_transform(data_clean)
            
            # Determine optimal number of clusters (up to 5)
            max_clusters = min(5, len(data_clean) - 1)
            inertias = []
            
            for k in range(1, max_clusters + 1):
                kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
                kmeans.fit(scaled_data)
                inertias.append(kmeans.inertia_)
            
            # Use elbow method to find optimal clusters
            optimal_clusters = 3 if max_clusters >= 3 else 2
            
            # Perform final clustering
            kmeans = KMeans(n_clusters=optimal_clusters, random_state=42, n_init=10)
            cluster_labels = kmeans.fit_predict(scaled_data)
            
            # Calculate cluster statistics
            cluster_stats = {}
            for cluster in range(optimal_clusters):
                cluster_data = data_clean[cluster_labels == cluster]
                cluster_stats[f'Cluster_{cluster}'] = {
                    'size': len(cluster_data),
                    'percentage': round((len(cluster_data) / len(data_clean)) * 100, 2),
                    'mean_values': cluster_data.mean().to_dict()
                }
            
            return {
                'optimal_clusters': optimal_clusters,
                'cluster_stats': cluster_stats,
                'inertias': inertias
            }
        except Exception as e:
            return {'error': f'Error in clustering analysis: {e}'}
    
    def generate_insights(self, analysis_results):
        """Generate business insights from analysis results"""
        insights = []
        
        try:
            # Basic stats insights
            if 'basic_stats' in analysis_results:
                stats = analysis_results['basic_stats']
                if 'shape' in stats:
                    insights.append(f"Dataset contains {stats['shape'][0]} records and {stats['shape'][1]} features")
            
            # Correlation insights
            if 'correlation_analysis' in analysis_results:
                corr_data = analysis_results['correlation_analysis']
                if 'strong_correlations' in corr_data and corr_data['strong_correlations']:
                    insights.append(f"Found {len(corr_data['strong_correlations'])} strong correlations in the data")
            
            # Outlier insights
            if 'outlier_detection' in analysis_results:
                outlier_data = analysis_results['outlier_detection']
                total_outliers = sum([info['count'] for info in outlier_data.values() if isinstance(info, dict) and 'count' in info])
                if total_outliers > 0:
                    insights.append(f"Detected {total_outliers} outliers across all numeric variables")
            
            # Clustering insights
            if 'clustering_analysis' in analysis_results:
                cluster_data = analysis_results['clustering_analysis']
                if 'optimal_clusters' in cluster_data:
                    insights.append(f"Data naturally groups into {cluster_data['optimal_clusters']} distinct clusters")
            
            return insights
        except Exception as e:
            return [f"Error generating insights: {e}"]
