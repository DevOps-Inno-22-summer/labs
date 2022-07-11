FROM python:3.9.13-slim-bullseye AS env

RUN python3 -m venv /opt/env
RUN . /opt/env/bin/activate

COPY requirements.txt requirements.txt
RUN /opt/env/bin/pip install -r requirements.txt


FROM python:3.9.13-slim-bullseye AS prod

RUN adduser --home /app --shell /bin/sh --uid 1000 --disabled-password appuser
USER appuser

WORKDIR /app

COPY --from=env /opt/env /app/env
COPY . .

RUN mkdir /app/logs
RUN touch /app/logs/visits.log

CMD ["/app/env/bin/python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]
EXPOSE 5000
