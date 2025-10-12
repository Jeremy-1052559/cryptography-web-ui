const ENCRYPTBUTTON = document.getElementById('encrypt-button'),
      DECRYPTBUTTON = document.getElementById('decrypt-button'),
      ENCRYPTBOX = document.getElementById('encrypt-box'),
      DECRYPTBOX = document.getElementById('decrypt-box');

ENCRYPTBUTTON.addEventListener('click', () => {
    post({'text': ENCRYPTBOX.value},
         '/encrypt',
         (json) => { DECRYPTBOX.value = json['encrypted']; },
         (error) => { console.log(error); }
    );
});

DECRYPTBUTTON.addEventListener('click', () => {
    post({'text': DECRYPTBOX.value},
         '/decrypt',
         (json) => { ENCRYPTBOX.value = json['decrypted']; },
         (error) => { console.log(error); }
    );
});

function post(data, endpoint, onload, onerror)
{
    var xhr = new XMLHttpRequest();
    xhr.open('POST', endpoint);
    xhr.onloadend = () => {
        if (xhr.readyState == xhr.DONE)
        {
            if (xhr.status == 200)
            {
                var json = JSON.parse(xhr.responseText);
                onload(json);
                return;
            }
            onerror(xhr.responseText);
        }
    };
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(data));
}