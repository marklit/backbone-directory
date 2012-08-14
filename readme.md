# Technical Demo #

I forked [backbone-directory](https://github.com/ccoenraets/backbone-directory) to use as a boilerplate codebase.

This demo uses among other technologies the following:

 * [backbone.js](http://backbonejs.org/) (Frontend MVC)
 * [D3](http://d3js.org/) (Charting)
 * [Solr](http://lucene.apache.org/solr/) (Search)
 * [Tastypie](http://tastypieapi.org/) (API Framework for Django)
 * [Tornado](http://www.tornadoweb.org/) (Non-blocking Web Server)

You can view a live demo if this app here: [ec2-23-22-192-67.compute-1.amazonaws.com](http://ec2-23-22-192-67.compute-1.amazonaws.com:8000/)

## Installation ##

If you're using a fresh installation of Ubuntu 12+ then you might need some packages installed first:

```bash
$ sudo apt-get update && \
  sudo apt-get install python-pip python-virtualenv virtualenvwrapper \
                        git-core build-essential python2.7-dev \
                        libevent-1.4-2 libevent1-dev python-gevent
```

If you don't have a copy of Solr installed then have a look at these [installation notes](http://feinan.com/2012/05/19/how-to-install-solr-3-6-0-on-ubuntu-12-04-lts/).

Clone a copy of this codebase from github:

```bash
$ cd ~ && git clone https://github.com/marklit/backbone-directory.git
```

Create a virtual environment.

I usually hide my virtualenv folders in `~/.virtualenvs`. If you don't have this folder then create it with the following: `mkdir ~/.virtualenvs`.

Then, setup the virtualenv and activate it:

```bash
$ cd ~/.virtualenvs && \
  virtualenv backbone-directory && \
  source ~/.virtualenvs/backbone-directory/bin/activate
```

Go into the root folder of this repo and install the requirements.

```bash
pip install -r requirements.txt
```

Then setup the database and import the fixture data.

```bash
 $ cd ~/backbone-directory/src && \
   python manage.py syncdb && \
   python manage.py migrate && \
   python manage.py loaddata contacts photos
```

Create a new solr `schema.xml`.

```bash
 $ cd ~/backbone-directory/src && \
   python manage.py build_solr_schema
```

Take the XML portion of the output from above and place it in `/etc/solr/conf/schema.xml`.

Once that's in place, rebuild the solr indices:

```bash
 $ cd ~/backbone-directory/src && \
   python manage.py rebuild_index
```

Test everything is working nicely.

I try and keep a lot of the commands in `fabric` when possible. `cd` into the root of the repo and run the follow commands to test everything is looking okay:

```bash
 $ fab test_lint
 $ fab test_pep8
 $ fab test
```

It's pretty likely `test_lint` and `test_pep8` will have some complaints. `test` shouldn't have any issues, if it does, there are problems in the code and or the environment that need to be addressed.

Run the webserver with the following:

```bash
 $ fab backend_tornado
```

This will bind the server to `0.0.0.0:8000` and launch it.

If you want to dump your contacts or photos table into the default fixtures run the following:

```bash
 $ fab update_fixtures
```