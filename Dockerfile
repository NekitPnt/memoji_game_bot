FROM python:3.10
# set work directory
WORKDIR /usr/src/memoji_game_bot/
# copy project
COPY . /usr/src/memoji_game_bot/
# install dependencies
#RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt
# run app
CMD ["python", "-m", "memoji_game_bot.bot"]