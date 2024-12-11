#!/bin/bash

# Start Flask backend using pipenv
echo "Starting Flask backend server..."
cd server
pipenv run python app.py &
BACKEND_PID=$!

# Start React frontend (Vite)
echo "Starting React frontend (Vite)..."
cd ../client
npm run dev &
FRONTEND_PID=$!

# Wait for both processes
echo "Frontend is running at http://localhost:5173"
echo "Backend is running at http://localhost:5000"
wait $BACKEND_PID $FRONTEND_PID
