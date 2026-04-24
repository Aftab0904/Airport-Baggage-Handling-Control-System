import time
import random

class BaggageSystemSim:
    def __init__(self):
        self.conveyor_running = False
        self.diverter_status = True  # True = OK, False = Fault
        self.bag_id = None
        self.destination = None
        self.e_stop = False
        self.throughput_count = 0

    def trigger_scan(self, bag_id, dest):
        if self.e_stop:
            print("[ALERT] System in E-STOP. Cannot scan.")
            return
        self.bag_id = bag_id
        self.destination = dest
        print(f"[SCAN] Bag {bag_id} detected. Destination: Zone {dest}")
        self.run_logic()

    def run_logic(self):
        print("[PLC] Calculating routing path...")
        time.sleep(1)  # Simulate travel time
        
        if self.e_stop:
            print("[HALT] E-STOP triggered during transit.")
            return

        if self.destination == 1:
            if self.diverter_status:
                print(f"[ACTION] Diverter 1 Actuated. Bag {self.bag_id} routed successfully.")
                self.throughput_count += 1
            else:
                print(f"[FAULT] Diverter 1 Jammed! Rerouting Bag {self.bag_id} to Overflow Zone.")
        else:
            print(f"[LOGIC] Destination {self.destination} is downstream. Bag moving forward.")

    def simulate_failure(self):
        self.diverter_status = False
        print("[SCADA] Diverter 1 Fault Detected.")

    def trigger_estop(self):
        self.e_stop = True
        self.conveyor_running = False
        print("[CRITICAL] EMERGENCY STOP ACTIVATED.")

if __name__ == "__main__":
    system = BaggageSystemSim()
    
    print("--- Airport Baggage Handling Control System Simulation ---")
    
    # Normal Operation
    system.trigger_scan(bag_id=101, dest=1)
    
    # Failure Scenario: Diverter Jam
    print("\n--- Simulating Diverter Failure ---")
    system.simulate_failure()
    system.trigger_scan(bag_id=102, dest=1)
    
    # Critical Scenario: E-STOP
    print("\n--- Simulating Emergency Stop ---")
    system.trigger_estop()
    system.trigger_scan(bag_id=103, dest=1)
    
    print(f"\nFinal Throughput: {system.throughput_count} bags.")
