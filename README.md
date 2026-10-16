# 🛡️ Secure Pipeline Lab
### A Security-First CI/CD Pipeline with Automated DevSecOps Gates

![CI](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=githubactions)
![Security](https://img.shields.io/badge/Security-DevSecOps-green)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)

A hands-on DevSecOps project demonstrating how to integrate automated
security checks into a CI/CD pipeline and prevent insecure changes
from being merged into the main branch.

The pipeline combines secret detection, static application security
testing (SAST), dependency and infrastructure misconfiguration
scanning, and container image vulnerability scanning.

> **Project goal:** Make security an enforceable condition of software
> delivery rather than a check performed after deployment.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Architecture](#-pipeline-architecture)
- [Security Gates](#-security-gates)
- [Technology Stack](#-technology-stack)
- [Repository Structure](#-repository-structure)
- [How the Pipeline Works](#-how-the-pipeline-works)
- [Getting Started](#-getting-started)
- [Security Testing](#-security-testing)
- [Branch Protection](#-branch-protection)
- [Evidence and Results](#-evidence-and-results)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🎯 Overview

Modern CI/CD pipelines can introduce security risks when credentials,
vulnerable dependencies, unsafe application code, or insecure container
configurations go undetected.

This project implements a GitHub Actions workflow that runs automated
security checks on pull requests and pushes to the `main` branch.

### Objectives

- Detect accidentally committed secrets.
- Identify insecure Python application patterns.
- Scan dependencies and project configuration for security issues.
- Build and scan a Docker container image.
- Fail required checks when configured security thresholds are exceeded.
- Enforce security checks through GitHub branch protection.
- Document findings, remediation, and justified security exceptions.

---

## 🏗️ Pipeline Architecture

```text
              Developer
                  |
                  v
          Commit / Pull Request
                  |
                  v
          GitHub Actions CI/CD
                  |
        +---------+----------+
        |         |          |
        v         v          v
     Gitleaks   Semgrep     Trivy FS
     Secrets     SAST      Dependencies
                           & Misconfig
        |         |          |
        +---------+----------+
                  |
           All gates pass?
                  |
                  v
           Docker Image Build
                  |
                  v
           Trivy Image Scan
                  |
                  v
       Required Checks Successful
                  |
                  v
       Protected Branch: main
                  |
                  v
           Merge Permitted
# Secure-Pipeline-Lab
# Secure-Pipeline-Lab
Enforcement principle: A pull request should not be mergeable when
a required security check fails. This requires the corresponding GitHub
branch protection or ruleset configuration in addition to the workflow.
| Gate                      | Tool                     | Purpose                                                   |
| ------------------------- | ------------------------ | --------------------------------------------------------- |
| Secret detection          | Gitleaks                 | Detect exposed credentials and secrets                    |
| Static analysis           | Semgrep                  | Identify potentially insecure application code            |
| Dependency scanning       | Trivy                    | Detect vulnerable dependencies                            |
| Misconfiguration scanning | Trivy                    | Identify supported infrastructure and configuration risks |
| Container scanning        | Docker + Trivy           | Detect vulnerabilities in the built image                 |
| Merge enforcement         | GitHub branch protection | Require security checks before merging                    |

Security policy

The pipeline is configured to fail on findings that meet its specified
severity thresholds.

High and critical findings are targeted by the Trivy scans.
Unfixed vulnerabilities are ignored by the current Trivy configuration.
Semgrep runs with Python and OWASP Top 10 rulesets.
Gitleaks checks repository history through a full checkout.

The exact results depend on the tools' rulesets, database versions,
project dependencies, and repository contents.


| Category               | Technology     |
| ---------------------- | -------------- |
| Operating system       | Kali Linux     |
| CI/CD                  | GitHub Actions |
| Application            | Python, Flask  |
| Static analysis        | Semgrep        |
| Secret detection       | Gitleaks       |
| Vulnerability scanning | Trivy          |
| Containerization       | Docker         |
| Version control        | Git and GitHub |
| Workflow format        | YAML           |


## 📂 Repository Structure

secure-pipeline/
├── .github/
│   └── workflows/
│       └── ci-security.yml
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .trivyignore.yaml
└── README.md

### ⚙️ How the Pipeline Works
1. Developer opens a pull request

GitHub Actions starts the workflow when a pull request is opened
or when code is pushed to main.

2. Security checks run

The pipeline performs secret detection, static analysis, and
filesystem scanning.

3. Container image is built

After the first three jobs succeed, the pipeline builds the Docker
image from the project Dockerfile.

4. Image vulnerability scan runs

Trivy scans the built image for findings at the configured severity
threshold.

5. Merge protection enforces the result

Once the required checks are configured in GitHub branch protection,
a failing required check prevents the pull request from being merged.



🛣️ Future Improvements
Pin the Semgrep container image by digest.
Add automated dependency update management.
Generate and publish a Software Bill of Materials (SBOM).
Add container image signing and provenance verification.
Use OIDC for cloud deployments instead of long-lived cloud keys.
Add deployment policies and runtime monitoring.
Integrate additional security reporting into the pipeline.
👨‍💻 Author

Rupesh Kumar Jha

DevSecOps | Cloud Security | CI/CD | Container Security

This project demonstrates practical implementation of security
controls throughout the software delivery lifecycle.

📄 License

This project is intended for educational and portfolio use.
An MIT license may be added if the repository is distributed under
that license.
