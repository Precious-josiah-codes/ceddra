from music_module.music import Music

def call_music(option):
    if option.find('sad+song') > -1 or option.find('sad+music') > -1:
        Music().playMood('sad')
    elif option.find('happy+song') > -1 or option.find('happy+music') > -1:
        Music().playMood('happy')
    elif option.find('romantic+song') > -1 or option.find('romantic+music') > -1:
        Music().playMood('romantic')
    elif option.find('gospel+song') > -1 or option.find('gospel+music') > -1:
        Music().playMood('gospel')
    else:
        Music().playMusic(option)




   

