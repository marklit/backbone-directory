from fabric.api import task, settings, roles, sudo, run, env, local


@task
def backend():
    """
    Run Backend API
    """
    local('cd src && python manage.py run_gunicorn %s' % env.backend_iface)


@task
def backend_dev():
    """
    Run Backend API (Restarts when .py's are changed)
    """
    local('cd src && python manage.py runserver %s' % env.backend_iface)


@task
def frontend():
    """
    Run Backend API
    """
    local('cd frontend && python -m SimpleHTTPServer %d' % env.frontend_port)
