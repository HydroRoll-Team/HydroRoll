import nox

nox.options.sessions = ["test"]


@nox.session
def test(python='.venv/Scripts/python.exe', reuse_venv=True):
    nox.session.env["MATURIN_PEP517_ARGS"] = "--profile=dev"
    nox.session.install(".[dev]")
    nox.session.run("pytest")


@nox.session
def bench(python='.venv/Scripts/python.exe', reuse_venv=True):
    nox.session.env["MATURIN_PEP517_ARGS"] = "--profile=dev"
    nox.session.install(".[dev]")
    nox.session.run("pytest", "--benchmark-enable")
