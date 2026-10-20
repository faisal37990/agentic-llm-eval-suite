# 🤖 Agentic LLM Evaluation & Adversarial Red-Teaming Suite

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![JSON Schema](https://img.shields.io/badge/Schema-Draft%207%2F2020--12-green?logo=json&logoColor=white)](https://json-schema.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

> **High-fidelity evaluation harness, automated JSON schema verifier, and multi-turn adversarial red-teaming engine for frontier LLMs (Claude, GPT-4, Codex, GLM).**
> Built by **[Faisal Sharif](https://linkedin.com/in/mohammedalfaisal-sharif/)** based on production AI Training & Evaluation and post-training (SFT) workflows.

---

## 📌 Architecture & Capabilities

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  Adversarial Prompts   │ ───► │  Multi-Turn Agent Env  │ ───► │  Automated Verifier    │
│  & Red-Team Scenarios  │      │  (Docker Sandboxed)    │      │  - JSON Schema Check   │
└────────────────────────┘      └────────────────────────┘      │  - Golden PPT/XLS Match│
                                                                 │  - Multi-Dim Rubrics   │
                                                                └────────────────────────┘
```

1. **Automated JSON Schema Verification:** Programmatically validates structured JSON agent outputs against strict business rules and reference golden datasets.
2. **Adversarial Red-Teaming Matrix:** Evaluates 20+ edge-case business scenarios designed to stress test reasoning consistency and eliminate hallucination modes.
3. **Multi-Dimensional Rubrics:** Quantifies domain accuracy, format compliance, reasoning depth, and instruction-following fidelity.
4. **Containerized Execution Sandbox:** Enforces isolated runtime environments via Docker for safe tool-calling validation.

---

## 🚀 Quickstart

### 1. Run via Docker
```bash
docker build -t agentic-llm-eval-suite .
docker run --rm agentic-llm-eval-suite
```

### 2. Run Locally via Python
```bash
# Clone the repository
git clone https://github.com/faisal37990/agentic-llm-eval-suite.git
cd agentic-llm-eval-suite

# Install dependencies
pip install -r requirements.txt

# Execute evaluation pipeline
python evaluator.py --run-eval --dataset scenarios/business_cases.json
```

---

## 📊 Sample Verification Output

```text
======================================================================
  AGENTIC LLM EVALUATION REPORT — FAISAL SHARIF AI TRAINING & EVALUATION HARNESS
======================================================================
[INFO] Loading Golden Solution Schema: schemas/business_analysis.json
[INFO] Verifying 20 Frontier Agent Executions...

✓ Case Study #01 [Margin Optimization]: PASS (Schema: 100%, Accuracy: 98.4%)
✓ Case Study #02 [Cash-Flow Projections]: PASS (Schema: 100%, Accuracy: 99.1%)
✗ Case Study #03 [Adversarial Ambiguity]: STUMPED MODEL (Hallucination Detected)
   └─ Reason: Agent hallucinated EBITDA multiplier on unstated fiscal horizon.
----------------------------------------------------------------------
Total Cases Tested: 20 | Conformance: 95.0% | Adversarial Catch Rate: 100%
======================================================================
```

---

## 👤 Author
**Faisal Sharif** — *AI Data Engineer & Model Evaluation Specialist*  
LinkedIn: [Mohammed Al Faisal Sharif](https://linkedin.com/in/mohammedalfaisal-sharif/) | GitHub: [@faisal37990](https://github.com/faisal37990)
