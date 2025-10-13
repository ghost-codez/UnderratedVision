"""
UnderratedVision Extensions

Enterprise-ready multi-domain AI automation platform built on Microsoft Magentic-UI.
Transforming industries through intelligent automation across diverse professional domains.
"""

__version__ = "2.0.0"
__magentic_ui_version__ = "0.1.2"
__author__ = "UnderratedVision Team"
__email__ = "contact@underratedvision.com"
__license__ = "MIT"
__description__ = "Enterprise-ready multi-domain AI automation platform"

from .agents import (
    UrbanZonesAgent,
    DomainType,
    AgentCapability,
    TaskResult,
    AgentRegistry,
    agent_registry,
    register_all_agents,
    RealEstateAnalystAgent,
    ConstructionCoordinatorAgent,
    MarketingStrategistAgent,
    MedicalResearchAssistantAgent,
)

from .workflows import (
    MultiDomainOrchestrator,
    WorkflowType,
    WorkflowStep,
    WorkflowResult,
    multi_domain_orchestrator,
)

# Auto-register all agents when the package is imported
register_all_agents()

__all__ = [
    # Version info
    "__version__",
    "__magentic_ui_version__",
    "__author__",
    "__email__",
    "__license__",
    "__description__",
    
    # Base classes
    "UrbanZonesAgent",
    "DomainType", 
    "AgentCapability",
    "TaskResult",
    "AgentRegistry",
    "agent_registry",
    "register_all_agents",
    
    # Domain agents
    "RealEstateAnalystAgent",
    "ConstructionCoordinatorAgent", 
    "MarketingStrategistAgent",
    "MedicalResearchAssistantAgent",
    
    # Workflows
    "MultiDomainOrchestrator",
    "WorkflowType",
    "WorkflowStep", 
    "WorkflowResult",
    "multi_domain_orchestrator",
]
