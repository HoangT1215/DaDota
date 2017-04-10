import pandas as pd
import matplotlib.pyplot as plt
import urllib2
import requests as r

#send request GET to opendota

a = [{"id":0
	,"name":"string"
	,"localized_name":"string"
	,"img":"string"
	,"icon":"string"
	,"pro_win":0
	,"pro_pick":0
	,"hero_id":0
	,"pro_ban":0
	,"1000_pick":0
	,"1000_win":0
	,"2000_pick":0
	,"2000_win":0
	,"3000_pick":0
	,"3000_win":0,
	"4000_pick":0,
	"4000_win":0,
	"5000_pick":0,
	"5000_win":0}]
p = urllib2.urlopen("https://api.opendota.com/api/heroStats").read()
data = pd.io.json.json_normalize(p)
print data

