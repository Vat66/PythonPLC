#!/bin/bash

# Install backend dependencies with pipenv
echo "Installing Flask backend dependencies with pipenv..."
cd server
pipenv install

# Install frontend dependencies with npm
echo "Installing React frontend dependencies..."
cd ../client
npm install
