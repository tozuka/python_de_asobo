# -*- coding: utf-8 -*-
import sys, os, re
import pickle

import openpnelib as op

import yaml
try:
  ## utilise LibYAML s'il existe
  from yaml import CLoader as Loader
  from yaml import CDumper as Dumper
except ImportError:
  ## sinon utilisions PyYAML
  from yaml import Loader, Dumper

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)


def usage():
  print "ルーティング名チェッカ。"
  print "　使い方: %s APP-ROOT" % sys.argv[0]


argv = sys.argv
argc = len(argv)
if argc < 2:
  usage();
  sys.exit(0)


path = argv[1]
if not op.is_symfony_app_directory(path):
  print "%s はSymfonyのディレクトリではありません" % path
  sys.exit(-1)

openpne_version = op.get_openpne_version(path)
if openpne_version == None:
  print "OpenPNEアプリケーションではないか、バージョンが不明です"
  sys.exit(-1)
elif not re.compile(r"3\.4\.").match(openpne_version):
  print "OpenPNE %s には対応していません" % openpne_version 
  sys.exit(-1)
else:
  print "このツールはOpenPNE %s に対応しています" % openpne_version

## APP ROOT
os.chdir(path)

#os.chdir(path)
#string = open('config/OpenPNE.yml').read().decode('utf8')
#data = yaml.load(string, Loader=Loader)
#pp.pprint(data)

routing_rules = {}

def read_routing_yml(app_name, app_dir, plugin_name=None):
  try:
    path = app_dir + '/config/routing.yml'
#    print "> reading %s..." % path
    if not os.access(path, os.F_OK|os.R_OK):
      return # file not found
    f = open(path,'r')
    # ルーティング名の順序を変えずに読み出したい
    buf = ""
    for line in f:
      if re.compile(r"^[ \t]*\n").match(line): # empty line
        buf += "---\n"
      else:
        buf += line.decode('utf8')
    for rule in yaml.load_all(buf, Loader=Loader):
      if app_name not in routing_rules:
        routing_rules[app_name] = []
      if rule != None:
        routing_rules[app_name].append(rule)
    f.close()
#    for rules in routing_rules[app_name]:
#      pp.pprint( rules )
  except ImportError:
    pass

def read_routing_yml_under_apps(apps_dir, plugin_name=None):
  if not os.access(apps_dir, os.R_OK):
    return
  for app in os.listdir(apps_dir):
    if app[0] == '.':
      continue
    if plugin_name != None:
      print 'プラグイン %s -- アプリケーション %s' % (plugin, app)
    else:
      print 'アプリケーション %s' % app
    app_dir = apps_dir + '/' + app
    read_routing_yml(app, app_dir, plugin_name)


## plugin/***Plugin/lib/routing/***RouteCollection.class.php
## <<< php読まないとダメですね

# apps/APPLICATION/config/routing.yml
read_routing_yml_under_apps('apps')

# apps/APPLICATION/config/routing.yml
for plugin in os.listdir("plugins"):
  if plugin[0] == ".":
    continue
  read_routing_yml_under_apps('plugins/' + plugin + '/apps', plugin)

for app,rules in routing_rules.iteritems():
  print "アプリケーション %s" % app
  for rule in rules:
    for route_name,settings in rule.iteritems():
      url = None
      param = {}
      if 'param' in settings:
        param = settings['param']
      if 'url' in settings:
        url = settings['url']
      if param and 'action' in param and 'module' in param:
        action = param['action']
        module = param['module']
#        pp.pprint(param)
#        print "%s <-- '@%s' <-- %s/%s" % (url,route_name,action,module)
        print "  s|'%s/%s|'@%s|g  # %s" % (action,module, route_name, url)

#os.chdir("apps")
#os.chdir("..")
#apps * config/routing.yml


#pp.pprint( os.listdir(".") )


#if access(

#string = open('example.yaml').read()
#string = string.decode('utf8')
#data = yaml.load(string, Loader=Loader)


#pp.pprint(data)


#data = [ 'hello', {'x':10, 'y':20}, {'x':15, 'y':25} ]
#print yaml.dump(data, Dumper=Dumper)

