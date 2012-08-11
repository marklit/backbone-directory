from fabric.api import task, settings, roles, sudo, run, env, local


@task
def backend():
    """
    Run Backend API
    """
    local('cd src && python manage.py run_gunicorn %s' % env.web_interface)


@task
def backend_dev():
    """
    Run Backend API (Restarts when .py's are changed)
    """
    local('cd src && python manage.py runserver %s' % env.web_interface)