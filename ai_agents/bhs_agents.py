from crewai import Agent, Task, Crew, Process

class BHSAgentSystem:
    def __init__(self):
        self.agents = self.create_agents()

    def create_agents(self):
        # 1. PLC Logic Auditor
        logic_auditor = Agent(
            role='PLC Logic Auditor',
            goal='Analyze SCL control logic for logical errors, race conditions, and timing mismatches.',
            backstory="""You are a Senior PLC Engineer with 20 years of experience in Siemens S7-1500 and SCL. 
            You excel at identifying subtle bugs in baggage routing algorithms, such as travel time calculation 
            errors or improper handling of E-STOP states.""",
            verbose=True,
            allow_delegation=True
        )

        # 2. Network & Sensor Diagnostic Agent
        network_diagnostic = Agent(
            role='Network & Sensor Diagnostic Expert',
            goal='Analyze Profinet logs and sensor signals to identify hardware failures or communication delays.',
            backstory="""You specialize in industrial fieldbus communication and Profinet diagnostics. 
            You can tell if a 'Photo-eye blocked' signal is a real bag jam, a dirty sensor, or a network node timeout.
            Your expertise prevents unnecessary mechanical inspections for electrical issues.""",
            verbose=True,
            allow_delegation=False
        )

        # 3. Performance Analyst Agent
        performance_analyst = Agent(
            role='Performance & Throughput Analyst',
            goal='Monitor system throughput (BPH) and identify bottlenecks or congestion zones.',
            backstory="""You are an Industrial Data Scientist. You analyze the flow of baggage across 
            different conveyor segments. You provide insights on how to optimize belt speeds and gap control 
            to maximize throughput without causing jams.""",
            verbose=True,
            allow_delegation=False
        )

        # 4. Controls Lead Orchestrator
        controls_lead = Agent(
            role='Controls Lead Orchestrator',
            goal='Synthesize insights from all agents and the RAG knowledge base to provide actionable decisions.',
            backstory="""You are the project lead for an industrial automation system. You coordinate the commissioning 
            of the system. You take the technical reports from the logic, network, and performance experts 
            and cross-reference them with the Project Design Specifications (PDS) to make final operational calls.""",
            verbose=True,
            allow_delegation=True
        )

        return {
            'logic_auditor': logic_auditor,
            'network_diagnostic': network_diagnostic,
            'performance_analyst': performance_analyst,
            'controls_lead': controls_lead
        }

    def run_commissioning_audit(self, scl_code, log_data):
        # Define Tasks
        task1 = Task(
            description=f"Audit the following SCL code for logic errors: {scl_code}",
            agent=self.agents['logic_auditor'],
            expected_output="A report identifying potential logic bugs and timing issues."
        )

        task2 = Task(
            description=f"Analyze these logs for network/sensor issues: {log_data}",
            agent=self.agents['network_diagnostic'],
            expected_output="A diagnostic report distinguishing between hardware and software faults."
        )

        task3 = Task(
            description="Synthesize the findings and recommend the next steps for the commissioning team.",
            agent=self.agents['controls_lead'],
            expected_output="A final executive summary with a root cause analysis and action plan."
        )

        # Form the Crew
        bhs_crew = Crew(
            agents=[self.agents['logic_auditor'], self.agents['network_diagnostic'], self.agents['controls_lead']],
            tasks=[task1, task2, task3],
            process=Process.sequential
        )

        return bhs_crew.kickoff()

if __name__ == "__main__":
    # Example Usage
    system = BHSAgentSystem()
    print("CrewAI BHS Diagnostic System Initialized.")
