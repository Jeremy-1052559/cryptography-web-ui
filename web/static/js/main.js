const ENCRYPTBUTTON = document.getElementById('encrypt-button'),
      DECRYPTBUTTON = document.getElementById('decrypt-button'),
      ENCRYPTBOX = document.getElementById('encrypt-box'),
      DECRYPTBOX = document.getElementById('decrypt-box'),
      ENCRYPTCOPYBUTTON = document.getElementById('clipboard-button-encrypt'),
      DECRYPTCOPYBUTTON = document.getElementById('clipboard-button-decrypt');

ENCRYPTBUTTON.addEventListener('click', () => {
    post({'text': ENCRYPTBOX.value},
         '/encrypt',
         (json) => { DECRYPTBOX.value = json['encrypted']; DECRYPTCOPYBUTTON.classList.toggle('d-none'); },
         (error) => { console.log(error); }
    );
});

DECRYPTBUTTON.addEventListener('click', () => {
    post({'text': DECRYPTBOX.value},
         '/decrypt',
         (json) => { ENCRYPTBOX.value = json['decrypted']; ENCRYPTCOPYBUTTON.classList.toggle('d-none'); },
         (error) => { console.log(error); }
    );
});

ENCRYPTCOPYBUTTON.addEventListener('click', () => { navigator.clipboard.writeText(ENCRYPTBOX.value); });
DECRYPTCOPYBUTTON.addEventListener('click', () => { navigator.clipboard.writeText(DECRYPTBOX.value); });

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