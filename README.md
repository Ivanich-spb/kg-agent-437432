# KG-Agent

Paper: KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph

ArXiv: http://arxiv.org/abs/2402.11163v1

Overview

KG-Agent proposes an autonomous LLM-based agent framework that improves reasoning over knowledge graphs (KGs) by integrating a small LLM, a multifunctional toolbox, a KG executor, and a knowledge memory. The framework iteratively selects tools and updates memory, and formulates multi-hop reasoning as program-like steps to fine-tune the base LLM. The paper reports strong performance when fine-tuning LLaMA-7B with a small instruction dataset.

Repository structure

- README.md: this file
- requirements.txt: Python dependencies
- Dockerfile: container specification
- setup.py: package installer
- kg_agent/__init__.py: package entry
- kg_agent/core.py: core KG-Agent framework skeleton
- examples/basic.py: minimal usage example

Usage

This repository provides a skeleton implementation for research and experimentation. The core implementation is intentionally minimal and contains TODO markers where project-specific logic (model loading, tool implementations, KG executor, memory store, and dataset processing) should be added.

References

- Paper: http://arxiv.org/abs/2402.11163v1

Notes

- The LLM/backbone assumed by the examples is PyTorch-compatible (e.g., HuggingFace Transformers). Adapt to your LLM of choice.
- No complete training/evaluation code is provided in this skeleton; use this as a starting point for reproducing the KG-Agent framework.
