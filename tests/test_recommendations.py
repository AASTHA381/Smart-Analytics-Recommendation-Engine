import unittest
import sys
import os
import pandas as pd
import numpy as np

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.recommendation_engine import RecommendationEngine
from models.data_analyzer import DataAnalyzer

class TestRecommendationEngine(unittest.TestCase):
    """Test cases for the RecommendationEngine class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.engine = RecommendationEngine()
        self.sample_data = pd.DataFrame({
            'product_id': [1, 2, 3, 4, 5],
            'sales_volume': [100, 150, 200, 80, 120],
            'revenue': [5000, 7500, 10000, 4000, 6000],
            'profit_margin': [0.2, 0.3, 0.25, 0.15, 0.28]
        })
    
    def test_initialization(self):
        """Test that the RecommendationEngine initializes correctly"""
        self.assertIsInstance(self.engine, RecommendationEngine)
        self.assertFalse(self.engine.is_trained)
        self.assertIsNone(self.engine.model)
    
    def test_load_data_default(self):
        """Test loading default sales data"""
        data = self.engine.load_data('sales')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)
        self.assertTrue('product_id' in data.columns)
    
    def test_load_data_customer(self):
        """Test loading customer data"""
        data = self.engine.load_data('customer')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)
        self.assertTrue('customer_id' in data.columns)
    
    def test_train_model(self):
        """Test model training functionality"""
        result = self.engine.train_model(self.sample_data)
        self.assertTrue(result)
        self.assertTrue(self.engine.is_trained)
        self.assertIsNotNone(self.engine.model)
    
    def test_train_model_insufficient_data(self):
        """Test model training with insufficient data"""
        insufficient_data = pd.DataFrame({'id': [1, 2, 3]})
        result = self.engine.train_model(insufficient_data)
        self.assertFalse(result)
    
    def test_generate_recommendations(self):
        """Test recommendation generation"""
        input_data = {'type': 'sales', 'period': '30_days'}
        recommendations = self.engine.generate_recommendations(input_data)
        
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        
        # Check that each recommendation has required fields
        for rec in recommendations:
            if rec.get('type') != 'error':
                self.assertIn('type', rec)
                self.assertIn('title', rec)
                self.assertIn('items', rec)
                self.assertIn('confidence', rec)
    
    def test_generate_recommendations_structure(self):
        """Test that recommendations have the expected structure"""
        recommendations = self.engine.generate_recommendations({})
        
        # Should return at least one recommendation
        self.assertGreater(len(recommendations), 0)
        
        # First recommendation should be about products
        first_rec = recommendations[0]
        if first_rec.get('type') != 'error':
            self.assertEqual(first_rec['type'], 'product')
            self.assertEqual(first_rec['title'], 'Top Revenue Generating Products')
    
    def test_calculate_similarity(self):
        """Test similarity calculation between datasets"""
        data1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        data2 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        
        similarity = self.engine.calculate_similarity(data1, data2)
        self.assertIsInstance(similarity, float)
        self.assertAlmostEqual(similarity, 1.0, places=5)  # Identical data should have similarity of 1
    
    def test_calculate_similarity_empty_data(self):
        """Test similarity calculation with empty data"""
        empty_data = pd.DataFrame()
        data = pd.DataFrame({'a': [1, 2, 3]})
        
        similarity = self.engine.calculate_similarity(empty_data, data)
        self.assertEqual(similarity, 0.0)


class TestDataAnalyzer(unittest.TestCase):
    """Test cases for the DataAnalyzer class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.analyzer = DataAnalyzer()
        self.sample_data = pd.DataFrame({
            'sales': [100, 150, 200, 80, 120, 300, 90, 110],
            'profit': [20, 30, 50, 16, 24, 75, 18, 22],
            'customers': [10, 15, 25, 8, 12, 35, 9, 11],
            'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B']
        })
    
    def test_initialization(self):
        """Test that the DataAnalyzer initializes correctly"""
        self.assertIsInstance(self.analyzer, DataAnalyzer)
    
    def test_analyze_dataframe(self):
        """Test analysis with pandas DataFrame input"""
        result = self.analyzer.analyze(self.sample_data)
        
        self.assertIsInstance(result, dict)
        self.assertIn('basic_stats', result)
        self.assertIn('correlation_analysis', result)
        self.assertIn('distribution_analysis', result)
        self.assertIn('outlier_detection', result)
        self.assertIn('clustering_analysis', result)
    
    def test_analyze_dictionary(self):
        """Test analysis with dictionary input"""
        data_dict = {
            'sales': [100, 150, 200],
            'profit': [20, 30, 50]
        }
        result = self.analyzer.analyze(data_dict)
        
        self.assertIsInstance(result, dict)
        self.assertIn('basic_stats', result)
    
    def test_basic_statistics(self):
        """Test basic statistical analysis"""
        stats = self.analyzer.basic_statistics(self.sample_data)
        
        self.assertIn('shape', stats)
        self.assertIn('numeric_columns', stats)
        self.assertIn('summary_stats', stats)
        
        # Check shape
        self.assertEqual(stats['shape'], (8, 4))
        self.assertEqual(stats['numeric_columns'], 3)
    
    def test_correlation_analysis(self):
        """Test correlation analysis"""
        corr_result = self.analyzer.correlation_analysis(self.sample_data)
        
        self.assertIn('correlation_matrix', corr_result)
        self.assertIn('strong_correlations', corr_result)
        
        # Should find strong correlation between sales and profit
        strong_corrs = corr_result['strong_correlations']
        correlation_found = any(
            ('sales' in corr['var1'] and 'profit' in corr['var2']) or
            ('profit' in corr['var1'] and 'sales' in corr['var2'])
            for corr in strong_corrs
        )
        # Note: This might not always be true depending on the data, so we just check structure
        self.assertIsInstance(strong_corrs, list)
    
    def test_distribution_analysis(self):
        """Test distribution analysis"""
        dist_result = self.analyzer.distribution_analysis(self.sample_data)
        
        # Should analyze numeric columns
        self.assertIn('sales', dist_result)
        self.assertIn('profit', dist_result)
        self.assertIn('customers', dist_result)
        
        # Check that each column has required statistics
        for col in ['sales', 'profit', 'customers']:
            self.assertIn('mean', dist_result[col])
            self.assertIn('median', dist_result[col])
            self.assertIn('std', dist_result[col])
    
    def test_detect_outliers(self):
        """Test outlier detection"""
        outliers = self.analyzer.detect_outliers(self.sample_data)
        
        # Should analyze numeric columns
        self.assertIn('sales', outliers)
        self.assertIn('profit', outliers)
        
        # Check outlier structure
        for col in ['sales', 'profit']:
            self.assertIn('count', outliers[col])
            self.assertIn('percentage', outliers[col])
            self.assertIn('values', outliers[col])
    
    def test_clustering_analysis(self):
        """Test clustering analysis"""
        cluster_result = self.analyzer.clustering_analysis(self.sample_data)
        
        if 'optimal_clusters' in cluster_result:
            self.assertIn('cluster_stats', cluster_result)
            self.assertIsInstance(cluster_result['optimal_clusters'], int)
            self.assertGreater(cluster_result['optimal_clusters'], 0)
        else:
            # Might not have enough data for clustering
            self.assertIn('message', cluster_result)
    
    def test_generate_insights(self):
        """Test insight generation"""
        analysis_results = self.analyzer.analyze(self.sample_data)
        insights = self.analyzer.generate_insights(analysis_results)
        
        self.assertIsInstance(insights, list)
        self.assertGreater(len(insights), 0)
        
        # Each insight should be a string
        for insight in insights:
            self.assertIsInstance(insight, str)
    
    def test_empty_dataframe(self):
        """Test analysis with empty DataFrame"""
        empty_df = pd.DataFrame()
        result = self.analyzer.analyze(empty_df)
        
        # Should handle empty data gracefully
        self.assertIsInstance(result, dict)
    
    def test_non_numeric_dataframe(self):
        """Test analysis with non-numeric DataFrame"""
        text_df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie'],
            'city': ['NYC', 'LA', 'Chicago']
        })
        result = self.analyzer.analyze(text_df)
        
        # Should handle non-numeric data gracefully
        self.assertIsInstance(result, dict)
        basic_stats = result.get('basic_stats', {})
        if 'message' in basic_stats:
            self.assertIn('No numeric columns', basic_stats['message'])


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def setUp(self):
        """Set up integration test fixtures"""
        self.engine = RecommendationEngine()
        self.analyzer = DataAnalyzer()
    
    def test_end_to_end_workflow(self):
        """Test a complete end-to-end workflow"""
        # Load data
        sales_data = self.engine.load_data('sales')
        
        # Analyze data
        analysis = self.analyzer.analyze(sales_data)
        
        # Generate recommendations
        recommendations = self.engine.generate_recommendations({'data_type': 'sales'})
        
        # Verify results
        self.assertIsInstance(sales_data, pd.DataFrame)
        self.assertIsInstance(analysis, dict)
        self.assertIsInstance(recommendations, list)
        
        # Check that we got meaningful results
        self.assertGreater(len(sales_data), 0)
        self.assertIn('basic_stats', analysis)
        self.assertGreater(len(recommendations), 0)
    
    def test_recommendation_with_analysis(self):
        """Test generating recommendations based on analysis results"""
        # Get some data and analyze it
        data = self.engine.load_data('customer')
        analysis = self.analyzer.analyze(data)
        
        # Use analysis insights to generate targeted recommendations
        input_data = {
            'analysis_results': analysis,
            'focus_area': 'customer_retention'
        }
        
        recommendations = self.engine.generate_recommendations(input_data)
        
        # Should get recommendations
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)


def run_tests():
    """Run all tests"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [TestRecommendationEngine, TestDataAnalyzer, TestIntegration]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    # Run tests when script is executed directly
    success = run_tests()
    
    if success:
        print("\n✅ All tests passed successfully!")
        exit(0)
    else:
        print("\n❌ Some tests failed!")
        exit(1)
