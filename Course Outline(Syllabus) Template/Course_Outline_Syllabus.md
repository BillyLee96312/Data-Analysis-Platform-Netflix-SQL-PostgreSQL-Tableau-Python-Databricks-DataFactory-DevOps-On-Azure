
# Course Outline & Syllabus

## Course Information
- **Course Title:** [Course Name]
- **Course Code:** [Code]
- **Instructor:** [Name]
- **Duration:** [Weeks/Months]
- **Prerequisites:** [List prerequisites]

## Course Description
[Brief overview of the course content and purpose]

## Learning Objectives
By the end of this course, students will be able to:
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3
- [ ] Objective 4

## Course Topics

### Module 1: [Topic Name]
- Subtopic 1.1
- Subtopic 1.2

### Module 2: [Topic Name]
- Subtopic 2.1
- Subtopic 2.2

### Module 3: [Topic Name]
- Subtopic 3.1
- Subtopic 3.2

## Assessment & Grading
| Assessment | Weight |
|------------|--------|
| Assignments | 30% |
| Quizzes | 20% |
| Project | 30% |
| Final Exam | 20% |

## Required Materials
- [Resource 1]
- [Resource 2]
- [Resource 3]

## Course Policies
- [Attendance policy]
- [Late submission policy]
- [Academic integrity]

## Support & Resources
- Office hours: [Schedule]
- Contact: [Email]
- Help resources: [Links]



## Steps To Add A New Structured Module with creating a file

Add a new structured Module 01 outline to Module 01/module_01_introduction.md (or a new file) that includes the 8 modules and chapter-level learning outcomes.
Add recommended starter files:
Module 01/Infrastructure/terraform_example.tf (or ARM) to create RG, storage, Key Vault, Databricks workspace, PostgreSQL.
Module 01/notebooks/starter_notebook_read_transform_write.py (Databricks) ? parameterized PySpark sample.
Module 01/ADF/adf_pipeline_copy_and_invoke.json ? ADF pipeline skeleton.
Module 01/sql/postgresql_schema.sql ? DDL for netflix schema.
Module 01/devops/azure-pipelines.yml ? minimal CI/CD pipeline (optional).
Add a Module 01/README.md with step-by-step lab instructions, acceptance tests, and cleanup steps.
Update the top-level README to link to Module 01 and the additional resources.
Implement cost, security, and governance checklists for students to follow.

## Module 01 ? Implementation Status and Next Steps
The repository now includes an expanded Module 01 with starter scaffolding. Use the following list to verify and continue development.

Files created (Module 01):
- `Module 01/module_01_introduction.md` ? Contains the expanded Sprint 1 curriculum and learning objectives.
- `Module 01/README.md` ? Step-by-step lab instructions, acceptance tests, and cleanup steps.
- `Module 01/Infrastructure/terraform_example.tf` ? Terraform skeleton to provision RG, storage, Key Vault, and placeholders for Databricks/Postgres resources.
- `Module 01/notebooks/starter_notebook_read_transform_write.py` ? Starter Databricks PySpark notebook script.
- `Module 01/ADF/adf_pipeline_copy_and_invoke.json` ? Sample ADF pipeline JSON template with Copy and Databricks activities.
- `Module 01/sql/postgresql_schema.sql` ? Basic PostgreSQL schema DDL for the `netflix` dataset.
- `Module 01/devops/azure-pipelines.yml` ? Minimal Azure Pipelines skeleton (Terraform + Notebook upload steps).
- `Module 01/sample_data/README.md` ? Instructions to download or upload sample datasets and AzCopy example.

Suggested Next Steps (Choose and track tasks):
1. Seed the `sample_data` with a small CSV (if licensing permits) or provide a simple synthetic sample that follows the `postgresql_schema.sql` layout.
2. Flesh out the `terraform_example.tf` with modules for Databricks and Azure Database for PostgreSQL or include an ARM template. Add a `variables.tf` and `outputs.tf` as needed.
3. Enhance the starter notebook to accept Databricks widgets for parameters and add robust error handling and logging.
4. Export an example ADF pipeline using the portal, and store the named pipeline JSON in `Module 01/ADF/`.
5. Add a `Module 01/notebooks/README.md` describing how to upload and parameterize the notebook in Databricks.
6. Optionally, create an `env.sample` to standardize environment variables and `Module 01/.env` for students (not checked into git) to configure local credentials.
7. Provide a short demo video and sample screenshots to illustrate successful run and acceptance tests.

Development Checklist for instructors:
- Confirm availability of sandbox environment for students or provide instructions for safe provisioning.
- Add a Terraform backend (e.g., Azure Storage) for state management, if Terraform will be used for provisioning.
- Provide sample Key Vault scripts or notes on secret rotation and RBAC setup.

---
This document can be used as a checkpoint for the sprint; track these items in your course board and mark them complete as scaffolding, content, and validation are added.