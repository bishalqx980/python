import os

music_list = os.listdir("song")

printout = ""
for music in music_list:
    music_name = music[0:-4]
    music_location = f"./song/{music}"

    printout += (
        f"<button class=\"music-btn\" onclick='loadmusic(\"{music_name}\", \"{music_location}\")'>{music_name}</button><br>\n"
    )

html_content = (
    "<!DOCTYPE html>\n"
    "<html lang=\"en\">\n"
    "<head>\n"
    "<meta charset=\"UTF-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    "<title>Music Station</title>\n"
    "<link rel=\"stylesheet\" href=\"style.css\">\n"
    "<script src=\"script.js\"></script>\n"
    "</head>\n"
    "<body style=\"background-image: url(bgimg.jpeg);\" onload=\"preload()\">\n"
    "<h1 style=\"text-align: center;\"><u>Music Station</u></h1>\n"
    "<div class=\"top-div\" id=\"top-div\">\n"
    "<div class=\"player-div\">\n"
    "<h3>Now playing: <span id=\"music-player-name\">none</span></h3>\n"
    "<audio id=\"music-player\" src controls autoplay loop></audio>\n"
    "<div class=\"player-div-info\">\n"
    f"<h2>Music loaded: {len(music_list)}</h2>\n"
    "<p><b>Autoplay:</b> <button onclick=\"autoplay('yes')\">ON</button> <button onclick=\"autoplay('no')\">OFF</button></p>\n"
    "<p><b>Repeat:</b> <button onclick=\"repeat('yes')\">ON</button> <button onclick=\"repeat('no')\">OFF</button></p>\n"
    "<p><b>Keep history:</b> <button onclick=\"history('yes')\">Yes</button> <button onclick=\"history('no')\">No</button></p>\n"
    "<p><b>Background image:</b> <button onclick=\"bgimage('yes')\">Keep</button> <button onclick=\"bgimage('no')\">Remove</button></p>\n"
    "<button onclick=\"log('log cleared!', 'yes')\">Clear log</button>\n"
    "</div>\n"
    "</div>\n"
    "<div class=\"list-div\">\n"
    f"{printout}" 
    "</div>\n"
    "</div>\n"
    "<textarea id=\"log\" readonly placeholder=\"log\"></textarea>\n"
    "</body>\n"
    "</html>\n"
)

with open("index.html", "w", encoding="UTF-8") as f:
    f.write(html_content)

print(".................................. DONE ................................")