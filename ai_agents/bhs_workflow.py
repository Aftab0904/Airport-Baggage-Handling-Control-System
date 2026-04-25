from typing import TypedDict, List
from langgraph.graph import StateGraph, END

# Define the state schema
class AgentState(TypedDict):
    sensor_signal: str
    duration: float
    profinet_status: str
    scl_logic_audit: str
    diagnostic_result: str

# Node 1: Network Monitor Agent
def network_monitor_node(state: AgentState):
    print("--- [Agent 1] Monitoring Profinet Logs ---")
    # Scenario: Photo-eye blocked signal stays high for > 5 seconds
    if state['duration'] > 5.0 and state['sensor_signal'] == "BLOCKED":
        return {"profinet_status": "CRITICAL: Sensor PEC_1201 remains BLOCKED. Possible Jam or Hardware Failure."}
    return {"profinet_status": "NORMAL: Sensor signals within expected parameters."}

# Node 2: SCL Logic Auditor Agent
def logic_auditor_node(state: AgentState):
    print("--- [Agent 2] Auditing SCL Code for Timing Mismatch ---")
    if "CRITICAL" in state['profinet_status']:
        # Simulating SCL audit: Checking if the Fault Timer in SCL is set too high or low
        return {"scl_logic_audit": "LOGIC AUDIT: Travel_Timer setpoint (5s) matches physical distance. Logic is correct."}
    return {"scl_logic_audit": "LOGIC AUDIT: No issues found."}

# Node 3: Orchestrator / Decision Node
def orchestrator_node(state: AgentState):
    print("--- [Orchestrator] Generating Final Diagnostic ---")
    if "CRITICAL" in state['profinet_status'] and "correct" in state['scl_logic_audit']:
        return {"diagnostic_result": "ROOT CAUSE: Mechanical Jam at Diverter #4. Sensor is functioning correctly, Logic is correct. Request Maintenance."}
    elif "CRITICAL" in state['profinet_status']:
         return {"diagnostic_result": "ROOT CAUSE: Possible Sensor Stuck or Logic Delay. Inspect PEC_1201 hardware."}
    return {"diagnostic_result": "System Healthy."}

# Build the Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("monitor", network_monitor_node)
workflow.add_node("audit", logic_auditor_node)
workflow.add_node("orchestrate", orchestrator_node)

# Set Entry Point
workflow.set_entry_point("monitor")

# Define Edges
workflow.add_edge("monitor", "audit")
workflow.add_edge("audit", "orchestrate")
workflow.add_edge("orchestrate", END)

# Compile
app = workflow.compile()

def run_diagnostic(sensor_signal, duration):
    inputs = {
        "sensor_signal": sensor_signal,
        "duration": duration,
        "profinet_status": "",
        "scl_logic_audit": "",
        "diagnostic_result": ""
    }
    result = app.invoke(inputs)
    print(f"\nFINAL DIAGNOSTIC REPORT:\n{result['diagnostic_result']}")

if __name__ == "__main__":
    print("Running LangGraph BHS Workflow Simulation...")
    run_diagnostic("BLOCKED", 6.2)
