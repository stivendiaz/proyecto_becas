// importar 
var express = require('express');
var CronJob = require('cron').CronJob; 
// instanciar
var app = express();
var path = require('path');
// ruteo
app.get('/', function(req, res){
    res.sendFile(path.join(__dirname + '/../web/index.html'));
});
// Inicializar en puerto
app.listen(9000);
 
console.log("Servidor Express en modo %s", app.settings.env);

// Patron para garantizar que se corra el job en un horario especifico
var job = new CronJob({
  cronTime: '00 22 16 * * 1-5',
  onTick: function() {
    /*
     * Runs every weekday (Monday through Friday)
     * at 13:00:00 PM. It does not run on Saturday
     * or Sunday.
     */
   doWithPython(); 
  },
  start: false
});
job.start();
console.log('job status', job.running); 

function doWithPython() {
    var PythonShell = require('python-shell');
    var pyshell = new PythonShell('server/ejemplopatron.py');
    
    pyshell.on('message', function (message) {
      // Recibe el mensaje recibido desde el script de python
      console.log(message);
    });
    
    // Termina el proceso y manda un mensaje en caso de ser exitoso o arroja el error
    pyshell.end(function (err,code,signal) {
      if (err) throw err;
      
      console.log('The exit code was: ' + code);
      console.log('The exit signal was: ' + signal);
      console.log('finished');
      console.log('finished');
      
    });
  
  
  }
     