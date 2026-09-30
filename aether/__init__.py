"""Aether — on-device agentic intelligence for Snapdragon-powered HP PCs."""

__version__ = "1.0.0"

from aether.brief import Brief
from aether.har import HeterogeneousAgenticRouter, RoutePlan
from aether.pipeline import AetherPipeline

__all__ = [
    "AetherPipeline",
    "Brief",
    "HeterogeneousAgenticRouter",
    "RoutePlan",
]
