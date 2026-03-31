const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const { spawn } = require("child_process");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: { origin: "*" }
});

app.use(express.static("public"));

let users = [];

// ======================= IMPORTANT FOR RAILWAY =======================
const PORT = process.env.PORT || 3000;

server.listen(PORT, "0.0.0.0", () => {
  console.log(`✅ Server running on port ${PORT}`);
});

// ======================= SOCKET.IO LOGIC =======================
io.on("connection", (socket) => {

  /* ---------------- USER JOIN ---------------- */
  socket.on("join", (name) => {
    socket.username = name;
    users.push(name);
    socket.slot = users.length - 1;

    socket.emit("my-slot", socket.slot);
    io.emit("users", users);
  });

  /* ---------------- CHAT ---------------- */
  socket.on("msg", (text) => {
    io.emit("msg", {
      name: socket.username,
      text: text,
      slot: socket.slot
    });
  });

  /* ---------------- PLAY GAME ---------------- */
  socket.on("play-game", (game) => {
    let file = "";

    if (game === "tictactoe") file = "games/tic_tac_toe.py";
    if (game === "dice") file = "games/dice_race.py";
    if (game === "word") file = "games/guess_the_word.py";
    if (game === "number") file = "games/guess_the_number.py";

    if (file === "") return;

    // Kill old game if running
    if (socket.gameProcess) {
      socket.gameProcess.kill();
      socket.gameProcess = null;
    }

    console.log(`Starting game: ${game} → ${file}`);

    socket.emit("game-output", `Starting ${game}...\n`);

    // Use python3 and unbuffered output (-u)
    const py = spawn("python3", ["-u", file], {
      stdio: ['pipe', 'pipe', 'pipe']
    });

    socket.gameProcess = py;

    // Output from Python
    py.stdout.on("data", (data) => {
      socket.emit("game-output", data.toString());
    });

    // Error from Python
    py.stderr.on("data", (err) => {
      socket.emit("game-output", `<span style="color:red">Error: ${err.toString()}</span>`);
    });

    // Game ended
    py.on("close", (code) => {
      socket.emit("game-output", `\nGame ended with code ${code}.\n`);
      socket.gameProcess = null;
    });
  });

  /* ---------------- GAME INPUT ---------------- */
  socket.on("game-input", (text) => {
    if (socket.gameProcess && socket.gameProcess.stdin) {
      try {
        socket.gameProcess.stdin.write(text + "\n");
      } catch (err) {
        socket.emit("game-output", "Input error.\n");
      }
    }
  });

  /* ---------------- DISCONNECT ---------------- */
  socket.on("disconnect", () => {
    if (socket.slot !== undefined) {
      users.splice(socket.slot, 1);
      io.emit("users", users);
    }

    if (socket.gameProcess) {
      socket.gameProcess.kill();
      socket.gameProcess = null;
    }
  });
});
