<!-- static/index.html -->
<!DOCTYPE html>
<html lang="bn">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>বিজ্ঞানীবন্ধু Chat & Myth Busting</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100">
    <div class="max-w-4xl mx-auto p-4 space-y-8">

        <!-- Gallery + Single Chat -->
        <div id="scientist-chat-module">
            <h2 class="text-2xl font-semibold mb-4">Roleplay as Scientist</h2>
            <div id="scientist-gallery" class="grid gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"></div>
        </div>

        <!-- Myth Evaluation -->
        <div id="myth-eval" class="space-y-4">
            <h2 class="text-2xl font-semibold">Evaluate Myth</h2>
            <textarea id="myth-input" rows="3" class="w-full border rounded p-2"
                placeholder="এখানে মিথ লিখুন..."></textarea>
            <button id="eval-btn" class="bg-indigo-500 text-white px-4 py-2 rounded hover:bg-indigo-600">Evaluate
                Myth</button>
            <pre id="eval-output" class="whitespace-pre-wrap bg-gray-50 p-4 rounded border text-gray-800"></pre>
        </div>

        <!-- Myth Busting Roundtable -->
        <div id="myth-bust" class="space-y-4">
            <h2 class="text-2xl font-semibold">Myth Busting Roundtable</h2>
            <textarea id="bust-input" rows="3" class="w-full border rounded p-2"
                placeholder="এখানে মিথ লিখুন..."></textarea>
            <button id="bust-btn" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Start
                Roundtable</button>
            <pre id="bust-output" class="whitespace-pre-wrap bg-gray-50 p-4 rounded border text-gray-800"></pre>
        </div>

    </div>

    <!-- Single Chat Modal -->
    <div id="chat-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 hidden">
        <div
            class="bg-white w-full max-w-md md:max-w-lg h-full md:h-3/4 rounded-lg shadow-lg flex flex-col overflow-hidden">
            <div class="flex items-center p-4 bg-blue-50 border-b">
                <img id="modal-avatar" class="w-12 h-12 rounded-full mr-3" />
                <h2 id="modal-name" class="text-xl font-semibold flex items-center"></h2>
                <button id="close-modal" class="ml-auto text-gray-500 hover:text-gray-800 text-2xl">×</button>
            </div>
            <div id="message-container" class="flex-1 p-4 overflow-y-auto space-y-3 bg-gray-50">
                <div id="empty-placeholder" class="text-center text-gray-400">কোনো বার্তা এখনও নেই।</div>
            </div>
            <div class="p-4 border-t flex">
                <input id="user-input" type="text" placeholder="আপনার বার্তা লিখুন..."
                    class="flex-1 border rounded-l px-3 py-2 focus:outline-none" />
                <button id="send-btn" disabled
                    class="bg-blue-400 text-white px-4 rounded-r hover:bg-blue-500 disabled:opacity-50">প্রেরণ
                    করুন</button>
            </div>
        </div>
    </div>

    <script>
        // Scientist data
        const scientists = [
            {
                'einstein': 'আলবার্ট আইনস্টাইন',
                'curie': 'মেরি কিউরি',
                'bose': 'সত্যেন্দ্রনাথ বোস',
                'hawking': 'স্টিফেন হকিং',
                'newton': 'আইজ্যাক নিউটন',
                'tesla': 'নিকোলা টেসলা',
                'darwin': 'চার্লস ডারউইন',
                'galileo': 'গ্যালিলিও গ্যালিলি',
                'maxwell': 'জেমস ক্লার্ক ম্যাক্সওয়েল',
                'faraday': 'মাইকেল ফারাডে',
                'feynman': 'রিচার্ড ফেইনম্যান',
                'bohr': 'নিলস বোর',
                'curie_s': 'পিয়েরে কিউরি',
                'lovelace': 'আদা লাভেলেস',
                'turing': 'অ্যালান টুরিং',
                'edison': 'থমাস এডিসন',
            }
        ];

        // DOM refs
        const G = id => document.getElementById(id),
            gallery = G('scientist-gallery'),
            modal = G('chat-modal'),
            msgC = G('message-container'),
            empty = G('empty-placeholder'),
            avatar = G('modal-avatar'),
            nameEl = G('modal-name'),
            userIn = G('user-input'),
            sendBtn = G('send-btn'),
            mythIn = G('myth-input'),
            evalBtn = G('eval-btn'),
            evalOut = G('eval-output'),
            bustIn = G('bust-input'),
            bustBtn = G('bust-btn'),
            bustOut = G('bust-output');
        let current = null;

        // Render gallery & modal logic
        function renderGallery() {
            scientists.forEach(sci => {
                let card = document.createElement('div');
                card.className = 'bg-white rounded-lg shadow p-4 text-center flex flex-col items-center';
                card.innerHTML = `
          <img src="${sci.avatar}" class="w-24 h-24 rounded-full mb-2"/>
          <h3 class="font-semibold mb-1">${sci.name}</h3>
          <p class="text-sm text-gray-600 mb-3">${sci.quote}</p>
          <button class="chat-btn bg-green-500 text-white px-3 py-1 rounded">আলোচনা করুন</button>`;
                card.querySelector('.chat-btn').onclick = () => openModal(sci);
                gallery.appendChild(card);
            });
        }

        function openModal(sci) {
            current = sci;
            avatar.src = sci.avatar;
            nameEl.textContent = `${sci.emoji} ${sci.name}`;
            msgC.innerHTML = '';
            empty.classList.remove('hidden');
            modal.classList.remove('hidden');
            sendBtn.disabled = true;
        }

        G('close-modal').onclick = () => modal.classList.add('hidden');

        function appendMsg(sender, text) {
            empty.classList.add('hidden');
            let d = document.createElement('div');
            d.className = sender === 'user' ? 'text-right' : 'text-left';
            d.innerHTML = `<span class="inline-block bg-gray-200 rounded px-3 py-1">${text}</span>`;
            msgC.appendChild(d);
            msgC.scrollTop = msgC.scrollHeight;
        }

        async function sendMsg() {
            let t = userIn.value.trim(); if (!t || !current) return;
            appendMsg('user', t);
            userIn.value = ''; sendBtn.disabled = true;
            appendMsg('bot', 'টাইপ করছেন...');
            let res = await fetch('/role_play_api/', {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: t, character_id: current.id })
            });
            msgC.lastChild.remove();
            let j = await res.json();
            appendMsg('bot', j.text || j.error);
        }

        userIn.oninput = () => sendBtn.disabled = !userIn.value.trim();
        sendBtn.onclick = sendMsg;
        userIn.onkeyup = e => e.key === 'Enter' && sendMsg();

        // Evaluate Myth
        evalBtn.onclick = async () => {
            let myth = mythIn.value.trim();
            if (!myth) return;
            evalOut.textContent = 'Evaluating...';
            let res = await fetch('/evaluate_api/', {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ myth })
            });
            let j = await res.json();
            evalOut.textContent = j.text || j.error;
        };

        // Myth Busting Roundtable
        bustBtn.onclick = async () => {
            let myth = bustIn.value.trim();
            if (!myth) return;
            bustOut.textContent = 'Starting roundtable...';
            let res = await fetch('/myth_bust_api/', {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ myth })
            });
            let j = await res.json();
            bustOut.textContent = j.text || j.error;
        };

        // init
        renderGallery();
    </script>
</body>

</html>