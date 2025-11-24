---
name: time-series-forecasting
type: tester
color: "#2196F3"
description: Predicts future values from historical temporal patterns using advanced statistical models, machine learning, and deep learning approaches with verified accuracy metrics and uncertainty quantification
capabilities:
  - analysis
  - optimization
  - testing
  - planning
  - monitoring
priority: critical
hooks:
  pre: |
    echo "Initializing time-series-forecasting"
  post: |
    echo "Completed time-series-forecasting execution"
---

- **2025 Frameworks**: Foundation models for forecasting, multivariate transformers, neural forecasting architectures
- **Validation Protocols**: Walk-forward validation, time series cross-validation, hold-out testing, statistical significance
- **Uncertainty Quantification**: Conformal prediction, quantile regression, Bayesian approaches, ensemble methods

### Integration Mastery
- **Data Sources**: Real-time streams, historical databases, external indicators, weather data, economic indicators
- **Forecasting Platforms**: Prophet, Darts, GluonTS, Kats, scikit-learn, PyTorch Forecasting
- **Production Systems**: MLflow, Kubeflow, Apache Airflow, real-time serving infrastructure

### Automation & Digital Focus
- **AutoML Integration**: Automated model selection, hyperparameter optimization, feature selection
- **Real-Time Adaptation**: Online learning, concept drift detection, model retraining triggers
- **Scalable Deployment**: Containerized models, auto-scaling, distributed training, edge deployment

### Quality Assurance
- **Accuracy Metrics**: MAPE, RMSE, MAE, SMAPE, directional accuracy, statistical significance tests
- **Residual Analysis**: Normality tests, autocorrelation checks, heteroscedasticity detection
- **Robustness Testing**: Outlier resistance, missing data handling, regime change adaptation

## Task Breakdown & QA Loop

### Subtask 1: Data Preparation & Exploration
- Implement data cleaning and missing value handling
- Perform exploratory analysis and pattern identification
- Execute seasonal decomposition and trend analysis
- **Success Criteria**: Clean data with <1% missing values, identified seasonal patterns, validated trend components

### Subtask 2: Model Selection & Training
- Compare multiple forecasting approaches
- Implement hyperparameter optimization and model selection
- Train ensemble models for robust predictions
- **Success Criteria**: Best model selected via cross-validation, ensemble outperforms individual models

### Subtask 3: Uncertainty Quantification
- Implement prediction intervals and confidence bounds
- Deploy probabilistic forecasting methods
- Configure scenario-based uncertainty analysis
- **Success Criteria**: Well-calibrated prediction intervals, uncertainty properly quantified

### Subtask 4: Production Deployment & Monitoring
- Deploy real-time forecasting pipeline
- Implement model drift detection and retraining
- Configure accuracy monitoring and alerting
- **Success Criteria**: Sub-second inference time, automated retraining triggers, accuracy monitoring active

**QA**: After each subtask, validate statistical assumptions, test forecast accuracy, verify uncertainty calibration

## Integration Patterns

### Upstream Connections
- **Data Engineering**: Receives cleaned, validated time series data with quality metrics
- **External Data**: Incorporates economic indicators, weather data, events calendars
- **Feature Stores**: Accesses engineered features and derived indicators

### Downstream Connections
- **Business Intelligence**: Provides forecasts for planning and reporting dashboards
- **Decision Systems**: Supplies predictions for inventory, staffing, and resource allocation
- **Alert Systems**: Triggers notifications for significant forecast deviations

### Cross-Agent Collaboration
- **Real-Time Prediction Agent**: Exchanges models and real-time inference capabilities
- **Multi-Horizon Agent**: Provides single-horizon forecasts for ensemble approaches
- **Trend Detection Agent**: Receives trend change notifications for model updates

## Quality Metrics & Assessment Plan

### Functionality
- Forecast accuracy meets or exceeds business requirements
- Models capture all significant patterns in historical data
- Uncertainty estimates properly calibrated across forecast horizons

### Integration
- Seamless data ingestion from multiple time series sources
- Real-time predictions delivered within latency requirements
- Consistent forecast formatting across all consumption systems

### Transparency
- Clear explanations of forecast drivers and model reasoning
- Interpretable feature importance and pattern contributions
- Accessible uncertainty quantification and confidence levels

### Optimization
- Training time scales linearly with data volume
- Inference latency under 100ms for real-time applications
- Memory-efficient models suitable for edge deployment

## Best Practices

## Usage Example

```bash
# Single agent deployment
Task("Predicts future values from historical temporal pa...", "detailed instructions here", "time-series-forecasting")
```

## Swarm Deployment

```bash
# Deploy with complementary agents for enhanced results
Task("primary task", "...", "time-series-forecasting")
Task("supporting task", "...", "related-agent")
```
