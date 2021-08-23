#just a simple script to control the E-load to emulate the inrush current of the relays

import lab_equipment as lb
import time

relay = {
	"count" : 4,
	"inrush_current_a" : 4,
	"inrush_time_s" : 0.1,
	"holding_current_a" : 0.12,
	"time_between_activation_s" : 0.5
}

eload = lb.BK8600()
eload.set_current(0)
eload.toggle_eload(False)

def activate_relay():
	eload.set_current(relay["inrush_current_a"])
	time.sleep(relay["inrush_time_s"])
	eload.set_current(relay["holding_current_a"])
	time.sleep(relay["time_between_activation_s"])


def activate_sequence():
	eload.toggle_eload(True)
	
	for i in range(relay["count"]):
		print("Relay {}", i+1)
		activate_relay()
		
	eload.toggle_eload(False)


print("Starting")
activate_sequence()

print("Done")
