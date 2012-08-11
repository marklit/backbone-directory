from fabric.api import task, settings, roles, sudo, run, env, local


def backend():
    local('cd src && python manage.py run_gunicorn 0.0.0.0:8000')


def frontend():
    local('python -m SimpleHTTPServer')