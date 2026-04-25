# AI-Augmented Baggage Handling Control System (PLC + RAG + Multi-Agent)

This project has been upgraded from a standard PLC control project to an AI-augmented Industrial System. It combines deterministic Siemens S7-1500 logic (SCL) with an advisory layer powered by CrewAI and LangGraph.

## Key Upgrades

### 1. Multi-Agent Diagnostic Layer (CrewAI)
We have implemented 4 specialized AI agents to assist in system commissioning and troubleshooting:
- PLC Logic Auditor: Analyzes SCL code for race conditions and timing mismatches.
- Network & Sensor Diagnostic Expert: Distinguishes between mechanical jams and Profinet communication issues.
- Performance & Throughput Analyst: Monitors BPH (Bags Per Hour) and optimizes belt speeds.
- Controls Lead Orchestrator: Synthesizes reports from all agents and provides final operational decisions.

### 2. Autonomous Troubleshooting Workflow (LangGraph)
A state-machine based workflow that automatically triggers when a sensor fault is detected.
- Scenario: If a 'Photo-eye blocked' signal stays high for > 5 seconds.
- Action: Agent 1 (Network Monitor) verifies signal integrity -> Agent 2 (Logic Auditor) checks the SCL timer setpoints -> Orchestrator generates a root cause analysis.

### 3. Modular PLC Library (SCL)
The monolithic FB_BaggageRouting has been refactored into a modular library for better maintainability and code reuse:
- FC_Kinematics: Pure calculation block for travel times.
- FB_BagTracking: State-machine block for tracking bags in transit.
- FB_DivertControl: Actuation and feedback monitoring block.

## New File Structure
```text
/ai_agents
  ├── bhs_agents.py       # CrewAI agent definitions
  └── bhs_workflow.py     # LangGraph troubleshooting workflow
/plc_logic
  ├── Routing_Logic.scl   # Legacy monolithic block
  └── /modular_library    # New modular SCL components
      ├── FC_Kinematics.scl
      ├── FB_BagTracking.scl
      └── FB_DivertControl.scl
```

## How to Run the AI Simulation
1. Install dependencies:
   ```bash
   pip install crewai langgraph
   ```
2. Run the Multi-Agent audit:
   ```bash
   python ai_agents/bhs_agents.py
   ```
3. Run the LangGraph diagnostic workflow:
   ```bash
   python ai_agents/bhs_workflow.py
   ```

## Industrial Positioning
This system positions AI as an Advisory Layer. The PLC remains the deterministic controller for safety and real-time routing, while the AI agents provide Expert Engineer Support to reduce downtime and accelerate commissioning.
