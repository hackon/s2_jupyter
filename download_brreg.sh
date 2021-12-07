#!/bin/sh

wget https://data.brreg.no/enhetsregisteret/api/enheter/lastned

mv lastned brreg.json.gz

gunzip brreg.json.gz