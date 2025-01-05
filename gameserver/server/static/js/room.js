
async function handleRoomCreation() {

    let player1 = document.getElementById("player1").value;
    let player2 = document.getElementById("player2").value;

    if (player1 == player2) {
        alert("Player1 and Player2 name should be unique and different");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/create-room", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ player1, player2 }),
        });
        
        if (!response.ok) {
            server_response = await response.json();
            for(let i=0;i<server_response["errors"].length;i++){
                alert(server_response["errors"][i]["message"]);
            }
            return;
        }

        const data = await response.json();
        console.log(data)

        if (data["status_code"] == 200) {
            localStorage.setItem("isRoomCreator", true);
            alert(data["message"]);
            alert(data["room_code"]);

        } else {
            alert(data["detail"]);
        }

    } catch (err) {
        console.error("Error in fetch:", err);
    }
}


async function JoinRoomHandler() {
    roomCode = document.getElementById("code").value;
    isRoomCreator = localStorage.getItem("isRoomCreator");
    if(isRoomCreator == null){
        isRoomCreator = false;
    }

    localStorage.setItem("roomCode", roomCode);

    try {
        const response = await fetch("http://127.0.0.1:8000/join-room", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ "room_code": roomCode, "is_room_creator": isRoomCreator }),
        });
        
        if (!response.ok) {
            server_response = await response.json();
            for(let i=0;i<server_response["errors"].length;i++){
                alert(server_response["errors"][i]["message"]);
            }
            return;
        }

        const data = await response.json();
        console.log(data)

        if (data["status_code"] == 200) {
            alert(data["message"]);
            window.location.href = "/game";
        } else {
            alert(data["detail"]);
        }

    } catch (err) {
        console.error("Error in fetch:", err);
    }
}

document.getElementById("create-room-form").addEventListener('submit', async (e) => {
    e.preventDefault();
    await handleRoomCreation();
});

document.getElementById("join-form").addEventListener('submit', async (e) => {
    e.preventDefault();
    await JoinRoomHandler();
});