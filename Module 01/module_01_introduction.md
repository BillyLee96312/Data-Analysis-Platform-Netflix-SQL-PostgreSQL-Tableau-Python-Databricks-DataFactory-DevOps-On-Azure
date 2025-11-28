# Sprint 1: Foundation & Infrastructure Setup (Weeks 1?2)

## Sprint Overview
This sprint sets up the cloud infrastructure and local tooling required to run the course "Data Analysis On Azure Databricks and Data Factory ? Pro Track" using the Netflix datasets. Students will provision resources, connect the environment, and validate end-to-end connectivity for a simple data pipeline.

## Goals
- Provision core Azure resources for labs (Databricks, Data Factory, Storage, PostgreSQL).
- Configure development tooling and credentials.
- Implement a working sample pipeline: raw data ¡æ Databricks processing ¡æ PostgreSQL / analytical store.
- Document resources, costs, and security constraints.

## Learning Objectives
- Learn to provision and configure Azure Databricks and Azure Data Factory.
- Understand storage architecture (bronze/silver/gold) and data ingestion patterns.
- Set up secure access with Azure AD service principals and managed identities.
- Create and run a simple ETL pipeline and validate results.

## Prerequisites
- Azure subscription (or a provided lab subscription).
- Basic Python and SQL knowledge.
- Kaggle / open data access to Netflix datasets (or instructor-provided sample).
- Local tools: Azure CLI, Databricks CLI (optional), Python 3.8+, Git.
- Optional: Tableau or Power BI for visualization.

## Deliverables (Sprint End)
- Deployed Azure resources: Resource Group, Storage Account, Databricks workspace, Data Factory, PostgreSQL instance (Azure Database for PostgreSQL).
- Working Databricks notebook that reads raw Netflix data from storage and writes processed data.
- A Data Factory pipeline that ingests raw files into storage or triggers Databricks job.
- README with infrastructure details and cost-minimization tips.
- Short demo recording (3?5 min) showing pipeline end-to-end and validation.

## Weekly Breakdown

Week 1 ? Foundation & Accounts
- Day 1?2:
    - Verify access to Azure subscription (or grant lab subscription).
    - Create resource group naming convention: e.g., rg-netflix-dataproc-xx.
    - Create a shared storage account with containers: raw, staging, processed (bronze/silver/gold).
    - Provision an Azure Database for PostgreSQL (Dev SKU).
- Day 3?5:
    - Create Azure Databricks workspace (default Standard plan) and a minimal cluster.
    - Install Databricks CLI and configure token OR set up Azure AD service principal and role assignments.
    - Prepare datasets: obtain Netflix CSV files (link to dataset or instructor copy).
    - Upload a sample dataset to storage/raw.

Week 2 ? Connectivity, Pipelines & Validation
- Day 6?8:
    - Configure Azure Data Factory (ADF) and create linked services to Blob Storage / ADLS, Databricks, PostgreSQL.
    - Create minimal ADF pipeline to copy raw data to staging or invoke Databricks notebook.
    - Create Databricks notebook to:
        - Read raw Netflix data
        - Execute simple transformations
        - Write results to PostgreSQL and to processed container
    - Configure networking and firewall rules for PostgreSQL and Databricks.
- Day 9?10:
    - Run end-to-end pipeline and validate data in PostgreSQL and processed storage.
    - Create brief documentation and demo video.
    - Add cleanup procedures and cost-control guidelines.

## Tasks & Checklist
- [ ] Provision resource group and storage account
- [ ] Create Databricks workspace and a cluster
- [ ] Set up Azure Database for PostgreSQL and create a test user/database
- [ ] Create Data Factory and link services
- [ ] Upload sample Netflix CSV and document schema
- [ ] Author and test a Databricks notebook for ETL
- [ ] Author and test an ADF pipeline to orchestrate
- [ ] Validate end-to-end flow and show data in PostgreSQL
- [ ] Submit README, resource inventory, and demonstration recording

---
## Expanded Sprint 1 Curriculum ? Modules & Next Steps
This section expands the Sprint 1 content into a step-by-step lab sequence with modules, chapter topics, learning outcomes, hands-on exercises, sample deliverables, and acceptance tests. Use the following as your guide for completing Sprint 1.

### Module 1.1 ? Intro & Environment Setup (Day 1?2)
- Learning outcomes:
    - Confirm Azure subscription access or lab sandbox.
    - Understand naming conventions and tagging policy for resources.
- Hands-on:
    - Create Resource Group and Storage Account with containers: `raw/`, `staging/`, `processed/`.
    - Install Azure CLI and Databricks CLI and configure an authenticated session.
- Deliverables:
    - Add a short environment README describing the resources and a CLI output screenshot.
- Acceptance tests:
    - `az group show` returns resource group details, and the storage account lists the `raw` container.

### Module 1.2 ? Storage & Data Ingestion (ADLS Gen2) (Day 2?3)
- Learning outcomes:
    - Implement Bronze/Silver/Gold data lake layout and storage ACLs.
    - Upload sample Netflix CSV files to ADLS Gen2.
- Hands-on:
    - Create a storage account configured for ADLS Gen2 (Hierarchical Namespace) and create the sample containers with example CSV in `raw/`.
- Deliverables:
    - Upload log or an `az` command snippet used to upload the sample dataset and a data schema doc.
- Acceptance tests:
    - The sample CSV exists in `raw/` when listing blobs.

### Module 1.3 ? Provision Azure PostgreSQL (Day 3)
- Learning outcomes:
    - Deploy Postgres instance and create a minimal database and user.
    - Secure credentials in Key Vault and configure firewall rules.
- Hands-on:
    - Provision a PostgreSQL instance and create a `analytics` database with a `netflix` schema and test user.
- Deliverables:
    - `postgresql_schema.sql` and a README on connection instructions (using Key Vault secrets).
- Acceptance tests:
    - DB connection succeeds from Databricks or local machine and schemata are present.

### Module 1.4 ? Databricks Workspace & Notebook (Day 3?5)
- Learning outcomes:
    - Create Databricks workspace and a minimal cluster; set auto-terminate.
    - Read CSV in notebook and write to ADLS and PostgreSQL via JDBC.
- Hands-on:
    - Upload a starter notebook and run it against the sample CSV; parameterize the inputs for environments.
- Deliverables:
    - `starter_notebook_read_transform_write.py` (parameterized PySpark notebook) and run logs/screenshots.
- Acceptance tests:
    - Notebook completes successfully and writes data to `processed/` container and PostgreSQL.

### Module 1.5 ? ADF Linked Services & Pipeline Orchestration (Day 6?8)
- Learning outcomes:
    - Configure linked services for ADLS Gen2, Databricks, and PostgreSQL.
    - Build a pipeline that either copies data between containers or triggers a Databricks notebook.
- Hands-on:
    - Create an ADF pipeline with a Copy Activity and a Databricks Notebook Activity; parameterize it.
- Deliverables:
    - ADF pipeline JSON export (`adf_pipeline_copy_and_invoke.json`) and run logs.
- Acceptance tests:
    - The pipeline run finishes with a success status and the target data is present.

### Module 1.6 ? Secrets, Security & Managed Identities (Day 7)
- Learning outcomes:
    - Use Key Vault with Databricks and ADF to manage secrets and credentials.
    - Apply least privilege and RBAC to service principals and identities.
- Hands-on:
    - Create a Key Vault, add secrets for DB credentials, and configure Key Vault access from Databricks and ADF.
    - Configure firewall rules and/or private endpoints for PostgreSQL.
- Deliverables:
    - A short document on security best practices used and screenshots of Key Vault integration.
- Acceptance tests:
    - Databricks and ADF services can read secrets from Key Vault; no secrets hard-coded in notebooks.

### Module 1.7 ? Cost Controls & Cleanup (Day 9?10)
- Learning outcomes:
    - Add budgets and alerts; set Databricks auto-terminate and use minimal SKUs.
    - Create cleanup scripts and tagging enforcement.
- Hands-on:
    - Configure budget alerts and a default tagging policy; implement an `az group delete` cleanup script.
- Deliverables:
    - A cost-control checklist, screenshots for budget alerts, and the cleanup script.
- Acceptance tests:
    - Alerts configured and tags exist on resources; cluster auto-terminate set to a low-timeout.

### Module 1.8 ? Optional: Azure DevOps CI/CD for IaC & Notebooks
- Learning outcomes:
    - Create a simple Azure DevOps pipeline to deploy IaC and deploy notebooks to Databricks via the CLI/API.
- Hands-on:
    - Generate a minimal `azure-pipelines.yml` that runs Terraform or ARM and uploads notebooks to the Databricks workspace.
- Deliverables:
    - `devops/azure-pipelines.yml`, Terraform/ARM skeletons, and a run log.
- Acceptance tests:
    - Pipeline successfully provisions or updates the environment; notebooks are uploaded by the pipeline.

## Starter Files (What to add to the repository next)
For students to execute the lab, add the following scaffold files under `Module 01/`:
- `Module 01/README.md` ? Step-by-step lab instructions, acceptance tests, and cleanup steps.
- `Module 01/Infrastructure/terraform_example.tf` ? Terraform skeleton for basic infra (RG, Storage, Key Vault, Databricks, PostgreSQL).
- `Module 01/notebooks/starter_notebook_read_transform_write.py` ? Parameterized notebook (PySpark) that reads from `raw/`, runs simple transformations, writes to `processed/`, and to Postgres via JDBC.
- `Module 01/ADF/adf_pipeline_copy_and_invoke.json` ? Minimal ADF pipeline JSON to copy files and trigger Databricks notebooks.
- `Module 01/sql/postgresql_schema.sql` ? Postgres schema for the `netflix` dataset and basic sample DDL.
- `Module 01/devops/azure-pipelines.yml` ? A simple pipeline that runs Terraform and uploads notebooks.
- `Module 01/sample_data/` ? Placeholder for a small sample dataset or instructions to download it.

## How to proceed next (Actionable Steps for Instructor / Students):
1. Add the scaffolding files listed above to the repository as starter templates.
2. Confirm dataset availability; if licensing prohibits distribution, add clear instructions for students to download the dataset from the public source and where to place it within `Module 01/sample_data/`.
3. Optionally, provide a Terraform or ARM template and provide a walkthrough for both CLI-based and IaC-based provisioning.
4. Add step-by-step run instructions in `Module 01/README.md` and link the script and templates inside the file.
5. Validate the acceptance tests and make a short 3?5 minute demo recording to document the end-to-end pipeline.

---
If you'd like, I can create the starter scaffolding files now (README + skeleton TF + sample notebook + pipeline JSON + SQL DDL + pipeline YAML) and add them to `Module 01/`. Tell me which files you want me to create first, or I can create all files with template content by default.

## Roles & Responsibilities
- Instructor:
    - Provide subscription access policy, datasets, and grading rubric.
    - Supply example workspace templates and starter notebooks.
- Students:
    - Provision resources (per permissions), implement pipelines, and document the work.
    - Adhere to cost/safety guidance and clean up resources as required.
- TA:
    - Assist with permission issues, debugging infra problems, and validation.

## Success Criteria / Acceptance Tests
- Resources exist and follow naming/convention guidelines.
- Databricks notebook reads the raw Netflix CSV in storage.
- ADF pipeline successfully orchestrates the Databricks job or performs copy activity.
- Processed data is written to PostgreSQL and/or processed storage with expected schema/row counts.
- Documentation includes run commands, the cost/capping approach, and cleanup steps.

## Recommended Configurations & Best Practices
- Use resource tags (team, sprint, cost-center).
- Use minimal SKUs for labs (Databricks Standard; PostgreSQL Basic/GPZ with minimal vCores).
- Use service principal & managed identities instead of hardcoded credentials.
- Store secrets in Azure Key Vault and reference them from Databricks/ADF.
- Use a bronze/silver/gold curated storage structure:
    - raw/ (landing)
    - staging/ (transformed)
    - processed/ (analytics-ready)
- Cost controls: auto-terminate Databricks clusters after inactivity; set budgets and alerts.

## Security & Cost Considerations
- Limit network exposure (NSGs, private endpoints if possible).
- Use firewall rules for PostgreSQL and Databricks as required.
- Provide cleanup steps to remove resources or automate teardown.

## Resources & Links (Instructor-supplied)
- Azure Databricks documentation and quickstart
- Azure Data Factory docs and copy activity guide
- Azure Database for PostgreSQL quickstart
- Databricks notebooks: PySpark basics and JDBC load/save examples
- Netflix dataset source or instructor dataset link

## Example Deliverable Naming Conventions
- Resource Group: rg-netflix-{studentid}-{sprint}
- Databricks: dbws-netflix-{studentid}
- Storage Account: stnetflix{studentid}
- ADF: adf-netflix-{studentid}
- PostgreSQL: pgnetflix-{studentid}

## Cleanup Plan
- Export resource inventory: resource IDs, cost estimates, and tags.
- Scripted teardown: az group delete --name rg-netflix-{studentid} --yes --no-wait
- Document final queries and sample visualizations for the next sprint.

Notes:
- For consistency, provide starter ARM/Terraform templates if available.
- If students don't have corporate Azure access, provide sandbox credentials or use a shared classroom subscription.

