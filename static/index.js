// const socket = new WebSocket('ws://localhost:8080');
// import io from 'socket.io-client/dist/socket.io';
const socket = io.connect('ws://127.0.0.1:5000/');
var stream_url = "youtube.com";

// Connection opened
// socket.addEventListener('open', function (event) {
//     socket.send('Hello Server!');
// });

// // Listen for messages
// socket.addEventListener('message', function (event) {
//     var b = document.querySelector("iframe");
//     b.setAttribute("src", event.data);
// });

socket.on('change', function(event){
    var b = document.querySelector("iframe");
    b.setAttribute("src", event.link);
    console.log(event.link)
    console.log(event)
});