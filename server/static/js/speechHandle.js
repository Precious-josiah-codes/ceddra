const grammar = '#JSGF V1.0; grammar colors; public <color> = ceddra | cedra;'
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList

var recognition = new SpeechRecognition()
var speechRecognitionList = new SpeechGrammarList()


speechRecognitionList.addFromString(grammar, 1)
recognition.grammars = speechRecognitionList
recognition.continuous = false
recognition.lang = 'en-US'
recognition.interimResults = false
recognition.maxAlternatives = 1

let diagnostic = document.querySelector('.output')
let bg = document.querySelector('html')



let speech_back = null

document.querySelector('#command').addEventListener('click', function() {
    recognition.start()
    console.log('Ready to recieve your command')
    if(speech_back !== null && speech_back !== 'Sorry i did not get that'){
        setTimeout(function () {
        console.log('Am here now')
        let synth = window.speechSynthesis
        let utterThis = new SpeechSynthesisUtterance(speech_back)
        utterThis.rate = 0.7
        utterThis.pitch = 0
        synth.speak(utterThis)
        console.log('she is speaking')
    }, 10000);
    } else {
        setTimeout(function(){
            let synth = window.speechSynthesis
            let utterThis = new SpeechSynthesisUtterance(speech_back)
            utterThis.rate = 0.7
            utterThis.pitch = 0
            synth.speak(utterThis)
        }, 4000)
    }

})




const reply = (reply_back) => {
    if (reply_back.toLowerCase().includes('play me') && reply_back.length > 7) {
        textIndex = reply_back.indexOf('play me')
        console.log('play me')
        new_text = reply_back.slice(8)
        let song_name = {Message : new_text}
        speech_back = 'playing ' + new_text
        send_request(song_name)
        console.log('playing ' + new_text)
    } else if (reply_back.toLowerCase().includes('play') && reply_back.length > 4){
        textIndex = reply_back.indexOf('play')
        new_text = reply_back.slice(5)
        song_title = new_text
        speech_back = 'playing ' + new_text
        let song_name = {Message : new_text}
        send_request(song_name)
        console.log('playing ' + new_text)
    }else {
        speech_back = 'Sorry i did not get that'
        console.log('Didnt find anything')
    }

}


const send_request = (userInput) => {
    // Async fetch
    fetch('/get_song', {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(userInput),
        cache: 'no-cache',
        headers: new Headers({
            'content-type': 'application/json'
        })
    })
    .then(function(response) {
        if (response.status !== 200) {
            console.log('Response status')
        }

        response.json().then(function(data) {
            console.log(data)
        })
    })


    
}

recognition.onresult = function(event) {
    var last = event.results.length - 1
    var speech = event.results[last][0].transcript
    
    diagnostic.textContent = 'Speech: ' + speech


    // calling the reply function
    reply(speech)
    
}


