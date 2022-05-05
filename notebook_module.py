# Databricks notebook source
# This file is an example of a job that needs to be executed on commit
import sys
# Include dependencies from this or other repo that is synced in Databricks repos
sys.path.append("/Workspace/Repos/brandon@databricks.com/repotests")
# Load the autoreload extension in notebooks where you want the dependencies to automatically be updated 
%load_ext autoreload
%autoreload 
# Run a dependency that you are continuously updating
from module import myfunc
myfunc()
