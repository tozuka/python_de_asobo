# -*- coding: utf-8 -*-
import os,re

#
# Symfonyな話
#
def is_symfony_app_directory(path="."):
  if not os.access(path, os.F_OK|os.R_OK):
    return False
  for subdir in ["lib", "lib/vendor/symfony", "config", "apps", "plugins", "data"]:
    if not os.access(path + "/" + subdir, os.F_OK|os.R_OK):
      return False
  return True

def get_symfony_version(path="."):
  return None

#
# OpenPNE固有の話
#
def is_openpne_app_directory(path="."):
  return is_symfony_app_directory(path)

def get_openpne_version(path="."):
  openpne_version = None
  try:
    f = open(path + '/data/version.php','r')
    p = re.compile("define\('OPENPNE_VERSION', ?'([.0-9]+)'\);")
    for line in f:
      matched = p.search(line)
      if matched != None:
        openpne_version = matched.group(1)
    f.close()
  except IOError:
    pass
  # print "未対応のOpenPNEバージョン"
  #sys.exit(0)
  return openpne_version
