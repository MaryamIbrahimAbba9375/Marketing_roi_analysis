# Local LLM Modular Serving Infrastructure Architecture (DTA Framework)

## 🏗️ Architecture Overview
This deployment separates tasks across distinct architectural boundaries to implement scalable edge-inference tracking patterns:
- **`models.py`:** Standardizes token pipelines, builds the prompt template injection boundaries, and processes generation configurations.
- **`main.py`:** Exposes asynchronous network server parameters via FastAPI, enforces input validation schemas using Pydantic, and handles runtime telemetry logs.
- **`client.py`:** Translates application workflows into stateful, accessible interactions via Streamlit web rendering interfaces.

---

## 📈 Latency Audit & Resource Constraints
- **Performance Findings:** During execution passes on single-core host environments using standard CPU thread parameters, the baseline local 1.1B TinyLlama iteration records token processing latency speeds averaging roughly **0.5s to 1.5s per token generated**.
- **Hardware Bottlenecks:** Memory bandwidth limits and floating-point logic units on standard CPUs degrade performance. Unlike high-throughput vector-aligned GPUs, standard configurations restrict parallel layer processing, making runtime metrics dependent on structural word choices and context limits.

---

## 🛡️ Applied Business Persona & Optimization Plan
- **Operational Persona:** Expert Programming Code Reviewer.
- **Concrete Use Case:** Deployed inside active corporate networks as an automated pull-request prep screening assistant. Developers run local code blocks through the application terminal to identify common PEP8 violations, dependency flaws, or typing oversights before initiating continuous integration builds. This saves developer engineering triage overhead.
- **Proposed Inference Optimization:** **Model Quantization (INT4/INT8 Conversion)**.
- **Optimization Rationale:** Quantizing default 32-bit float parameters down to structured 4-bit integers reduces the memory storage profile of local models by up to 75%. This configuration swap limits memory cache traffic constraints, enabling CPU pipelines to complete matrix multiplications significantly faster and reducing generation latencies.
