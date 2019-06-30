const zerorpc = require("zerorpc");
const ipcRenderer = require("electron").ipcRenderer;

var server = new zerorpc.Server({
  popUp: function(text, x, y) {
    ipcRenderer.send("popup", text, x, y);
  }
});

server.bind("tcp://0.0.0.0:1235");
