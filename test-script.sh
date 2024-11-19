#!/bin/bash

# Test API from repo1
response=$(curl -s http://kube-test-service/repo1-api)
echo "Repo1 Response: $response"

# Pass response to repo2 and test
result=$(curl -s -X POST http://kube-test-service/repo2-api -d "data=$response")
echo "Repo2 Result: $result"

if [[ "$result" == *"expected-output"* ]]; then
  echo "Test Passed!"
  exit 0
else
  echo "Test Failed!"
  exit 1
fi
