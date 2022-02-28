import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session(name="clean")
def clean(session):
    session.run(*"ablog clean -D".split(), external=True)


@nox.session
def docs(session):
    session.install("-r", "requirements.txt")
    session.run(*"ablog build".split())
    session.log("open ./_website/index.html")


@nox.session
def linkcheck(session):
    session.install("-r", "requirements.txt")
    session.run(*"sphinx-build -b linkcheck . _website".split())


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-r", "requirements.txt")
    session.run(
        *"sphinx-autobuild --open-browser --ignore _website -b dirhtml . _website".split()
    )
