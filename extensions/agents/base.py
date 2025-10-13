"""
Base classes for UnderratedVision domain-specific agents.

This module provides the foundation for creating specialized AI agents
that extend Magentic-UI's capabilities for specific professional domains.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import asyncio
from datetime import datetime

from magentic_ui import get_task_team
from magentic_ui.teams.orchestrator.orchestrator_config import OrchestratorConfig


class DomainType(Enum):
    """Professional domain categories for specialized agents."""
    WHITE_COLLAR = "white_collar"
    BLUE_COLLAR = "blue_collar"
    URBAN_PLANNING = "urban_planning"
    REAL_ESTATE = "real_estate"
    CONSTRUCTION = "construction"
    MUNICIPAL = "municipal"


@dataclass
class AgentCapability:
    """Represents a specific capability of an agent."""
    name: str
    description: str
    input_types: List[str]
    output_types: List[str]
    confidence_level: float = 0.8


@dataclass
class TaskResult:
    """Standardized result format for agent tasks."""
    success: bool
    data: Any
    confidence: float
    execution_time: float
    metadata: Dict[str, Any]
    timestamp: datetime


class UrbanZonesAgent(ABC):
    """
    Base class for all UnderratedVision domain-specific agents.

    This class provides the foundation for creating specialized agents
    that can integrate with the Magentic-UI platform while adding
    domain-specific intelligence and capabilities.
    """
    
    def __init__(
        self,
        name: str,
        domain: DomainType,
        capabilities: List[AgentCapability],
        description: str = "",
        version: str = "1.0.0"
    ):
        self.name = name
        self.domain = domain
        self.capabilities = capabilities
        self.description = description
        self.version = version
        self.created_at = datetime.now()
        self._task_history: List[TaskResult] = []
    
    @abstractmethod
    async def execute_task(self, task: str, context: Optional[Dict] = None) -> TaskResult:
        """
        Execute a domain-specific task.
        
        Args:
            task: The task description or command
            context: Optional context information
            
        Returns:
            TaskResult with execution details and results
        """
        pass
    
    @abstractmethod
    def get_capabilities_description(self) -> str:
        """Return a human-readable description of agent capabilities."""
        pass
    
    def get_domain_expertise(self) -> Dict[str, Any]:
        """Return information about the agent's domain expertise."""
        return {
            "domain": self.domain.value,
            "name": self.name,
            "description": self.description,
            "capabilities": [
                {
                    "name": cap.name,
                    "description": cap.description,
                    "confidence": cap.confidence_level
                }
                for cap in self.capabilities
            ],
            "version": self.version,
            "task_count": len(self._task_history),
            "average_confidence": self._calculate_average_confidence()
        }
    
    def _calculate_average_confidence(self) -> float:
        """Calculate average confidence from task history."""
        if not self._task_history:
            return 0.0
        return sum(result.confidence for result in self._task_history) / len(self._task_history)
    
    async def validate_input(self, task: str, context: Optional[Dict] = None) -> bool:
        """Validate if the agent can handle the given task."""
        # Basic validation - can be overridden by specific agents
        return len(task.strip()) > 0
    
    def add_task_result(self, result: TaskResult) -> None:
        """Add a task result to the agent's history."""
        self._task_history.append(result)
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics for the agent."""
        if not self._task_history:
            return {"tasks_completed": 0, "success_rate": 0.0, "average_confidence": 0.0}
        
        successful_tasks = sum(1 for result in self._task_history if result.success)
        return {
            "tasks_completed": len(self._task_history),
            "success_rate": successful_tasks / len(self._task_history),
            "average_confidence": self._calculate_average_confidence(),
            "average_execution_time": sum(r.execution_time for r in self._task_history) / len(self._task_history)
        }


class AgentRegistry:
    """Registry for managing domain-specific agents."""
    
    def __init__(self):
        self._agents: Dict[str, UrbanZonesAgent] = {}
        self._domain_agents: Dict[DomainType, List[UrbanZonesAgent]] = {
            domain: [] for domain in DomainType
        }
    
    def register_agent(self, agent: UrbanZonesAgent) -> None:
        """Register a new agent."""
        self._agents[agent.name] = agent
        self._domain_agents[agent.domain].append(agent)
    
    def get_agent(self, name: str) -> Optional[UrbanZonesAgent]:
        """Get an agent by name."""
        return self._agents.get(name)
    
    def get_agents_by_domain(self, domain: DomainType) -> List[UrbanZonesAgent]:
        """Get all agents for a specific domain."""
        return self._domain_agents.get(domain, [])
    
    def list_all_agents(self) -> List[UrbanZonesAgent]:
        """Get all registered agents."""
        return list(self._agents.values())
    
    def get_domain_summary(self) -> Dict[str, Any]:
        """Get a summary of all domains and their agents."""
        return {
            domain.value: {
                "agent_count": len(agents),
                "agents": [agent.name for agent in agents]
            }
            for domain, agents in self._domain_agents.items()
        }


# Global agent registry instance
agent_registry = AgentRegistry()
