# ula

Slack-integrated web app that allows users to challenge each other to build healthy habits



https://user-images.githubusercontent.com/8964784/151279085-2c9fa01e-3acc-40fa-ba46-9234d3e7a27c.mov


#### Running the app locally

0. Open Rosetta Terminal
1. `pyenv activate venv3`
2. `cd bot && python3 app.py`
3. `ngrok http 3000`
4. Assign https ngrok url + '/slack/events' to Event Subscriptions at https://api.slack.com/
