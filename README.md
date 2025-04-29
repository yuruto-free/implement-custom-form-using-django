# Implement custom form using Django
This repository is an example of implementing custom form such as Datalist form, restricted form and so on by using Django.

## Assumption
I assume that host environment follows below.

| Target | Detail | Command |
| :--- | :--- | :--- |
| Device | Raspberry Pi 4 Model B | `more /proc/device-tree/model` |
| Architecture | arm64v8 (aarch64)  | `uname -m` |
| OS | Debian GNU/Linux 11 (bullseye) | `cat /etc/os-release \| head -n 1` |

## Preparation
1. Install `git`, `docker`, and `docker-compose` to your pc and enable each service.
1. Run the following command and change working directory to the cloned directory.

    ```bash
    git clone https://github.com/tnakagami/asset-management.git
    ```

1. Create `.env` files by following markdown files.

    | Target | Path | Detail |
    | :--- | :---- | :--- |
    | Django | `./env_files/django/.env` | [README.md](./env_files/django/README.md) |
    | PostgreSQL | `./env_files/postgres/.env` | [README.md](./env_files/postgres/README.md) |

1. Create `.env` file in the top directory. This `.env` file consists of the following environment variables.

    | Environment variable name | Detail | Example |
    | :---- | :---- | :---- |
    | `HOST_ACCESS_PORT` | Port number used to connect to web server | 3001 |
    | `HOST_ARCHITECTURE` | Architecture of host machine | arm64v8 |
    | `HOST_TIMEZONE` | Time Zone in your pc | Asia/Tokyo |
    | `HOST_LANGCODE` | Language code of your country | ja |

1. Run the following command to create docker image.

    ```bash
    # In the host environment
    docker-compose build --no-cache --build-arg UID="$(id -u)" --build-arg GID="$(id -g)"
    ```

1. Check [README.md](./django/README.md) to initialize Django application.

## Execution
1. Run the following comand.

    ```bash
    # In the host environment
    docker-compose up -d
    ```

1. Access to `http://your-server-ip-address:${HOST_ACCESS_PORT}`.

    The default port number is 3001.
