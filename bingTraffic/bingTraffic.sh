#!/bin/bash
bingTraffic(){
curl http://dev.virtualearth.net/REST/v1/Traffic/Incidents/37,-105,45,-94?key=eqBURiWWTE5afcJ2IqYG~xNlJhANCoR7y-NsuhTEswQ~AtEBP9BiaYkAEDKsgHuJWI0lxmMWjE83qzFw3yUbZdoowdXKaCnaNbJKtUo5eb24 >> $(pwd)/result.json

}
