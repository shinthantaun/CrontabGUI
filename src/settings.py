"""Constants to control GUI features such as font and color

imgpath : 
Image folder path which contains button images and logo

app     : 
Font and GUI window size

canvas  : 
Background color of the canvas. Canvas is where buttons and labels are rendered

scrollbar : 
Scrollbar background color

cronJob : 
Font and background color of Cronjob label

saveButton : 
Font and background color of saveButton
"""
# Put your image file path here
imgpath = "/home/burneds/crontabGUI/img/"

app = {
    "font" : ('Bold', 11),
    "windowSize": "800x560"
}

canvas = {
    "background": "#393E46",
}

scrollbar = {
    "troughcolor": "#393E46"
}

cronJob = {
    "fontcolor" : "#F2E7D5",
    "background" : "#393E46"
}

saveButton = {
    "fontcolor" : "#F7F7F7",
    "background" : "#6D9886"
}
