# Technical Demo #

I forked [backbone-directory](https://github.com/ccoenraets/backbone-directory) to use as a boiler plate code base.

This demo uses among other technologies the following:

 * [D3](http://d3js.org/)
 * [backbone.js](http://backbonejs.org/)
 * [Solr](http://lucene.apache.org/solr/)

## Installation ##

1. Create a virtual environment

```bash
$ cd ~/.virtualenvs && \
  virtualenv backbone-directory && \
  source ~/.virtualenvs/backbone-directory/bin/activate
```

2. Go into the root folder of this repo and install the requirements

```bash
pip install -r requirements.txt
```

3. Then setup the database and import the fixture data

```bash
 $ cd src && \
   python manage.py syncdb && \
   python manage.py migrate && \
   python manage.py loaddata contacts photos
```

4. Create a new solr schema.xml

```bash
 $ cd src && \
   python manage.py build_solr_schema
```

Take the XML portion of the output from above and place it in `/etc/solr/conf/schema.xml`.

Once that's in place, rebuild the solr indices:

```bash
 $ cd src && \
   python manage.py rebuild_index
```

5. Test everything is working nicely

I try and keep a lot of the commands in `fabric` when possible. `cd` into the root of the repo and run the follow commands to test everything is looking okay:

```bash
 $ fab test_lint test test_pep8
```

It's pretty likely pylint and pep8 will have some complaints. `test` shouldn't have any issues, if it does, there are problems in the code and or the environment that need to be addressed.

6. Run the webserver

```bash
 $ fab backend_dev
```

7. If you want to dump your contacts or photos table into the default fixtures run the following:

```bash
 $ fab update_fixtures
```