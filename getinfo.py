import datacore.datacore as dc
import datacore.shipid

if __name__ == '__main__':
	for i in datacore.shipid.ship_all:
		dc.getinfo(i)