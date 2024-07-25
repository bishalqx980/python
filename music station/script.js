function preload(){
   if (window.screen.width < 800){
      document.getElementById("top-div").style.display = "contents"
      document.getElementById("log").style.width = "100%"
   }

   var vautoplay = localStorage.getItem("autoplay")
   var vrepeat = localStorage.getItem("repeat")
   var vhistory = localStorage.getItem("history")
   var vbgimage = localStorage.getItem("bgimage")

   if (vhistory == "yes"){
   var music_name = localStorage.getItem("music_name")
   var music_link = localStorage.getItem("music_link")

   loadmusic(music_name, music_link)
   }

   autoplay(vautoplay)
   repeat(vrepeat)
   history(vhistory)
   bgimage(vbgimage)
 }

 function log(message, clear=null){
   if (clear){
      document.getElementById("log").innerHTML = message
   }else{
      document.getElementById("log").innerHTML += "\n> " + message
   }
 }

 function loadmusic(name, music){
   document.getElementById("music-player-name").innerHTML = name
   document.getElementById("music-player").src = music
   log(name + " loaded!")

   localStorage.setItem("music_name", name)
   localStorage.setItem("music_link", music)
 }

 function autoplay(bool){
   if (bool == "yes"){
      document.getElementById("music-player").setAttribute("autoplay", "")
      log("Autoplay enabled!")
   }else{
      document.getElementById("music-player").removeAttribute("autoplay")
      log("Autoplay disabled!")
   }

   localStorage.setItem("autoplay", bool)
 }

 function repeat(bool){
   if (bool == "yes"){
      document.getElementById("music-player").setAttribute("loop", "")
      log("Repeat enabled!")
   }else{
      document.getElementById("music-player").removeAttribute("loop")
      log("Repeat disabled!")
   }

   localStorage.setItem("repeat", bool)
 }

 function history(bool){
   if (bool == "yes"){
      log("History enabled!")
   }else{
      log("History disabled!")
   }

   localStorage.setItem("history", bool)
 }

 function bgimage(bool){
   if (bool == "yes"){
      document.body.style.backgroundImage =  "url('bgimg.jpeg')"
      log("Background image enabled!")
   }else{
      document.body.style.backgroundImage =  ""
      log("Background image disabled!")
   }

   localStorage.setItem("bgimage", bool)
}