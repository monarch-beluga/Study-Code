import {ref} from "vue";

const currentSpeech = ref('');
const speechSynthesis = window.speechSynthesis

const speakMessage = (text) => {
    return new Promise((resolve) => {
        if (!window.speechSynthesis) {
            resolve(false);
            return;
        }

        const utterance = new SpeechSynthesisUtterance(text);
        currentSpeech.value = text;

        utterance.onend = () => {
            resolve(true);
        };

        utterance.onerror = () => {
            resolve(false);
        };

        window.speechSynthesis.speak(utterance);
    });
};
const stopSpeak = () => {
    speechSynthesis.cancel();
}

export {speakMessage, stopSpeak}
