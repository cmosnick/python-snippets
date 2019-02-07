counts = [{u'MN077': 1182271858.7694633, u'WA673': 1073538697.537076}, {u'MN077': 3426428429.658165}, {u'WA762': 5881062178.455971, u'WA774': 1807980204.880361, u'WA673': 1014335235.3638974}, {u'WA774': 949337316.5546284, u'WA749': 2802251954.306837}]

counts_agg = {}
for obj in counts:
	for key, count in obj.items():
		if key in counts_agg.keys():
			counts_agg[key] += count
		else:
			counts_agg[key] = count

print counts_agg