#!/bin/bash
bingTraffic(){
curl http://dev.virtualearth.net/REST/v1/Traffic/Incidents/mapArea/includeLocationCodes?severity=severity1,severity2,severityn\&type=type1,type2,typen\&key=eqBURiWWTE5afcJ2IqYG~xNlJhANCoR7y-NsuhTEswQ~AtEBP9BiaYkAEDKsgHuJWI0lxmMWjE83qzFw3yUbZdoowdXKaCnaNbJKtUo5eb24 >> $(pwd)/result.json

}
