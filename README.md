# Learning celery
Simple repository designed to learn and test [celery](http://docs.celeryproject.org) related stuff.

## Prerequisites

At the bare minimum you'll need the following for your development environment:

1. [Python 3.6](http://www.python.org/)
2. [pyenv](https://github.com/pyenv/pyenv)
3. [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) or [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)
4. [Docker](https://www.docker.com/)
5. [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

### Cloning

```bash
$ git clone git@github.com:phillipemoreira/learning-celery.git
$ cd learning-celery
```

### Setting up python virtual environment

```bash
$ pyenv install 3.6.1
$ pyenv virtualenv 3.6.1 learning-celery
$ pyenv local learning-celery
```

#### Errors

If you receive one error of missing OpenSSL to run the `pyenv install`, you can try to fix running:

```bash
$ sudo apt install -y libssl1.0-dev
```

### Installation

```bash
$ make install
```

## Running

**TODO**

## Testing

**TODO**