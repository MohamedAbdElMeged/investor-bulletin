
#!/bin/bash
sleep 10
echo "$(pwd)/investor_bulletin"
export PYTHONPATH="$(pwd)/investor_bulletin" && uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload



