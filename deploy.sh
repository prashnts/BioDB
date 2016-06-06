echo "${$(cat igloo/_config.sample.py)/\$module_dir/$(pwd)}" >! igloo/_config.py
npm install
npm run firstrun
