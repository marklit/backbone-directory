from fabric.api import local, task, env


@task
def test():
    """
    Runs unit tests and coverage tool on local codebase
    """
    local('cd src && coverage run --omit="*/migrations/*,*/.virtualenvs/*" '
        'manage.py test -v2 %s; coverage report; '
        'coverage annotate' % ' '.join(env.django_apps))


@task
def test_pep8(only_codes=None):
    """
    To filter on certain codes: fab pep8:E122
    """
    if only_codes is not None:
        select = '--select=%s' % only_codes
    else:
        select = '--ignore=W291,W293,E261'
    
    local('pep8 --exclude=migrations --show-source --show-pep8 '
        '--statistics %s src/ fabs/ fabfile.py' % select)


@task
def test_lint():
    """
    Reports on coding errors in any python files
    """
    local('pylint --ignore=migrations --errors-only src/ fabs/ fabfile.py')
