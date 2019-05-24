domains = {"Ukraine": "UA", "Germany": "DE", "GreatBritan": "UK"}
capitals = {"Ukraine": "Kyiv", "Germany": "Berlin", "GreatBritan": "London"}
for key in domains.keys():
    print("Domain for {} is {}".format(key, domains[key]))
for key in capitals.keys():
    print("Capital for {} is {}".format(key, capitals[key]))

for key in capitals.keys():
    print("Capital for {} is {} and domain is {}".format(key, capitals[key], domains[key]))
domainsCOM = {}
for key in domains.keys():
    domainsCOM[key] = "COM."+domains[key]
    print(key, domainsCOM[key])
domainsGOV = {}

for key in domains.keys():
    domainsGOV[key] = "GOV."+domains[key]
    print(key, domainsGOV[key])
