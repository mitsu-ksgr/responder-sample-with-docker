responder tutorial
==================

### Refs
- [taoufik07/responder: A familiar HTTP Service Framework for Python\.](https://github.com/taoufik07/responder)
- [Quick Start\! — responder 1\.3\.0 documentation](https://responder.kennethreitz.org/en/latest/quickstart.html)
- [Deploying Responder — responder 1\.3\.0 documentation](https://responder.kennethreitz.org/en/latest/deployment.html#docker-deployment)


#### run
```bash
$ docker-compose build
$ docker-compose up -d
$ docker-compose ps
Name      Command       State          Ports
----------------------------------------------------
web    python3 app.py   Up      0.0.0.0:8080->80/tcp
```

- http://localhost:8080/
- or exec `./quicktest.sh`


