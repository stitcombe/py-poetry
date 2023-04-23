import nox
import tempfile

nox.options.sessions = ["lint", "test", "scan"]


@nox.session
def lint(session):
    session.install("ruff", "black")
    session.run("ruff check .")
    session.run("black .")


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
    session.notify("safety")


@nox.session
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
