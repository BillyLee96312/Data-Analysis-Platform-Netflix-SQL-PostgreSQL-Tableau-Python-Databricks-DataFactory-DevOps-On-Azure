# Module 01 ? Sprint 1: Foundation & Infrastructure Setup

This module contains the Sprint 1 lab materials and step-by-step instructions to provision a lab environment for the course.

## Overview
Sprint 1 focuses on provisioning and configuring core Azure services: ADLS Gen2, Databricks, Azure Data Factory (ADF), and PostgreSQL. Students will run an ETL pipeline: raw data ¡æ Databricks processing ¡æ PostgreSQL and processed storage.

## Learning Objectives
- Provision Azure resources and follow naming conventions and tagging.
- Upload and manage data in ADLS Gen2 and run basic Spark transformations in Databricks.
- Configure an ADF pipeline to orchestrate a Databricks job or copy activity.
- Connect Databricks with PostgreSQL using secure credentials.
- Implement basic security, secrets management, and cost control.

## Prerequisites
- Azure subscription with contributor-level access (or a sandbox/instructor provided subscription).
- Basic command-line experience with Azure CLI.
- Databricks CLI (optional) and Python 3.8+ installed locally.

## Setup & Step-by-Step Lab Instructions
1. Prepare the environment
   - Create a Resource Group (naming convention: `rg-netflix-{studentid}-sprint1`).
   - Create a Storage Account (e.g., `stnetflix{studentid}`) with Hierarchical Namespace enabled and containers: `raw`, `staging`, `processed`.

2. Upload sample dataset
   - Download a small sample Netflix dataset or use the public source link.
   - Upload into the `raw/` container using AzCopy or Azure Storage Explorer.

3. Provision PostgreSQL
   - Create an Azure Database for PostgreSQL instance (basic/dev SKU) and a database named `analytics`.
   - Create a test user and store credentials in Key Vault.

4. Provision Databricks and cluster
   - Create a Databricks workspace (Standard) and a minimal cluster with `autoTerminate` set to 10 minutes.
   - Upload the starter notebook and configure cluster to use managed identity or token.

5. Configure Azure Data Factory
   - Create ADF and link services for ADLS Gen2, Databricks, and PostgreSQL.
   - Build a pipeline with a Copy Activity and a Databricks Notebook Activity.

6. Configure Secrets and Security
   - Create Key Vault and store DB credentials and tokens; configure RBAC and Key Vault policies.
   - Implement firewall rules for the PostgreSQL instance (allow student IP and Databricks workspace IP or use private endpoint).

7. Validate Pipeline
   - Run the ADF pipeline or manually run the Databricks notebook: read CSV from `raw` ¡æ transform ¡æ write to `processed` and PostgreSQL.
   - Confirm data in `processed/` container and in PostgreSQL.

8. Cost Control and Cleanup
   - Create a budget alert and set up tags on resources (team/student/sprint).
   - Run cleanup: `az group delete --name rg-netflix-{studentid}-sprint1 --yes --no-wait`.

## Acceptance Tests (Checklist)
- [ ] Resource Group & storage account created with required containers.
- [ ] Sample CSV present in `raw/`.
- [ ] PostgreSQL instance accessible and `netflix` schema exists.
- [ ] Databricks workspace and notebook run correctly and write results into storage and DB.
- [ ] ADF pipeline runs successfully and orchestrates Notebook or Copy activities as expected.
- [ ] No hard-coded secrets in notebooks or pipelines; secrets are stored in Key Vault.
- [ ] Budget alert and resource tags configured.

## Deliverables for Sprint 1
- `README.md` and resource inventory.
- Starter notebook and SQL schema.
- ADF pipeline JSON export and logs.
- Minimal IaC sample (Terraform/ARM) or CLI instructions for provisioning.
- Short demo video (3?5 minutes) showing end-to-end process.

## Optional: Azure DevOps CI/CD
- Add a minimal `azure-pipelines.yml` pipeline to publish notebooks and run Terraform or deployments.

## Cleanup Steps & Cost-Savings Tips
- Auto-terminate clusters, set low compute sizes for labs.
- Use `az group delete` to clean up all resources when done.
- Add tagging for cost allocation.

---

If you want, I can now create starter files (Terraform example, sample notebook skeleton, ADF pipeline JSON, SQL schema, and a sample pipeline YAML). Which files should I create first? (I can create all of them if you'd like a full scaffold.)