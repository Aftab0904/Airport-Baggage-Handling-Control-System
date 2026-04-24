# SCADA/HMI Visualization Specs
## System: Airport Baggage Handling Control

### 1. Communication Interface
- **Protocol**: Profinet (Simulated via TCP/IP)
- **Update Rate**: 100ms
- **PLC IP Address**: 192.168.0.10
- **HMI IP Address**: 192.168.0.20

### 2. Tag Mapping (PLC to HMI)
| Object Name | PLC Tag (SCL) | Data Type | HMI Animation |
| :--- | :--- | :--- | :--- |
| Conveyor_Motor | o_Conveyor_Run | Bool | Green (Running) / Grey (Off) |
| Diverter_Arm | o_Divert_Command | Bool | Linear Movement (0-100%) |
| System_Status | o_System_Fault | Bool | Red Blinking (Fault) / Grey (OK) |
| Bag_Counter | s_Success_Count | DInt | Numeric Display |
| Emergency_Stop | i_Emergency_Stop | Bool | Red Graphic Overlays |

### 3. HMI Screens
#### Screen 01: Main Layout (System Overview)
- 2D representation of the conveyor loop.
- Dynamic "Bag" graphics that move based on `s_Travel_Timer.ET`.
- Start/Stop/Reset buttons.

#### Screen 02: Diagnostics & Faults
- Real-time alarm log for diverter jams.
- Profinet node status (Health Check).
- Motor current feedback (Simulated).

#### Screen 03: Performance Metrics
- Throughput calculation (Bags per hour).
- Efficiency Percentage (Successful Diverts / Total Scans).
