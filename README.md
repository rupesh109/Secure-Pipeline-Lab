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



## 🔐 Security Gates

| Security Gate | Tool | Purpose |
|:---|:---|:---|
| <h3>Secret Detection</h3> | Gitleaks | Detect exposed credentials |
| <h3>Static Analysis</h3> | Semgrep | Identify insecure application code |
| <h3>Dependency Scanning</h3> | Trivy | Detect vulnerable dependencies |
| <h3>Configuration Scanning</h3> | Trivy | Identify configuration risks |
| <h3>Container Scanning</h3> | Docker + Trivy | Scan images for vulnerabilities |
| <h3>Merge Protection</h3> | GitHub Rulesets | Enforce required checks |

## 🧰 Technology Stack

| Category | Technology |
|:---|:---|
| <h3>Operating System</h3> | Kali Linux |
| <h3>CI/CD</h3> | GitHub Actions |
| <h3>Application</h3> | Python, Flask |
| <h3>Security Analysis</h3> | Semgrep |
| <h3>Secret Detection</h3> | Gitleaks |
| <h3>Vulnerability Scanning</h3> | Trivy |
| <h3>Containerization</h3> | Docker |
| <h3>Version Control</h3> | Git and GitHub |

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

### 🚀 Getting Started

### Prerequisites

- Git
- Python 3
- Docker
- GitHub account

### Clone the Repository

```bash
git clone https://github.com/rupesh109/Secure-Pipeline-Lab.git
cd Secure-Pipeline-Lab
```

### Set Up Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Build the Docker Image

```bash
docker build -t secure-pipeline-lab:local .
```

## 🧪 Security Testing

| Test Case | Expected Result |
|:---|:---|
| <h3>Synthetic leaked secret</h3> | Secret scan fails |
| <h3>Insecure Python pattern</h3> | SAST fails when detected |
| <h3>Vulnerable dependency</h3> | Trivy fails when policy criteria are met |
| <h3>Insecure container configuration</h3> | Relevant scan fails when detected |
| <h3>Corrected pull request</h3> | Required checks pass |

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

