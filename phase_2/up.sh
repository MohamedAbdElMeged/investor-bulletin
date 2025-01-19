
docker compose -f docker-compose.yml up --build

sleep 3

# SETUP DATABASE ROLES AND PERMISSIONS
docker exec database sh -c "/cockroach/cockroach sql -u root --insecure  --host=database < /docker-entrypoint-initdb.d/init.sql"

