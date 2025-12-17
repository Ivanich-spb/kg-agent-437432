"""Basic usage example for the KG-Agent skeleton.

This example demonstrates how to create a simple agent with an in-memory KG
and a toy tool. Replace the dummy LLM with a real model (HuggingFace/LLM
wrapper) and implement prompt parsing per the paper's approach.
"""
from typing import Any

from kg_agent.core import KGAgent, KGToolbox, KGExecutor, neighbor_tool


class DummyLLM:
    """Minimal dummy LLM wrapper for demo purposes.

    This class emulates a generate() method. Replace with a proper model.
    """

    def generate(self, prompt: str):
        # TODO: Replace with real LLM call (e.g., transformers pipeline or custom wrapper)
        return "[]"


def main():
    # Initialize components
    llm = DummyLLM()
    executor = KGExecutor()

    # Load a tiny toy graph
    triples = [("Alice", "knows", "Bob"), ("Bob", "works_with", "Carol")]
    executor.load_triples(triples)

    toolbox = KGToolbox()
    toolbox.register("neighbors", lambda node, depth=1: neighbor_tool(executor, node, depth))

    agent = KGAgent(llm=llm, toolbox=toolbox, executor=executor)

    question = "Who is two hops away from Alice?"
    result = agent.run(question)
    print("Agent result:", result)


if __name__ == "__main__":
    main()
