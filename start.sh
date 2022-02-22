echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/madibag/NEAEA_12_BOT /Grade12
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/madibag/NEAEA_12_BOT -b $BRANCH /Grade12
fi
cd /Grade12
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
