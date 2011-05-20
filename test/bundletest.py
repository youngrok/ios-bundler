import os
import shutil
from iosbundler import bundler
import unittest

class BundlerTest(unittest.TestCase):
    def setUp(self):
        self.workdir = os.path.dirname(__file__) + '/..'
        shutil.rmtree(os.path.join(self.workdir, 'build'))
        os.makedirs(self.workdir + '/build')
        shutil.copytree(self.workdir + '/SampleApp', self.workdir + '/build/SampleApp')
        shutil.copytree(self.workdir + '/SampleFramework', self.workdir + '/build/SampleFramework')
        
    def test_get_project(self):
        bundler.set_workdir(self.workdir + '/build')
        project = bundler.get_project('SampleApp')
        self.assertEquals('SampleApp', project.uniqueid().split(':')[-1])
        
    def test_install_local(self):
        bundler.set_workdir(self.workdir + '/build')
        print bundler.get_project('SampleApp').dependencies()
        bundler.add_dependency('SampleApp', 'SampleFramework')
        print bundler.get_project('SampleApp').dependencies()
#        bundler.install_local(workdir + 'build/SampleApp', workdir + '/build/SampleFramework')
    
#bundle install SampleFramework

#build SampleApp
#confirm build
