#!/bin/zsh
set -euo pipefail

REPO="/Users/natalie/paper-planes-skills"
HOST="178.130.50.200"
PORT="2222"
KEY="/Users/natalie/.ssh/paperplanes_frappe_selectel"
CONTAINER="learning-prod-backend-1"
BENCH="/home/frappe/frappe-bench"
SITE="lms.178.130.50.200.sslip.io"

cd "$REPO"
python3 scripts/prepare_frappe_payload.py

scp -q -i "$KEY" -P "$PORT" -o IdentitiesOnly=yes \
  registry/frappe_payload.json root@"$HOST":/tmp/skills_publish_payload.json
scp -q -i "$KEY" -P "$PORT" -o IdentitiesOnly=yes \
  scripts/frappe_apply_payload.py root@"$HOST":/tmp/frappe_apply_payload.py

ssh -i "$KEY" -p "$PORT" -o IdentitiesOnly=yes root@"$HOST" "
  docker cp /tmp/skills_publish_payload.json $CONTAINER:/tmp/skills_publish_payload.json &&
  docker cp /tmp/frappe_apply_payload.py $CONTAINER:$BENCH/apps/lms/lms/frappe_apply_payload.py &&
  docker exec -u frappe $CONTAINER bash -lc \
    'cd $BENCH && bench --site $SITE execute lms.frappe_apply_payload.main'
"
