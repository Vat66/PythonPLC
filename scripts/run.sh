#!/bin/bash

# Start Flask backend using pipenv in the background
echo "Starting Flask backend server..."
cd server
python app.py &
BACKEND_PID=$!

# Start React frontend (Vite) in the background
echo "Starting React frontend (Vite)..."
cd ../client
npm run dev &
FRONTEND_PID=$!

# Wait for both processes to finish
wait $BACKEND_PID $FRONTEND_PID
