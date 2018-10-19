#!/bin/sh
#
# Purpose: Check the Block timestamp of Nodeos



# URL of Nodeos
URL="http://mainnet.eosnairobi.io"

# Sanity Check - Is node eveen up?
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL/v1/chain/get_info)


if [[ "$STATUS" == 200 ]]; then
  # If STATUS == 200
  DATA=$(curl -sb -H "Accept: application/json" "http://mainnet.eosnairobi.io/v1/chain/get_info")
  OUTPUT="SUCCESS"
  STATE=$STATE_OK

else
  OUTPUT="CRITICAL: The outgoing connection to $URL isn't reachable"
  DATA="Nothing"
  STATE=$STATE_CRITICAL
fi

# Sending the output message & Exit
echo $OUTPUT 
echo $DATA
exit $STATE
