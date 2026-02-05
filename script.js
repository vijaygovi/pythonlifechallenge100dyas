// --- Login ---
function login() {
    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    if (u && p) {
        document.getElementById('loginPage').style.display = 'none';
        document.getElementById('dashboard').style.display = 'flex';
        initCharts(); startCamera();
    } else alert("Enter valid credentials!");
}
function logout() { location.reload(); }

// --- Graph ---
function initCharts() {
    const ctx = document.getElementById('weatherCropChart');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [
                {
                    label: 'Temperature (°C)', data: [30, 32, 31, 29, 28, 27, 29],
                    borderColor: '#ef4444', backgroundColor: 'rgba(239,68,68,0.2)', yAxisID: 'y1', tension: 0.3
                },
                {
                    label: 'Rainfall (mm)', data: [5, 12, 8, 2, 0, 15, 10],
                    borderColor: '#3b82f6', backgroundColor: 'rgba(59,130,246,0.2)', yAxisID: 'y1', tension: 0.3
                },
                {
                    label: 'Crop Yield Index', data: [70, 85, 78, 65, 60, 90, 80],
                    borderColor: '#16a34a', backgroundColor: 'rgba(22,163,74,0.2)', yAxisID: 'y2', tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            interaction: { mode: 'index' },
            scales: {
                y1: { type: 'linear', position: 'left' },
                y2: { type: 'linear', position: 'right' }
            }
        }
    });
    document.getElementById("aiStatus").innerText = "Rain boosted yield midweek 🌧🌱";
}

// --- AI Assistant ---
function mockAIResponse(msg) {
    if (msg.toLowerCase().includes("rain")) return "🌧 Rain will boost soil moisture, expect better growth.";
    if (msg.toLowerCase().includes("heat")) return "🔥 Heat stress detected, irrigate more often.";
    return "✅ Crops look stable for now.";
}
function sendAIMessage() {
    const input = document.getElementById('aiInput');
    const msg = input.value.trim(); if (!msg) return;
    addChat("👨‍🌾 You: " + msg);
    const reply = mockAIResponse(msg);
    setTimeout(() => { addChat("🤖 AI: " + reply); addActivity(reply); }, 600);
    input.value = "";
}
function addChat(text) {
    const box = document.getElementById('chatBox');
    const div = document.createElement('div'); div.textContent = text; box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

// --- Activities ---
function addActivity(activity) {
    const list = document.getElementById('activities');
    const li = document.createElement('li');
    li.innerHTML = activity + " <button onclick='markDone(this)'>✔</button>";
    list.prepend(li);
}
function markDone(btn) {
    const li = btn.parentElement;
    li.style.textDecoration = "line-through"; li.style.color = "#9ca3af"; btn.remove();
}

// --- Camera ---
function startCamera() {
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => { video.srcObject = stream; })
        .catch(err => console.error("Camera error:", err));
}
function capturePhoto() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    canvas.style.display = "block";
    canvas.width = video.videoWidth; canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    const analysis = "📷 AI analyzed photo: Crops healthy with slight heat stress.";
    addChat("🤖 AI: " + analysis);
    addActivity(analysis);
}
// --- Sidebar ---

    function toggleMenu(id) {
        let menu = document.getElementById(id);
    menu.style.display = menu.style.display === "block" ? "none" : "block";
            }
function addNewCrop() {
    alert("Add New Crop button clicked!");
}

