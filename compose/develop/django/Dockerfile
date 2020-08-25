FROM python:3.6-alpine

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # System utilities
  && apk add curl \
  # Create user
  && addgroup -S django && adduser -S -G django django \
  && apk add postgresql-client

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/development.txt \
    && rm -rf /requirements

COPY ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start && chown django /start
COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app
