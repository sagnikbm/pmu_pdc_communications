# pmu_pdc_communications
tinyPMU.py to tinyPMU5.py will create 5 PMUs waiting for a PDC to connect
tinPDCmultiple.py will connect to all of the 5 PMUs created in the above step.
You can then run superPDC.py to connect to the tinPDCmultiple.py PDC.
This is one part of the grid network.
Future plans are to aggregate the measurements received at tinPDCmultiple.py and then relay it to superPDC.py. Right now it just
sends out random data.
