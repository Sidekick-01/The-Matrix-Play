const socket = io()

const uscreen = document.getElementById("uscreen")
const uname = document.getElementById("uname")
const joinbtn = document.getElementById("joinbtn")
const msginput = document.getElementById("msginput")

/* GAME TERMINAL ELEMENTS */
const gameScreen = document.getElementById("gameScreen")
const terminal = document.getElementById("gameTerminal")
const gameInput = document.getElementById("gameInput")
const gameTitle = document.getElementById("gameTitle")
const backBtn = document.getElementById("backBtn")

let myslot = -1
let myname = ""
let users = []


/* ---------------- JOIN ---------------- */

joinbtn.onclick = () => {

  const name = uname.value.trim()

  if(!name){
    alert("enter name")
    return
  }

  myname = name
  uscreen.style.display = "none"

  socket.emit("join", name)

}

uname.addEventListener("keypress", e=>{
  if(e.key === "Enter") joinbtn.click()
})


/* ---------------- SERVER SLOT ---------------- */

socket.on("my-slot", slot => {

  myslot = slot

  const center = document.querySelector("#slot2 .status")
  if(center){
    center.textContent = "YOU – " + myname
  }

})


/* ---------------- USERS UPDATE ---------------- */

socket.on("users", list => {

  users = list

  const display = [null,null,null,null,null]

  display[2] = users[myslot]

  if(myslot-1 >= 0) display[1] = users[myslot-1]
  if(myslot-2 >= 0) display[0] = users[myslot-2]

  if(myslot+1 < users.length) display[3] = users[myslot+1]
  if(myslot+2 < users.length) display[4] = users[myslot+2]

  for(let i=0;i<5;i++){

    const mon = document.getElementById("slot"+i)
    if(!mon) continue

    const status = mon.querySelector(".status")
    const profile = mon.querySelector(".profile")
    const chat = document.getElementById("chat"+i)

    if(display[i]){

      mon.classList.remove("dim")
      if(chat) chat.classList.remove("dim")

      if(i !== 2 && status){
        status.textContent = display[i]
      }

      if(profile){
        profile.textContent = display[i][0].toUpperCase()
      }

    } 
    else {

      mon.classList.add("dim")
      if(chat) chat.classList.add("dim")

      if(i !== 2 && status){
        status.textContent = "Commander – OFFLINE"
      }

      if(profile){
        profile.textContent = "?"
      }

    }

  }

})


/* ---------------- CHAT SEND ---------------- */

msginput.addEventListener("keypress", e => {

  if(e.key !== "Enter") return

  const text = msginput.value.trim()

  if(!text) return
  if(myslot === -1) return

  socket.emit("msg", text)

  msginput.value = ""

})


/* ---------------- CHAT RECEIVE ---------------- */

socket.on("msg", data => {

  if(myslot === -1) return

  let displaySlot = null

  if(data.slot === myslot) displaySlot = 2
  else if(data.slot === myslot-1) displaySlot = 1
  else if(data.slot === myslot-2) displaySlot = 0
  else if(data.slot === myslot+1) displaySlot = 3
  else if(data.slot === myslot+2) displaySlot = 4

  if(displaySlot === null) return

  const chat = document.getElementById("chat"+displaySlot)
  if(!chat) return

  const line = document.createElement("div")
  line.textContent = data.name + ": " + data.text

  chat.appendChild(line)

  chat.scrollTop = chat.scrollHeight

})


/* ---------------- GAME UI ---------------- */

function openGameUI(name){

  document.querySelector(".scene").style.display="none"
  document.querySelector(".game-area").style.display="none"

  gameScreen.style.display="block"

  gameTitle.innerText = name
  terminal.innerHTML = ""

  gameInput.focus()

}

backBtn.onclick = ()=>{

  gameScreen.style.display="none"

  document.querySelector(".scene").style.display="block"
  document.querySelector(".game-area").style.display="block"

}


/* ---------------- GAME BUTTONS ---------------- */

document.getElementById("3tbtn").onclick = ()=>{
  openGameUI("Tic Tac Toe")
  socket.emit("play-game","tictactoe")
}

document.getElementById("dracebtn").onclick = ()=>{
  openGameUI("Dice Race")
  socket.emit("play-game","dice")
}

document.getElementById("wordbtn").onclick = ()=>{
  openGameUI("Guess The Word")
  socket.emit("play-game","word")
}

document.getElementById("numbtn").onclick = ()=>{
  openGameUI("Guess The Number")
  socket.emit("play-game","number")
}


/* ---------------- GAME OUTPUT ---------------- */

socket.on("game-output", output => {

  if(!terminal) return

  terminal.innerHTML += output + "<br>"

  terminal.scrollTop = terminal.scrollHeight

})


/* ---------------- GAME INPUT ---------------- */

if(gameInput){

  gameInput.addEventListener("keypress", e => {

    if(e.key !== "Enter") return

    const text = gameInput.value.trim()

    if(!text) return

    terminal.innerHTML += "<span style='color:#0ff'> > " + text + "</span><br>"

    socket.emit("game-input", text)

    gameInput.value = ""

  })

}