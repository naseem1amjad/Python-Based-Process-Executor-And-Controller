#Script created by Naseem Amjad (urdujini@gmail.com)
#it is run when flask run is called on command line
#Permissive license granted with conditions only requiring preservation of copyright and license notices.

from flask import Flask

import os,signal,sys
import time
 

app = Flask(__name__)

base_url=''
file2run='test_run.py'
hasParameter=False
file2runParemeter='test'

if os.environ.get('FLASK_ENV')=="development":
    print("Entering in TEST mode")
    hasParameter=True


version='2021-09-30'

myhtml='<HTML><!-- base_url="'+base_url+'" version='+version+' -->'
myhtml=myhtml+'<title>Python based Controller - by Naseem Amjad</title>'
myhtml=myhtml+'<h1>Process/Script ('+file2run+') Controller</h1>'
myhtml=myhtml+'<a href="'+base_url+'/check">Check Process</a><BR><BR>'
myhtml=myhtml+'<a href="'+base_url+'/start">Start Process</a><BR><BR>'
myhtml=myhtml+'<a href="'+base_url+'/stop">Stop Process</a><BR><BR>'

@app.route('/')
def hello():       
    return myhtml
    
@app.route('/stop')
def stop_process():
    kill_target(file2run)
    return myhtml+'<h3>Process '+file2run+' stopped </h3><BR>'
 
@app.route('/start') 
def start_process():
    if (is_running(file2run)):
        return myhtml+'<h3>'+file2run+' is already running</h3><BR>'
    else:
        if hasParameter:
            os.system('python3 ./'+file2run+' '+file2runParemeter+' &')
            return myhtml+'<h3>Process "'+file2run+' '+file2runParemeter+'" started </h3><BR>'
        else:
            os.system('python3 ./'+file2run+' &')
            return myhtml+'<h3>Process '+file2run+' started </h3><BR>'
    

@app.route('/check')
def check_process():
    if (is_running(file2run)):
        return myhtml+'<h3>Process '+file2run+' found running</h3><BR>'
    else:
        return myhtml+'<h3>Process '+file2run+' NOT running</h3><BR>'
    
def is_running(target):
    cmd_run="ps aux | grep {}".format(target)
    out=os.popen(cmd_run).read()
    for line in out.splitlines():
        if './'+target in line:
            return 1
    return 0
    
@app.route('/about')
def get_now_time():
    # Get current local time
    now_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return myhtml+'<hr><h2>Script developed by Naseem Amjad (naseem@technologist.com)<h2><hr><h4>Time: '+now_time+'</h4><h5>Version: '+version+'</h5>'
 
def kill(pid):
    a = os.kill(pid,signal.SIGKILL)
    myreturn='The process that killed pid to '+str(pid)+', the return value is: '+str(a)
    return myreturn;
 
def kill_target(target):
    cmd_run="ps aux | grep {}".format(target)
    out=os.popen(cmd_run).read()
    for line in out.splitlines():
        if './'+target in line:
            pid = int(line.split()[1])
            kill(pid)
 # It is recommended to add the & symbol after the run command, it seems to be running in another thread
