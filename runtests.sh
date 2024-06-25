source .envrc

cd tests

# random string for this run
export TEST_RUN_ID=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13)
export CLOUDICORN_NO_GIT_CHECK=1

set -eu

python3 -m pytest pytest_assertconf.py

function cleanup()
{
    echo "cleaning up..."
    python3 -m pytest pytest_teardown.py

}

trap cleanup EXIT TERM HUP 

for t in $(ls pytest_batch*); do
    python3 -m pytest $t
done
