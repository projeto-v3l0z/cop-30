FROM alpine:latest

RUN apk update && apk add --no-cache zsh git python3 py3-pip tzdata pkgconfig
# adicionar as dependencias do mysql
RUN apk add --no-cache mysql-dev gcc musl-dev python3-dev libffi-dev openssl-dev gettext

SHELL ["/bin/zsh", "-c"]

RUN sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN ln -fs /usr/share/zoneinfo/America/Belem /etc/localtime
RUN echo "America/Belem" > /etc/timezone

WORKDIR /app

COPY requirements.txt .
RUN pip install --break-system-packages -r requirements.txt


COPY . .

EXPOSE 8000