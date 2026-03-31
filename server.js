const express = require("express")
const http = require("http")
const { Server } = require("socket.io")
const { spawn } = require("child_process")

const app = express()
const server = http.createServer(app)
const io = new Server(server)

app.use(express.static("public"))

let users = []

io.on("connection", socket => {

  /* ---------------- USER JOIN ---------------- */

  socket.on("join", name => {

    socket.username = name
    users.push(name)

    socket.slot = users.length - 1

    socket.emit("my-slot", socket.slot)

    io.emit("users", users)

  })


  /* ---------------- CHAT MESSAGE ---------------- */

  socket.on("msg", text => {

    io.emit("msg", {
      name: socket.username,
      text: text,
      slot: socket.slot
    })

  })


  /* ---------------- PLAY PYTHON GAME ---------------- */

  socket.on("play-game", game => {

    let file = ""

    if(game === "tictactoe") file = "games/tic_tac_toe.py"
    if(game === "dice") file = "games/dice_race.py"
    if(game === "word") file = "games/guess_the_word.py"
    if(game === "number") file = "games/guess_the_number.py"

    if(file === "") return


    /* stop old game if running */

    if(socket.gameProcess){
      socket.gameProcess.kill()
      socket.gameProcess = null
    }


    /* RUN PYTHON WITH UNBUFFERED OUTPUT */

    const py = spawn("python", ["-u", file])

    socket.gameProcess = py


    /* PYTHON OUTPUT */

    py.stdout.on("data", data => {

      socket.emit("game-output", data.toString())

    })


    /* PYTHON ERROR */

    py.stderr.on("data", err => {

      socket.emit("game-output", "Error: " + err.toString())

    })


    /* GAME END */

    py.on("close", () => {

      socket.emit("game-output", "\nGame ended.")
      socket.gameProcess = null

    })

  })


  /* ---------------- GAME INPUT FROM BROWSER ---------------- */

  socket.on("game-input", text => {

    if(socket.gameProcess){

      try{
        socket.gameProcess.stdin.write(text + "\n")
      }
      catch(err){
        socket.emit("game-output","Input error.")
      }

    }

  })


  /* ---------------- USER DISCONNECT ---------------- */

  socket.on("disconnect", () => {

    if(socket.slot !== undefined){

      users.splice(socket.slot,1)
      io.emit("users", users)

    }

    if(socket.gameProcess){

      socket.gameProcess.kill()
      socket.gameProcess = null

    }

  })

})


server.listen(3000, () => {
  console.log("Server running on http://localhost:3000")
})