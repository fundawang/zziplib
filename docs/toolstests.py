#! /usr/bin/python3

import sys
print(sys.path)
sys.path += ["."]
print(sys.path)

from tools import md2dbk
from unittest import TestCase, TestSuite, TextTestRunner, main
from fnmatch import fnmatchcase as matches

import logging
logg = logging.getLogger("TOOLS")

class md2dbkTests(TestCase):
    def test_1000(self):
        b = md2dbk.blocks("")
        self.assertEqual(b, [])
    def test_1001(self):
        b = md2dbk.blocks("a")
        self.assertEqual(b, ["a\n"])
    def test_1002(self):
        b = md2dbk.blocks("a\n")
        self.assertEqual(b, ["a\n"])
    def test_1003(self):
        b = md2dbk.blocks("a\nb")
        self.assertEqual(b, ["a\nb\n"])
    def test_1004(self):
        b = md2dbk.blocks("a\nb\n")
        self.assertEqual(b, ["a\nb\n"])
    def test_1005(self):
        b = md2dbk.blocks("a\nb\n\nc")
        self.assertEqual(b, ["a\nb\n", "c\n"])
    def test_1006(self):
        b = md2dbk.blocks("a\nb\n\nc\n")
        self.assertEqual(b, ["a\nb\n", "c\n"])
    def test_1007(self):
        b = md2dbk.blocks("a\nb\n\n\nc")
        self.assertEqual(b, ["a\nb\n", "c\n"])
    def test_1008(self):
        b = md2dbk.blocks("a\nb\n\n\nc\n")
        self.assertEqual(b, ["a\nb\n", "c\n"])
    def test_1009(self):
        b = md2dbk.blocks("a\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a\nb\n", "c\n"])
    def test_1010(self):
        b = md2dbk.blocks("a *xx*\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a *xx*\nb\n", "c\n"])
    def test_1011(self):
        b = md2dbk.blocks("a **xx**\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a **xx**\nb\n", "c\n"])
    def test_1012(self):
        b = md2dbk.blocks("a _xx_\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a _xx_\nb\n", "c\n"])
    def test_1013(self):
        b = md2dbk.blocks("a __xx__\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a __xx__\nb\n", "c\n"])
    def test_1014(self):
        b = md2dbk.blocks("a `xx`\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a `xx`\nb\n", "c\n"])
    def test_1015(self):
        b = md2dbk.blocks("a ``xx``\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a ``xx``\nb\n", "c\n"])
    def test_1016(self):
        b = md2dbk.blocks("a [xx]\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a [xx]\nb\n", "c\n"])
    def test_1017(self):
        b = md2dbk.blocks("a [xx](foo)\nb\n\n\nc\n\n")
        self.assertEqual(b, ["a [xx](foo)\nb\n", "c\n"])
    def test_1101(self):
        b = md2dbk.blocks("# a")
        self.assertEqual(b, ["# a\n"])
    def test_1102(self):
        b = md2dbk.blocks("## a")
        self.assertEqual(b, ["## a\n"])
    def test_1103(self):
        b = md2dbk.blocks("### a")
        self.assertEqual(b, ["### a\n"])
    def test_1104(self):
        b = md2dbk.blocks("#### a")
        self.assertEqual(b, ["#### a\n"])
    def test_1105(self):
        b = md2dbk.blocks("##### a")
        self.assertEqual(b, ["##### a\n"])
    def test_1106(self):
        b = md2dbk.blocks("###### a")
        self.assertEqual(b, ["###### a\n"])
    def test_1111(self):
        b = md2dbk.blocks("# a\n# b")
        self.assertEqual(b, ["# a\n# b\n"])
    def test_1112(self):
        b = md2dbk.blocks("## a\n## b")
        self.assertEqual(b, ["## a\n## b\n"])
    def test_1113(self):
        b = md2dbk.blocks("### a\n## b")
        self.assertEqual(b, ["### a\n## b\n"])
    def test_1114(self):
        b = md2dbk.blocks("#### a\n## b")
        self.assertEqual(b, ["#### a\n## b\n"])
    def test_1115(self):
        b = md2dbk.blocks("##### a\n## b")
        self.assertEqual(b, ["##### a\n## b\n"])
    def test_1116(self):
        b = md2dbk.blocks("###### a\n## b")
        self.assertEqual(b, ["###### a\n## b\n"])
    def test_1121(self):
        b = md2dbk.blocks("# a\n b")
        self.assertEqual(b, ["# a\n b\n"])
    def test_1122(self):
        b = md2dbk.blocks("## a\n b")
        self.assertEqual(b, ["## a\n b\n"])
    def test_1123(self):
        b = md2dbk.blocks("### a\n b")
        self.assertEqual(b, ["### a\n b\n"])
    def test_1124(self):
        b = md2dbk.blocks("#### a\n b")
        self.assertEqual(b, ["#### a\n b\n"])
    def test_1125(self):
        b = md2dbk.blocks("##### a\n b")
        self.assertEqual(b, ["##### a\n b\n"])
    def test_1126(self):
        b = md2dbk.blocks("###### a\n b")
        self.assertEqual(b, ["###### a\n b\n"])
    def test_1131(self):
        b = md2dbk.blocks("a\n===")
        self.assertEqual(b, ["# a\n"])
    def test_1132(self):
        b = md2dbk.blocks("a\n---")
        self.assertEqual(b, ["## a\n"])
    def test_1133(self):
        b = md2dbk.blocks("a\n===\nb")
        self.assertEqual(b, ["# a\nb\n"])
    def test_1134(self):
        b = md2dbk.blocks("a\n---\nb")
        self.assertEqual(b, ["## a\nb\n"])
    def test_1135(self):
        b = md2dbk.blocks("a\n===\n## b")
        self.assertEqual(b, ["# a\n## b\n"])
    def test_1136(self):
        b = md2dbk.blocks("a\n---\n## b")
        self.assertEqual(b, ["## a\n## b\n"])
    def test_1141(self):
        b = md2dbk.blocks("a\n===\n\n")
        self.assertEqual(b, ["# a\n"])
    def test_1142(self):
        b = md2dbk.blocks("a\n---\n\n")
        self.assertEqual(b, ["## a\n"])
    def test_1143(self):
        b = md2dbk.blocks("a\n===\n\n\nb")
        self.assertEqual(b, ["# a\n", "b\n"])
    def test_1144(self):
        b = md2dbk.blocks("a\n---\n\n\nb")
        self.assertEqual(b, ["## a\n", "b\n"])
    def test_1145(self):
        b = md2dbk.blocks("a\n===\n\n\n## b")
        self.assertEqual(b, ["# a\n", "## b\n"])
    def test_1146(self):
        b = md2dbk.blocks("a\n---\n\n\n## b")
        self.assertEqual(b, ["## a\n", "## b\n"])
    def test_1151(self):
        b = md2dbk.blocks("# a\n\n\nb")
        self.assertEqual(b, ["# a\n", "b\n"])
    def test_1152(self):
        b = md2dbk.blocks("## a\n\nb")
        self.assertEqual(b, ["## a\n", "b\n"])
    def test_1153(self):
        b = md2dbk.blocks("### a\n\n\n\nb")
        self.assertEqual(b, ["### a\n", "b\n"])
    def test_1154(self):
        b = md2dbk.blocks("#### a\n\n\nb")
        self.assertEqual(b, ["#### a\n", "b\n"])
    def test_1155(self):
        b = md2dbk.blocks("##### a\n\n\n## b")
        self.assertEqual(b, ["##### a\n", "## b\n"])
    def test_1156(self):
        b = md2dbk.blocks("###### a\n\n\n## b")
        self.assertEqual(b, ["###### a\n", "## b\n"])
    def test_1201(self):
        b = md2dbk.blocks("* a\n\n\n")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "</itemizedlist>"])
    def test_1202(self):
        b = md2dbk.blocks("* a\n\n\nb")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "</itemizedlist>", "b\n"])
    def test_1203(self):
        b = md2dbk.blocks("* a\n\n\nb\n* c")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "</itemizedlist>", "b\n", 
                             "<itemizedlist>", "* c\n", 
                             "</itemizedlist>"])
    def test_1211(self):
        b = md2dbk.blocks("* a\n* x\n\n")
        self.assertEqual(b, ["<itemizedlist>", "* a\n* x\n", 
                             "</itemizedlist>"])
    def test_1212(self):
        b = md2dbk.blocks("* a\n* x\n\nb")
        self.assertEqual(b, ["<itemizedlist>", "* a\n* x\n", 
                             "</itemizedlist>", "b\n"])
    def test_1213(self):
        b = md2dbk.blocks("* a\n* x\n\nb\n* c")
        self.assertEqual(b, ["<itemizedlist>", "* a\n* x\n",
                             "</itemizedlist>", "b\n",
                             "<itemizedlist>", "* c\n",
                             "</itemizedlist>"])
    def test_1221(self):
        b = md2dbk.blocks("* a\n** x\n\n")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "</itemizedlist>", 
                             "</itemizedlist>"])
    def test_1222(self):
        b = md2dbk.blocks("* a\n** x\n\nb")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "</itemizedlist>", 
                             "</itemizedlist>", "b\n"])
    def test_1223(self):
        b = md2dbk.blocks("* a\n** x\n\nb\n* c")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "</itemizedlist>", 
                             "</itemizedlist>", "b\n",
                             "<itemizedlist>", "* c\n", 
                             "</itemizedlist>"])
    def test_1224(self):
        b = md2dbk.blocks("* a\n** x\n*** y\nb\n* c")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "<itemizedlist>", "*** y\n",
                             "</itemizedlist>", 
                             "</itemizedlist>", 
                             "</itemizedlist>", "b\n",
                             "<itemizedlist>", "* c\n", 
                             "</itemizedlist>"])
    def test_1225(self):
        b = md2dbk.blocks("* a\n** x\n** y\nb\n* c")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n** y\n", 
                             "</itemizedlist>", 
                             "</itemizedlist>", "b\n",
                             "<itemizedlist>", "* c\n", 
                             "</itemizedlist>"])
    def test_1226(self):
        b = md2dbk.blocks("* a\n** x\n* y\n\nb")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "</itemizedlist>", "* y\n", 
                             "</itemizedlist>", "b\n"])
    def test_1227(self):
        b = md2dbk.blocks("* a\n** x\n* y\n* z\n\nb")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "</itemizedlist>", "* y\n* z\n", 
                             "</itemizedlist>", "b\n"])
    def test_1228(self):
        b = md2dbk.blocks("* a\n** x\n* y\n** z\n\nb")
        self.assertEqual(b, ["<itemizedlist>", "* a\n", 
                             "<itemizedlist>", "** x\n", 
                             "</itemizedlist>", "* y\n", 
                             "<itemizedlist>", "** z\n", 
                             "</itemizedlist>", 
                             "</itemizedlist>", "b\n"])

if __name__ == "__main__":
    # main()
  import optparse
  _o = optparse.OptionParser("%prog [options] test_xxx")
  _o.add_option("--xmlresults", metavar="FILE", default=None,
    help="capture results as a junit xml file [%default]")
  _o.add_option("-v", "--verbose", action="count", default=0,
    help="increase logging output [%default]")
  opt, args = _o.parse_args()
  logging.basicConfig(level = logging.WARNING - 10 * opt.verbose)
  #
  if not args: args += [ "test_" ]
  suite = TestSuite()
  for arg in args:
    for classname in sorted(list(globals())):
      if not classname.endswith("Tests"):
        continue
      testclass = globals()[classname]
      for method in sorted(dir(testclass)):
        if "*" not in arg: arg += "*"
        if arg.startswith("_"): arg = arg[1:]
        if matches(method, arg):
          suite.addTest(testclass(method))
  xmlresults = opt.xmlresults
  if xmlresults:
    try: import xmlrunner
    except: xmlresults=None
  if xmlresults:
    if os.path.exists(opt.xmlresults):
      os.remove(opt.xmlresults)
    logg.info("xml results into %s", opt.xmlresults)
    Runner = xmlrunner.XMLTestRunner
    result = Runner(output=opt.xmlresults).run(suite)
  else:
    Runner = TextTestRunner
    result = Runner(verbosity=opt.verbose).run(suite)
  if not result.wasSuccessful():
    sys.exit(1)