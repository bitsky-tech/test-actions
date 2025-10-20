"""
The Agentic module provides core components for building intelligent agent systems.

This module contains various Automa implementations for orchestrating and executing 
LLM-based intelligent agent workflows. These Automa implementations are typically 
composed together to build complex intelligent agents with advanced capabilities.
"""

from ._concurrent_automa import ConcurrentAutoma

__all__ = [
    "ConcurrentAutoma", 
]