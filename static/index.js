// const socket = new WebSocket('ws://localhost:8080');
var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
stream_url = "youtube.com"

// Connection opened
// socket.addEventListener('open', function (event) {
//     socket.send('Hello Server!');
// });

// // Listen for messages
// socket.addEventListener('message', function (event) {
//     var b = document.querySelector("iframe");
//     b.setAttribute("src", event.data);
// });

socket.on('change link', function(event)){
    // var b = document.querySelector("iframe");
    // b.setAttribute("src", event.data);
    console.log("1 minute passed")
}
