
const game = new PingPongGame();


function setup(){
    let canvas = createCanvas(600, 400);
    canvas.id("game")
    canvas.parent("app");

    let roomCode = localStorage.getItem("roomCode");

    player1 = new Player(player1Id, "1");
    player2 = new Player(player2Id, "2");
    game.players.push(player1);
    game.players.push(player2);
    
}

function draw(){
    background(0);
    game.renderPlayers();

}