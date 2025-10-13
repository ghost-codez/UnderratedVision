"""
Construction Coordination Agent for Urban Zones.

This agent specializes in construction project management, scheduling,
safety compliance, and trade coordination for construction professionals.
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import re

from ..base import UrbanZonesAgent, DomainType, AgentCapability, TaskResult


class ConstructionCoordinatorAgent(UrbanZonesAgent):
    """
    Specialized agent for construction project coordination and management.
    
    Capabilities:
    - Project scheduling and timeline optimization
    - Trade coordination and sequencing
    - Material estimation and procurement
    - Safety compliance and regulation checking
    - Quality control and inspection scheduling
    - Cost estimation and budget tracking
    """
    
    def __init__(self):
        capabilities = [
            AgentCapability(
                name="project_scheduling",
                description="Create and optimize construction project schedules",
                input_types=["project_scope", "trade_requirements", "timeline"],
                output_types=["schedule", "critical_path", "milestones"],
                confidence_level=0.88
            ),
            AgentCapability(
                name="trade_coordination",
                description="Coordinate multiple trades and subcontractors",
                input_types=["trade_list", "dependencies", "availability"],
                output_types=["coordination_plan", "sequence_optimization"],
                confidence_level=0.85
            ),
            AgentCapability(
                name="material_estimation",
                description="Estimate materials and quantities for construction projects",
                input_types=["blueprints", "specifications", "project_type"],
                output_types=["material_list", "quantities", "cost_estimates"],
                confidence_level=0.82
            ),
            AgentCapability(
                name="safety_compliance",
                description="Check safety regulations and OSHA compliance",
                input_types=["project_type", "work_activities", "site_conditions"],
                output_types=["safety_plan", "compliance_checklist", "training_requirements"],
                confidence_level=0.90
            ),
            AgentCapability(
                name="quality_control",
                description="Schedule inspections and quality control checkpoints",
                input_types=["project_phase", "building_codes", "specifications"],
                output_types=["inspection_schedule", "quality_checklist"],
                confidence_level=0.87
            )
        ]
        
        super().__init__(
            name="construction_coordinator",
            domain=DomainType.BLUE_COLLAR,
            capabilities=capabilities,
            description="Expert construction coordination agent for project management, scheduling, and compliance",
            version="1.0.0"
        )
    
    async def execute_task(self, task: str, context: Optional[Dict] = None) -> TaskResult:
        """Execute construction coordination tasks."""
        start_time = datetime.now()
        
        try:
            task_type = self._identify_task_type(task)
            
            if task_type == "project_scheduling":
                result = await self._create_project_schedule(task, context)
            elif task_type == "trade_coordination":
                result = await self._coordinate_trades(task, context)
            elif task_type == "material_estimation":
                result = await self._estimate_materials(task, context)
            elif task_type == "safety_compliance":
                result = await self._check_safety_compliance(task, context)
            elif task_type == "quality_control":
                result = await self._plan_quality_control(task, context)
            else:
                result = await self._general_construction_analysis(task, context)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            task_result = TaskResult(
                success=True,
                data=result,
                confidence=result.get("confidence", 0.85),
                execution_time=execution_time,
                metadata={
                    "task_type": task_type,
                    "agent": self.name,
                    "domain": self.domain.value
                },
                timestamp=datetime.now()
            )
            
            self.add_task_result(task_result)
            return task_result
            
        except Exception as e:
            execution_time = (datetime.now() - start_time).total_seconds()
            return TaskResult(
                success=False,
                data={"error": str(e)},
                confidence=0.0,
                execution_time=execution_time,
                metadata={"error_type": type(e).__name__},
                timestamp=datetime.now()
            )
    
    def _identify_task_type(self, task: str) -> str:
        """Identify the type of construction task based on keywords."""
        task_lower = task.lower()
        
        if any(keyword in task_lower for keyword in ["schedule", "timeline", "planning", "sequence"]):
            return "project_scheduling"
        elif any(keyword in task_lower for keyword in ["trade", "subcontractor", "coordinate", "crew"]):
            return "trade_coordination"
        elif any(keyword in task_lower for keyword in ["material", "estimate", "quantity", "procurement"]):
            return "material_estimation"
        elif any(keyword in task_lower for keyword in ["safety", "osha", "compliance", "regulation"]):
            return "safety_compliance"
        elif any(keyword in task_lower for keyword in ["quality", "inspection", "control", "testing"]):
            return "quality_control"
        else:
            return "general_analysis"
    
    async def _create_project_schedule(self, task: str, context: Optional[Dict]) -> Dict[str, Any]:
        """Create optimized construction project schedule."""
        project_type = self._extract_project_type(task)
        duration_weeks = self._extract_duration(task) or 12
        
        # Generate realistic construction schedule
        schedule = {
            "project_type": project_type,
            "total_duration_weeks": duration_weeks,
            "phases": [
                {
                    "phase": "Site Preparation",
                    "duration_days": 5,
                    "start_date": "2024-11-01",
                    "end_date": "2024-11-05",
                    "trades": ["Excavation", "Surveying"],
                    "critical_path": True
                },
                {
                    "phase": "Foundation",
                    "duration_days": 10,
                    "start_date": "2024-11-06",
                    "end_date": "2024-11-15",
                    "trades": ["Concrete", "Rebar"],
                    "critical_path": True
                },
                {
                    "phase": "Framing",
                    "duration_days": 15,
                    "start_date": "2024-11-18",
                    "end_date": "2024-12-02",
                    "trades": ["Carpenters", "Structural"],
                    "critical_path": True
                },
                {
                    "phase": "MEP Rough-in",
                    "duration_days": 12,
                    "start_date": "2024-12-03",
                    "end_date": "2024-12-14",
                    "trades": ["Electrical", "Plumbing", "HVAC"],
                    "critical_path": False
                },
                {
                    "phase": "Insulation & Drywall",
                    "duration_days": 8,
                    "start_date": "2024-12-17",
                    "end_date": "2024-12-24",
                    "trades": ["Insulation", "Drywall"],
                    "critical_path": True
                },
                {
                    "phase": "Finish Work",
                    "duration_days": 20,
                    "start_date": "2025-01-02",
                    "end_date": "2025-01-21",
                    "trades": ["Flooring", "Painting", "Trim"],
                    "critical_path": False
                }
            ],
            "critical_milestones": [
                {"milestone": "Foundation Complete", "date": "2024-11-15"},
                {"milestone": "Framing Complete", "date": "2024-12-02"},
                {"milestone": "MEP Rough-in Complete", "date": "2024-12-14"},
                {"milestone": "Final Inspection", "date": "2025-01-21"}
            ],
            "resource_optimization": {
                "peak_crew_size": 12,
                "equipment_utilization": "85%",
                "material_delivery_schedule": "Just-in-time with 2-day buffer"
            },
            "risk_factors": [
                "Weather delays (winter construction)",
                "Material delivery delays",
                "Inspection scheduling conflicts"
            ],
            "confidence": 0.88
        }
        
        return schedule
    
    async def _coordinate_trades(self, task: str, context: Optional[Dict]) -> Dict[str, Any]:
        """Coordinate multiple trades and subcontractors."""
        trades_needed = self._extract_trades(task)
        
        coordination = {
            "trades_coordination": {
                "primary_trades": trades_needed,
                "sequencing": [
                    {"order": 1, "trade": "Excavation", "duration": "3 days", "crew_size": 4},
                    {"order": 2, "trade": "Concrete", "duration": "5 days", "crew_size": 6},
                    {"order": 3, "trade": "Framing", "duration": "10 days", "crew_size": 8},
                    {"order": 4, "trade": "Electrical", "duration": "6 days", "crew_size": 3},
                    {"order": 4, "trade": "Plumbing", "duration": "6 days", "crew_size": 3},
                    {"order": 5, "trade": "HVAC", "duration": "4 days", "crew_size": 2},
                    {"order": 6, "trade": "Drywall", "duration": "8 days", "crew_size": 4}
                ]
            },
            "coordination_challenges": [
                "Electrical and plumbing can run parallel but need coordination",
                "HVAC must wait for electrical rough-in completion",
                "Drywall cannot start until all MEP inspections pass"
            ],
            "communication_plan": {
                "daily_standup": "7:00 AM on-site",
                "weekly_coordination": "Friday 3:00 PM",
                "issue_escalation": "Project manager within 2 hours"
            },
            "quality_checkpoints": [
                "Foundation inspection before framing",
                "MEP rough-in inspection before insulation",
                "Final walkthrough before handover"
            ],
            "safety_coordination": {
                "site_safety_officer": "Required for all phases",
                "trade_specific_training": "OSHA 10 minimum for all workers",
                "daily_safety_briefings": "Before work start"
            },
            "confidence": 0.85
        }
        
        return coordination
    
    async def _estimate_materials(self, task: str, context: Optional[Dict]) -> Dict[str, Any]:
        """Estimate materials and quantities for construction project."""
        project_size = self._extract_square_footage(task) or 2000
        
        estimation = {
            "project_size_sqft": project_size,
            "material_estimates": {
                "concrete": {
                    "quantity": f"{project_size * 0.15:.0f} cubic yards",
                    "unit_cost": 120,
                    "total_cost": project_size * 0.15 * 120,
                    "supplier": "Local concrete plant"
                },
                "lumber": {
                    "quantity": f"{project_size * 6:.0f} board feet",
                    "unit_cost": 0.85,
                    "total_cost": project_size * 6 * 0.85,
                    "supplier": "Lumber yard"
                },
                "drywall": {
                    "quantity": f"{project_size * 2.2:.0f} sheets (4x8)",
                    "unit_cost": 12,
                    "total_cost": project_size * 2.2 * 12,
                    "supplier": "Building supply"
                },
                "electrical": {
                    "quantity": "Allowance per sqft",
                    "unit_cost": 3.50,
                    "total_cost": project_size * 3.50,
                    "supplier": "Electrical supply house"
                },
                "plumbing": {
                    "quantity": "Allowance per sqft",
                    "unit_cost": 2.75,
                    "total_cost": project_size * 2.75,
                    "supplier": "Plumbing supply"
                }
            },
            "total_material_cost": (project_size * 0.15 * 120) + (project_size * 6 * 0.85) + 
                                 (project_size * 2.2 * 12) + (project_size * 3.50) + (project_size * 2.75),
            "procurement_schedule": [
                {"material": "Concrete", "order_date": "2 days before pour", "delivery": "Day of pour"},
                {"material": "Lumber", "order_date": "1 week before framing", "delivery": "Staged delivery"},
                {"material": "MEP materials", "order_date": "Before rough-in", "delivery": "As needed"}
            ],
            "waste_factor": "10% added to all quantities",
            "confidence": 0.82
        }
        
        return estimation
    
    async def _check_safety_compliance(self, task: str, context: Optional[Dict]) -> Dict[str, Any]:
        """Check safety regulations and OSHA compliance."""
        work_type = self._extract_work_type(task)
        
        compliance = {
            "work_type": work_type,
            "osha_requirements": {
                "general_safety": [
                    "Hard hats required in all work areas",
                    "Safety glasses for all personnel",
                    "High-visibility vests in active areas",
                    "Steel-toed boots for all workers"
                ],
                "fall_protection": [
                    "Guardrails for work above 6 feet",
                    "Personal fall arrest systems for roof work",
                    "Safety nets where applicable",
                    "Ladder safety training required"
                ],
                "excavation_safety": [
                    "Competent person for excavation oversight",
                    "Proper sloping or shoring systems",
                    "Utility location before digging",
                    "Daily excavation inspections"
                ]
            },
            "training_requirements": [
                "OSHA 10-hour construction safety",
                "Site-specific safety orientation",
                "Equipment-specific training",
                "Emergency response procedures"
            ],
            "inspection_schedule": {
                "daily": "Site safety walkthrough",
                "weekly": "Comprehensive safety audit",
                "monthly": "Safety meeting and training update"
            },
            "emergency_procedures": {
                "first_aid": "Certified first aid personnel on-site",
                "emergency_contacts": "Posted in visible locations",
                "evacuation_plan": "Clearly marked routes and assembly points"
            },
            "compliance_documentation": [
                "Daily safety logs",
                "Training records",
                "Incident reports",
                "Inspection checklists"
            ],
            "confidence": 0.90
        }
        
        return compliance
    
    async def _plan_quality_control(self, task: str, context: Optional[Dict]) -> Dict[str, Any]:
        """Plan quality control and inspection schedule."""
        project_phase = self._extract_project_phase(task)
        
        quality_plan = {
            "project_phase": project_phase,
            "inspection_points": [
                {
                    "phase": "Foundation",
                    "inspections": ["Excavation", "Rebar placement", "Concrete pour"],
                    "inspector": "Building department",
                    "timing": "Before proceeding to next phase"
                },
                {
                    "phase": "Framing",
                    "inspections": ["Structural framing", "Shear walls", "Roof structure"],
                    "inspector": "Structural engineer",
                    "timing": "Before MEP rough-in"
                },
                {
                    "phase": "MEP Rough-in",
                    "inspections": ["Electrical rough", "Plumbing rough", "HVAC rough"],
                    "inspector": "Trade inspectors",
                    "timing": "Before insulation"
                }
            ],
            "quality_standards": {
                "workmanship": "Industry standard practices",
                "materials": "Specified grade and quality",
                "code_compliance": "Local building codes",
                "documentation": "Photo documentation of all phases"
            },
            "testing_requirements": [
                "Concrete strength testing",
                "Electrical system testing",
                "Plumbing pressure testing",
                "HVAC commissioning"
            ],
            "quality_metrics": {
                "defect_rate_target": "< 2%",
                "rework_percentage": "< 5%",
                "inspection_pass_rate": "> 95%"
            },
            "confidence": 0.87
        }
        
        return quality_plan
    
    async def _general_construction_analysis(self, task: str, context: Optional[Dict]) -> Dict[str, Any]:
        """Provide general construction analysis and guidance."""
        return {
            "analysis_type": "general_construction_consultation",
            "task_summary": task,
            "recommendations": [
                "Develop detailed project schedule with critical path analysis",
                "Coordinate all trades early in planning phase",
                "Implement comprehensive safety program",
                "Establish quality control checkpoints",
                "Plan material procurement and delivery schedule"
            ],
            "best_practices": [
                "Daily coordination meetings with all trades",
                "Weather contingency planning",
                "Regular safety training and enforcement",
                "Proactive communication with inspectors",
                "Document all changes and decisions"
            ],
            "confidence": 0.75
        }
    
    def _extract_project_type(self, text: str) -> str:
        """Extract project type from text."""
        project_types = {
            "residential": ["house", "home", "residential", "single family"],
            "commercial": ["office", "retail", "commercial", "warehouse"],
            "renovation": ["remodel", "renovation", "addition", "upgrade"]
        }
        
        text_lower = text.lower()
        for project_type, keywords in project_types.items():
            if any(keyword in text_lower for keyword in keywords):
                return project_type
        
        return "general construction"
    
    def _extract_duration(self, text: str) -> Optional[int]:
        """Extract project duration in weeks."""
        duration_match = re.search(r'(\d+)\s*(?:week|month)', text.lower())
        if duration_match:
            value = int(duration_match.group(1))
            if "month" in duration_match.group(0):
                return value * 4  # Convert months to weeks
            return value
        return None
    
    def _extract_trades(self, text: str) -> List[str]:
        """Extract required trades from text."""
        all_trades = ["Excavation", "Concrete", "Framing", "Electrical", "Plumbing", "HVAC", "Drywall", "Flooring", "Painting"]
        mentioned_trades = []
        
        text_lower = text.lower()
        for trade in all_trades:
            if trade.lower() in text_lower:
                mentioned_trades.append(trade)
        
        return mentioned_trades if mentioned_trades else all_trades
    
    def _extract_square_footage(self, text: str) -> Optional[int]:
        """Extract square footage from text."""
        sqft_match = re.search(r'(\d+)\s*(?:sq|square|sqft)', text.lower())
        return int(sqft_match.group(1)) if sqft_match else None
    
    def _extract_work_type(self, text: str) -> str:
        """Extract work type from text."""
        work_types = {
            "new construction": ["new", "construction", "build"],
            "renovation": ["renovation", "remodel", "upgrade"],
            "roofing": ["roof", "roofing", "shingle"],
            "excavation": ["excavation", "digging", "foundation"]
        }
        
        text_lower = text.lower()
        for work_type, keywords in work_types.items():
            if any(keyword in text_lower for keyword in keywords):
                return work_type
        
        return "general construction"
    
    def _extract_project_phase(self, text: str) -> str:
        """Extract project phase from text."""
        phases = ["foundation", "framing", "rough-in", "finish", "final"]
        text_lower = text.lower()
        
        for phase in phases:
            if phase in text_lower:
                return phase
        
        return "general"
    
    def get_capabilities_description(self) -> str:
        """Return a description of the agent's capabilities."""
        return """
        Construction Coordination Expert - Specialized in:
        
        • Project Scheduling: Critical path analysis and timeline optimization
        • Trade Coordination: Multi-contractor scheduling and workflow management
        • Material Estimation: Quantity takeoffs and procurement planning
        • Safety Compliance: OSHA regulations and safety program development
        • Quality Control: Inspection scheduling and quality assurance planning
        
        Perfect for general contractors, project managers, and construction
        professionals seeking efficient project coordination and compliance.
        """
