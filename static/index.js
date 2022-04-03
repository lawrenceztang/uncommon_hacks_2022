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

socket.on('change', function(data){
    // var b = document.querySelector("iframe");
    // b.setAttribute("src", event.data);
    console.log("1 minute passed")
});

// $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

// $(function(){
//     $('#vote').bind('click', function()

//         )

//     }
//     )