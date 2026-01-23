#!/bin/bash

# Test Creative HQ in a fresh Docker environment
# This simulates what a new user would experience

echo "🚀 Building fresh Creative HQ environment..."
echo ""

cd "$(dirname "$0")"

# Build and run
docker-compose build --no-cache
docker-compose run --rm creative-hq

echo ""
echo "Done! Container cleaned up."
