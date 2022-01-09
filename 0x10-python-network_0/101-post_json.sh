#!/bin/bash
# displays only the status code of the response.
curl -s -d @$2 -H "content-Type: application/json" -X POST "$1"
