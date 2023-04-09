import nox

nox.options.sessions = ["lint", "test"]


@nox.session
def lint(session):
    session.install("black", "isort", "flake8", "pydocstyle")
    session.run("black .")
    session.run("isort .")
    session.run("flake8")
    session.run("pydocstyle")


@nox.session
def test(session):
    session.install("pytest", "pytest-mock")
    session.run("pytest")
    session.notify("coverage")


@nox.session
def coverage(session):
    session.install("coverage")
    session.run("coverage")


@nox.session
def scan(session):
    session.install("bandit", "radon")
    session.run("bandit")
    session.run("radon")
