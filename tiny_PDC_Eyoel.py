from synchrophasor.pdc import Pdc

pdc = Pdc(pdc_id=7, pmu_ip="127.0.0.1", pmu_port=4712)

pdc.run()  # Connect to PMU

header = pdc.get_header()  # Get header message from PMU
config = pdc.get_config()  # Get configuration from PMU

pdc.start()  # Request to start sending measurements

while True:
    data = pdc.get()  # Keep receiving data
    if not data:
        pdc.quit()  # Close connection
        break
