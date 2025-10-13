"""
Urban Zones Multi-Domain Agent System

This module provides a comprehensive suite of AI agents specialized for
diverse professional domains, demonstrating expertise across industries.
"""

from .base import (
    UrbanZonesAgent,
    DomainType,
    AgentCapability,
    TaskResult,
    AgentRegistry,
    agent_registry
)

# Import all domain-specific agents
from .white_collar.real_estate_analyst import RealEstateAnalystAgent
from .blue_collar.construction_coordinator import ConstructionCoordinatorAgent
from .creative.marketing_strategist import MarketingStrategistAgent
from .healthcare.medical_research_assistant import MedicalResearchAssistantAgent

# Auto-register all agents
def register_all_agents():
    """Register all available agents in the system."""
    agents = [
        RealEstateAnalystAgent(),
        ConstructionCoordinatorAgent(),
        MarketingStrategistAgent(),
        MedicalResearchAssistantAgent(),
    ]
    
    for agent in agents:
        agent_registry.register_agent(agent)
    
    return agent_registry

# Initialize the registry
register_all_agents()

__all__ = [
    'UrbanZonesAgent',
    'DomainType',
    'AgentCapability',
    'TaskResult',
    'AgentRegistry',
    'agent_registry',
    'RealEstateAnalystAgent',
    'ConstructionCoordinatorAgent',
    'MarketingStrategistAgent',
    'MedicalResearchAssistantAgent',
    'register_all_agents'
]
