// Main JavaScript functionality for the PR application

class PRApp {
    constructor() {
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadInitialData();
    }

    bindEvents() {
        // Recommendation button handler
        const recommendationBtn = document.getElementById('get-recommendations');
        if (recommendationBtn) {
            recommendationBtn.addEventListener('click', () => this.getRecommendations());
        }

        // Analysis button handler
        const analysisBtn = document.getElementById('run-analysis');
        if (analysisBtn) {
            analysisBtn.addEventListener('click', () => this.runAnalysis());
        }

        // File upload handler
        const fileInput = document.getElementById('data-file');
        if (fileInput) {
            fileInput.addEventListener('change', (e) => this.handleFileUpload(e));
        }

        // Navigation handlers
        this.bindNavigationEvents();
    }

    bindNavigationEvents() {
        const navLinks = document.querySelectorAll('nav a');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                // Remove active class from all links
                navLinks.forEach(l => l.classList.remove('active'));
                // Add active class to clicked link
                e.target.classList.add('active');
            });
        });
    }

    async loadInitialData() {
        try {
            this.showLoading('Loading initial data...');
            
            // Load dashboard metrics
            await this.loadDashboardMetrics();
            
            this.hideLoading();
        } catch (error) {
            console.error('Error loading initial data:', error);
            this.showAlert('Error loading initial data', 'danger');
            this.hideLoading();
        }
    }

    async loadDashboardMetrics() {
        // Simulate loading dashboard metrics
        const metrics = {
            totalSales: 125000,
            totalCustomers: 1250,
            avgOrderValue: 85.50,
            conversionRate: 3.2
        };

        this.updateMetricCards(metrics);
    }

    updateMetricCards(metrics) {
        const metricElements = {
            'total-sales': metrics.totalSales.toLocaleString(),
            'total-customers': metrics.totalCustomers.toLocaleString(),
            'avg-order-value': `$${metrics.avgOrderValue.toFixed(2)}`,
            'conversion-rate': `${metrics.conversionRate}%`
        };

        Object.entries(metricElements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
                this.animateValue(element, value);
            }
        });
    }

    animateValue(element, finalValue) {
        // Simple animation for metric values
        element.style.transform = 'scale(1.1)';
        element.style.transition = 'transform 0.3s ease';
        
        setTimeout(() => {
            element.style.transform = 'scale(1)';
        }, 300);
    }

    async getRecommendations() {
        try {
            this.showLoading('Generating recommendations...');
            
            const response = await fetch('/api/recommendations', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    type: 'general',
                    data: this.getCurrentData()
                })
            });

            const result = await response.json();
            
            if (result.success) {
                this.displayRecommendations(result.recommendations);
                this.showAlert('Recommendations generated successfully!', 'success');
            } else {
                throw new Error(result.error || 'Failed to generate recommendations');
            }
            
        } catch (error) {
            console.error('Error getting recommendations:', error);
            this.showAlert('Error generating recommendations: ' + error.message, 'danger');
        } finally {
            this.hideLoading();
        }
    }

    async runAnalysis() {
        try {
            this.showLoading('Running data analysis...');
            
            const response = await fetch('/api/analysis', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    data: this.getCurrentData(),
                    analysis_type: 'comprehensive'
                })
            });

            const result = await response.json();
            
            if (result.success) {
                this.displayAnalysis(result.analysis);
                this.showAlert('Analysis completed successfully!', 'success');
            } else {
                throw new Error(result.error || 'Failed to run analysis');
            }
            
        } catch (error) {
            console.error('Error running analysis:', error);
            this.showAlert('Error running analysis: ' + error.message, 'danger');
        } finally {
            this.hideLoading();
        }
    }

    getCurrentData() {
        // Get current form data or return sample data
        return {
            sales_data: [
                { product: 'Product A', sales: 1000, revenue: 50000 },
                { product: 'Product B', sales: 800, revenue: 40000 },
                { product: 'Product C', sales: 600, revenue: 30000 }
            ],
            time_period: '30_days'
        };
    }

    displayRecommendations(recommendations) {
        const container = document.getElementById('recommendations-container');
        if (!container) return;

        container.innerHTML = '';

        recommendations.forEach((rec, index) => {
            const recElement = this.createRecommendationCard(rec, index);
            container.appendChild(recElement);
        });
    }

    createRecommendationCard(recommendation, index) {
        const card = document.createElement('div');
        card.className = 'card recommendation-card';
        card.style.animationDelay = `${index * 0.1}s`;
        
        let itemsHtml = '';
        if (recommendation.items && Array.isArray(recommendation.items)) {
            itemsHtml = recommendation.items.map(item => `<li>${item}</li>`).join('');
        }

        card.innerHTML = `
            <div class="recommendation-header">
                <h3>${recommendation.title || 'Recommendation'}</h3>
                ${recommendation.confidence ? `<span class="confidence">Confidence: ${(recommendation.confidence * 100).toFixed(1)}%</span>` : ''}
            </div>
            <div class="recommendation-type">
                <span class="status status-info">${recommendation.type || 'General'}</span>
            </div>
            ${itemsHtml ? `<ul class="recommendation-items">${itemsHtml}</ul>` : ''}
            <div class="recommendation-actions">
                <button class="btn btn-sm" onclick="app.implementRecommendation(${index})">Implement</button>
                <button class="btn btn-secondary btn-sm" onclick="app.saveRecommendation(${index})">Save for Later</button>
            </div>
        `;

        return card;
    }

    displayAnalysis(analysis) {
        const container = document.getElementById('analysis-container');
        if (!container) return;

        container.innerHTML = this.createAnalysisHTML(analysis);
    }

    createAnalysisHTML(analysis) {
        let html = '<div class="analysis-results">';
        
        // Basic Statistics
        if (analysis.basic_stats) {
            html += this.createBasicStatsHTML(analysis.basic_stats);
        }
        
        // Correlation Analysis
        if (analysis.correlation_analysis) {
            html += this.createCorrelationHTML(analysis.correlation_analysis);
        }
        
        // Outlier Detection
        if (analysis.outlier_detection) {
            html += this.createOutlierHTML(analysis.outlier_detection);
        }
        
        // Clustering Analysis
        if (analysis.clustering_analysis) {
            html += this.createClusteringHTML(analysis.clustering_analysis);
        }
        
        html += '</div>';
        return html;
    }

    createBasicStatsHTML(stats) {
        return `
            <div class="card">
                <h3>Basic Statistics</h3>
                <div class="grid grid-2">
                    <div class="metric-card">
                        <div class="metric-value">${stats.shape ? stats.shape[0] : 'N/A'}</div>
                        <div class="metric-label">Total Records</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">${stats.numeric_columns || 'N/A'}</div>
                        <div class="metric-label">Numeric Columns</div>
                    </div>
                </div>
            </div>
        `;
    }

    createCorrelationHTML(correlation) {
        let html = '<div class="card"><h3>Correlation Analysis</h3>';
        
        if (correlation.strong_correlations && correlation.strong_correlations.length > 0) {
            html += '<h4>Strong Correlations Found:</h4><ul>';
            correlation.strong_correlations.forEach(corr => {
                html += `<li>${corr.var1} ↔ ${corr.var2}: ${corr.correlation}</li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>No strong correlations found.</p>';
        }
        
        html += '</div>';
        return html;
    }

    createOutlierHTML(outliers) {
        let html = '<div class="card"><h3>Outlier Detection</h3>';
        
        const outlierEntries = Object.entries(outliers).filter(([key, value]) => 
            typeof value === 'object' && value.count !== undefined
        );
        
        if (outlierEntries.length > 0) {
            html += '<div class="grid grid-2">';
            outlierEntries.forEach(([column, info]) => {
                html += `
                    <div class="metric-card">
                        <div class="metric-value">${info.count}</div>
                        <div class="metric-label">${column} Outliers (${info.percentage}%)</div>
                    </div>
                `;
            });
            html += '</div>';
        } else {
            html += '<p>No outliers detected.</p>';
        }
        
        html += '</div>';
        return html;
    }

    createClusteringHTML(clustering) {
        let html = '<div class="card"><h3>Clustering Analysis</h3>';
        
        if (clustering.optimal_clusters) {
            html += `<p>Data naturally groups into <strong>${clustering.optimal_clusters}</strong> clusters.</p>`;
            
            if (clustering.cluster_stats) {
                html += '<h4>Cluster Distribution:</h4><div class="grid grid-3">';
                Object.entries(clustering.cluster_stats).forEach(([cluster, stats]) => {
                    html += `
                        <div class="metric-card">
                            <div class="metric-value">${stats.size}</div>
                            <div class="metric-label">${cluster} (${stats.percentage}%)</div>
                        </div>
                    `;
                });
                html += '</div>';
            }
        }
        
        html += '</div>';
        return html;
    }

    handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        this.showLoading('Uploading file...');
        
        // Simulate file processing
        setTimeout(() => {
            this.showAlert(`File "${file.name}" uploaded successfully!`, 'success');
            this.hideLoading();
        }, 2000);
    }

    implementRecommendation(index) {
        this.showAlert(`Implementing recommendation ${index + 1}...`, 'info');
        // Add implementation logic here
    }

    saveRecommendation(index) {
        this.showAlert(`Recommendation ${index + 1} saved for later!`, 'success');
        // Add save logic here
    }

    showLoading(message = 'Loading...') {
        const loadingElement = document.getElementById('loading');
        const loadingMessage = document.getElementById('loading-message');
        
        if (loadingElement) {
            loadingElement.style.display = 'flex';
            if (loadingMessage) {
                loadingMessage.textContent = message;
            }
        }
    }

    hideLoading() {
        const loadingElement = document.getElementById('loading');
        if (loadingElement) {
            loadingElement.style.display = 'none';
        }
    }

    showAlert(message, type = 'info') {
        const alertContainer = document.getElementById('alert-container') || document.body;
        
        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.innerHTML = `
            ${message}
            <button onclick="this.parentElement.remove()" style="float: right; background: none; border: none; font-size: 1.2rem; cursor: pointer;">&times;</button>
        `;
        
        alertContainer.appendChild(alert);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (alert.parentElement) {
                alert.remove();
            }
        }, 5000);
    }

    // Utility methods
    formatNumber(num) {
        return new Intl.NumberFormat().format(num);
    }

    formatCurrency(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(amount);
    }

    formatPercentage(value) {
        return `${(value * 100).toFixed(1)}%`;
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new PRApp();
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PRApp;
}
