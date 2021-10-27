import pygeoip # pip install pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('2.112.70.194')
for key, val in res.items():
    print('%s : %s' % (key, val))
    # Ciao a tutti