#!/usr/bin/env sh

echo 'Installing serve just for testing our app can be delivered correctly'
set -x
npm install -g serve
set +x

echo 'Run the build result using serve and test your react app use this'
set -x
serve -s build &
sleep 1
echo $! > .pidfile
set +x

echo 'Now...'
echo 'Visit http://localhost:3000 to see your Node.js/React application in action.'
