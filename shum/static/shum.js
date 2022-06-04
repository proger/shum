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

    let index = 0;

    // each word is a checkbox

    function tokenId(loc, kind) {
        return `_${loc.toString().padStart(3, "0")}-${kind}`;
    }
    function insertion(loc) {
        return `<label class="btn btn-insertion" data-word="<unk>">
            <input type="checkbox" autocomplete="off" name="${tokenId(loc, "I")}" value="<unk>">·
        </label>`;
    }
    let buttons = `<div id="tokens" class="btn-group" data-toggle="buttons">`;
    for (const word of transcript.split(" ")) {
        const escaped = word.replace(/</g,'&lt;').replace(/>/g,'&gt;');
        buttons += `
        ${insertion(index*2)}
        <label class="btn btn-correct active">
            <input type="checkbox" autocomplete="off" checked name="${tokenId(index*2+1, "S")}" value="${word}">${escaped}</input>
        </label>
        `;
        index += 1;
    }
    buttons += `${insertion(index*2)}</div>`;
    document.getElementById('hypothesis').innerHTML = buttons;

    document.forms.shum.utt_id.value = utt_id;
    document.forms.shum.hypothesis.value = transcript;
})

$(document.body).on('vulyk.save', (e, callback) => {
    const value = Object.fromEntries((new FormData(document.forms.shum)).entries());
    console.log(value);
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

