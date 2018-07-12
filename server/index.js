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
  cronTime: '00 54 16 * * 1-5',
  onTick: function() {
    /*
     * Runs every weekday (Monday through Friday)
     * at 13:00:00 PM. It does not run on Saturday
     * or Sunday.
     */
   var doWithPython = require('./doWithPython');; 
  },
  start: false
});
job.start();
console.log('job status', job.running); 