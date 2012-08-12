from fabric.api import task, settings, roles, sudo, run, env, local


@task
def update_fixtures():
    """
    Dump the current copy of certain tables into fixture files
    """
    dump_cmd = 'cd src && python manage.py dumpdata --indent=4'
    
    data_sets_and_targets = (
        ('contacts.city contacts.department contacts.person', 'contacts', 
            'contacts'),
        ('photos.photo', 'photos', 'photos'),
    )
    
    for (model, app, fixture) in data_sets_and_targets:
        local('%s %s> %s/fixtures/%s.json' % (dump_cmd, model, app, fixture))
