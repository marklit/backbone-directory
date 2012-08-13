from fabric.api import task, settings, roles, sudo, run, env, local


@task
def backend():
    """
    Run Frontend and Backend API w/ gevent
    """
    local('cd src && python manage.py run_gunicorn %s' % env.web_interface)


@task
def backend_dev():
    """
    Run Frontend and Backend API (Restarts when .py's are changed)
    """
    local('cd src && python manage.py runserver %s' % env.web_interface)

@task
def backend_tornado():
    """
    Run Frontend and Backend API w/ Tornado
    """
    local('cd src && python manage.py run_tornado --reload %s' % (
        env.web_interface,))