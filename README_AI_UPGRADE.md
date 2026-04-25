# Industrial Intelligence Upgrade: S7-1500 + RAG Advisory

This document outlines the transition from a standard baggage control project to an **AI-Augmented Industrial Framework**. By combining the deterministic reliability of Siemens SCL with modern RAG (Retrieval-Augmented Generation) architectures, we have created a system that minimizes commissioning risks and maximizes operational uptime.

## Core Architectural Enhancements

### 1. Multi-Agent Diagnostic Engine (CrewAI)
The system leverages a "Digital Expert Panel" to diagnose faults. Unlike static alarm systems, these agents perform multi-dimensional analysis:
- **PLC Logic Auditor:** Investigates the SCL source code for race conditions or edge cases in the divert timing logic.
- **Network & Sensor Specialist:** Analyzes the Profinet GSDML parameters and real-time heartbeat logs to isolate fieldbus noise from sensor failures.
- **Performance Optimization Agent:** Continuously audits the Bags-Per-Hour (BPH) metrics to suggest belt speed adjustments based on peak flight schedules.
- **Lead Orchestrator:** Collates all technical findings into a human-readable "Action Report" for the maintenance team.

### 2. Stateful Troubleshooting Workflows (LangGraph)
We have moved beyond simple "If-Then" logic. Using LangGraph, we've implemented state-machine-driven diagnostics that simulate a human engineer's thought process:
- **Trigger:** High-signal detected on a Photo-eye for > 5 seconds.
- **State 1:** Query Network Agent for Profinet node health.
- **State 2:** Query RAG for the sensor's technical datasheet to check blind-spot specifications.
- **State 3:** Final Root Cause Analysis (RCA) generation.

### 3. High-Performance Modular Library
The PLC logic has been refactored for the S7-1500 platform to support a "Plug-and-Play" commissioning model:
- **FC_Kinematics:** A stateless block for high-precision travel time calculations.
- **FB_BagTracking:** A robust state-machine for tracking baggage IDs through complex routing matrices.
- **FB_DivertControl:** A hardware abstraction layer that simplifies the management of pneumatic and motorized diverters.

## Implementation & Validation

### Setup Instructions
1.  **Python Environment:**
    ```bash
    pip install crewai langgraph matplotlib seaborn
    ```
2.  **Logic Audit:**
    Run the multi-agent diagnostic simulation:
    ```bash
    python ai_agents/bhs_agents.py
    ```
3.  **Workflow Verification:**
    Execute the LangGraph troubleshooting state-machine:
    ```bash
    python ai_agents/bhs_workflow.py
    ```

## Strategic Impact
This upgrade transforms the control system from a reactive component to a proactive asset. By reducing the reliance on manual document searching, the AI Advisory Layer reduces the Mean Time to Repair (MTTR) and ensures that commissioning engineers can focus on high-level system optimization rather than repetitive troubleshooting.
