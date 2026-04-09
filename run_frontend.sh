#!/bin/zsh
# Starts Next.js frontend dev server
# Run from project root

cd frontend
nvm use 20 2>/dev/null || true
npm run dev
