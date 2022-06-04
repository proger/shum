var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    plugins: [
    ]
});

$("#play").on('click', e => {
    wavesurfer.playPause();
});

$(document.body).on('vulyk.next', (e, data) => {
    console.log({e, data});
    const {utt_id, transcript, wav, phones, phone_durations} = data.result.task.data;

    wavesurfer.load(wav.replace(/^\./, ''));
    document.getElementById('text').innerText = transcript;
    document.forms.shum.utt_id.value = utt_id;
    document.forms.shum.transcript.value = transcript;
})

$(document.body).on('vulyk.save', (e, callback) => {
    const value = Object.fromEntries((new FormData(document.forms.shum)).entries())
    callback(value);
});

$(document.body).on('vulyk.skip', (e, callback) => {
    callback();
});

$(document.body).on('vulyk.task_error', (e, data) => {
    $.magnificPopup.open({
        items: {
            src: '<div class="zoom-anim-dialog small-dialog">' +
            '<div class="dialog-content">Завдання закінчились! 🎉</div>' +
            '</div>',
            type: 'inline'
        }
    })
});

