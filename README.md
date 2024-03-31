## Expedia Analytics

### Objective

The purpose of the ExpediaAnalytics project is to analyze and visualize hotel price trends and dynamics within the tourism sector, leveraging the Expedia Hotel Dataset. Through an end-to-end data pipeline, this project aims to provide insights into hotel pricing strategies, demand fluctuations, and market competitiveness.

### Table of Contents

- [Objective](#objective)
- [Architecture](#architecture)
- [Technologies and Tools](#Technologies-and-tools)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

### Architecture

[Diagram to be added]

The project architecture encompasses the following components:

- Data ingestion from Kaggle to Google Cloud Storage (GCS) as the data lake.
- Data processing and transformation using dbt in BigQuery.
- Workflow orchestration with Mage to manage the data pipeline.
- Visualization of insights through a dashboard in Google Looker Studio.

### Technologies and Tools

This project utilizes a range of technologies and tools, including:

- **Google Cloud Platform (GCP)** for cloud storage, data warehousing, and computing resources.
- **Google Cloud Storage (GCS)** as the data lake for raw data storage.
- **BigQuery** for data warehousing and SQL-based transformations.
- **dbt (Data Build Tool)** for data transformation within BigQuery.
- **Mage** for workflow orchestration across the data pipeline.
- **Google Looker Studio** for dashboard creation and data visualization.
- **Pipenv** for Python dependency management and virtual environment creation.

### Installation

To get started with the ExpediaAnalytics project, follow these steps:

1. Clone the repository.
2. Install dependencies using Pipenv:
   ```shell
   pipenv install
   ```
   Note: This step will be updated with specific dependencies as the project progresses.
3. Set up a GCP project and configure GCS and BigQuery services according to your setup.

### Usage

This section will be updated with detailed instructions on running the data pipeline, executing dbt models, orchestrating workflows with Mage, and accessing the dashboard in Google Looker Studio. Steps will include:

- Data ingestion commands or scripts.
- dbt run commands for data transformation.
- Mage setup and execution steps.
- Instructions to access and interact with the Looker Studio dashboard.

### Dashboard

[Dashboard to be added]

### License

This project is licensed under the [MIT License](LICENSE).
