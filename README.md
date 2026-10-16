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
---

## 🔐 Security Gates

| Security Gate | Tool | Purpose |
|:---|:---|:---|
| Secret Detection | Gitleaks | Detect exposed credentials |
| Static Analysis | Semgrep | Identify insecure application code |
| Dependency Scanning | Trivy | Detect vulnerable dependencies |
| Configuration Scanning | Trivy | Identify configuration risks |
| Container Scanning | Docker + Trivy | Scan images for vulnerabilities |
| Merge Protection | GitHub Rulesets | Enforce required checks |

## 🧰 Technology Stack

| Category | Technology |
|:---|:---|
| Operating System | Kali Linux |
| CI/CD | GitHub Actions |
| Application | Python, Flask |
| Security Analysis | Semgrep |
| Secret Detection | Gitleaks |
| Vulnerability Scanning | Trivy |
| Containerization | Docker |
| Version Control | Git and GitHub |

## 📂 Repository Structure

    Secure-Pipeline-Lab/
    ├── .github/
    │   └── workflows/
    │       └── ci-security.yml
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    ├── .trivyignore.yaml
    └── README.md

## ⚙️ How It Works

1. **Code Submission:** A developer pushes code or opens a pull request.
2. **Security Analysis:** Gitleaks, Semgrep, and Trivy run security checks.
3. **Container Build:** Docker builds the application image.
4. **Image Scanning:** Trivy scans the built image for vulnerabilities.
5. **Merge Enforcement:** GitHub requires the configured security checks to pass.

## 🚀 Getting Started

### Prerequisites

- Git
- Python 3
- Docker
- GitHub account

### Clone the Repository

    git clone https://github.com/rupesh109/Secure-Pipeline-Lab.git
    cd Secure-Pipeline-Lab

### Set Up Python

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

### Build the Docker Image

    docker build -t secure-pipeline-lab:local .

## 🧪 Security Testing

| Test Case | Expected Result |
|:---|:---|
| Synthetic leaked secret | Secret scan fails |
| Insecure Python pattern | SAST fails when detected |
| Vulnerable dependency | Trivy fails when policy criteria are met |
| Insecure container configuration | Relevant scan fails when detected |
| Corrected pull request | Required checks pass |

All test credentials must be synthetic. Never commit real API keys, passwords, or access tokens.

## 🔒 Branch Protection

Configure GitHub branch protection to require these checks:

- `secrets`
- `sast`
- `deps-and-iac`
- `build-scan`

A failed required check must prevent merging into `main`.

## 📊 Results and Evidence

- [ ] Successful baseline pipeline
- [ ] Secret detection test
- [ ] SAST test
- [ ] Dependency scanning test
- [ ] Container scanning test
- [ ] Pull request blocked by a failed check
- [ ] Successful pipeline after remediation

## 🛣️ Future Improvements

- Generate a Software Bill of Materials (SBOM).
- Automate dependency updates.
- Pin container images by digest.
- Add container image signing.
- Use OIDC for cloud deployments.
- Integrate centralized security reporting.

## 👨‍💻 Author

**Rupesh Kumar Jha**

DevSecOps | Cloud Security | CI/CD | Container Security

---

<div align="center">

**Secure by design. Tested continuously. Delivered confidently.**

</div>
