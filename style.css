
/* ១. ការកំណត់គ្រឹះនៃអាណាចក្រ (Global Setup) */
:root {
    --hologram-cyan: #00ffff;
    --hologram-blue: #00a8ff;
    --neon-glow: 0 0 15px rgba(0, 255, 255, 0.5);
    --glass-bg: rgba(255, 255, 255, 0.05);
    --card-radius: 18px;
    --bank-gold: #ffce00;
}

body {
    background: #050510;
    color: white;
    font-family: 'Kantumruy', sans-serif;
    margin: 0;
    overflow-x: hidden;
    background-image: radial-gradient(circle at center, #0f172a 0%, #050510 100%);
}

/* ២. របារស្វែងរក និងប៊ូតុងសំឡេង */
.top-bar {
    display: flex;
    gap: 15px;
    padding: 20px;
    background: rgba(0, 255, 255, 0.03);
    border-bottom: 1px solid rgba(0, 255, 255, 0.1);
}

#search-input {
    width: 100%;
    padding: 12px 20px;
    border-radius: 12px;
    border: 1px solid var(--hologram-cyan);
    background: rgba(0, 255, 255, 0.05);
    color: white;
    outline: none;
    transition: 0.3s;
}

#search-input:focus {
    box-shadow: var(--neon-glow);
}

.btn-voice {
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid var(--hologram-cyan);
    color: var(--hologram-cyan);
    padding: 10px 20px;
    border-radius: 12px;
    cursor: pointer;
    font-weight: bold;
    white-space: nowrap;
}

/* ៣. របារប្រភេទម្ហូប */
#category-bar {
    padding: 15px 20px;
    display: flex;
    gap: 12px;
}

.btn-cat {
    padding: 10px 22px;
    border-radius: 30px;
    cursor: pointer;
    background: transparent;
    color: white;
    border: 1px solid rgba(0, 255, 255, 0.3);
    transition: 0.3s;
}

.btn-cat.active {
    background: var(--hologram-cyan);
    color: black;
    font-weight: bold;
    border-color: var(--hologram-cyan);
    box-shadow: var(--neon-glow);
}

/* ៤. តំបន់បញ្ជីមុខម្ហូប */
#main-content {
    display: flex;
    gap: 20px;
    padding: 0 20px 20px 20px;
}

#menu {
    flex: 3;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 20px;
}

.hologram-card {
    position: relative;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 255, 0.15);
    border-radius: var(--card-radius);
    padding: 15px;
    text-align: center;
    transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
    overflow: hidden;
}

.hologram-card:hover {
    transform: translateY(-8px);
    border-color: var(--hologram-cyan);
    box-shadow: var(--neon-glow);
    background: rgba(0, 255, 255, 0.08);
}

.scanline {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 2px;
    background: rgba(0, 255, 255, 0.2);
    animation: scan 4s linear infinite;
}

@keyframes scan { 0% { top: 0; } 100% { top: 100%; } }

.prod-img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 12px;
    margin-bottom: 12px;
}

.kh-name { font-weight: bold; font-size: 1em; margin-bottom: 5px; }
.prod-price { color: var(--hologram-cyan); font-weight: bold; font-size: 1.2em; }

/* ៥. ផ្ទាំងវិក្កយបត្រ (Invoice) */
#cart {
    flex: 1;
    min-width: 340px;
    background: #0a0a1a;
    border: 1px solid var(--hologram-cyan);
    border-radius: var(--card-radius);
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    align-self: flex-start;
}

.invoice-header { text-align: center; margin-bottom: 15px; }

#cart-list { max-height: 350px; overflow-y: auto; padding-right: 5px; }

.summary-line {
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
    font-size: 0.95em;
}

.grand-total {
    font-size: 1.4em;
    font-weight: bold;
    color: var(--hologram-cyan);
    margin-top: 10px;
}

/* ៦. ផ្នែកបង់ប្រាក់តាមធនាគារ (Bank Area) */
#bank-area {
    margin-top: 15px;
    padding: 15px;
    border-radius: 12px;
    border: 1px dashed var(--bank-gold);
    background: rgba(255, 206, 0, 0.05);
    text-align: center;
    animation: pulseGold 2s infinite;
}

@keyframes pulseGold {
    0%, 100% { border-color: var(--bank-gold); }
    50% { border-color: #fff; box-shadow: 0 0 10px rgba(255, 206, 0, 0.2); }
}

#riel-total {
    font-size: 1.6em;
    font-weight: bold;
    color: var(--bank-gold);
    margin: 5px 0;
}

.btn-check {
    width: 100%;
    margin-top: 15px;
    padding: 15px;
    background: var(--hologram-cyan);
    border: none;
    border-radius: 12px;
    font-weight: bold;
    cursor: pointer;
    font-size: 1em;
    transition: 0.3s;
}

.btn-check:hover { filter: brightness(1.2); transform: scale(1.02); }

/* ៧. ផ្ទាំងទូទាត់ (Modal) */
.modal {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.9);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.modal-content {
    background: #0f172a;
    border: 2px solid var(--hologram-cyan);
    border-radius: 25px;
    padding: 30px;
    width: 420px;
    text-align: center;
    box-shadow: 0 0 50px rgba(0, 255, 255, 0.2);
}

.payment-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 20px 0;
}

.btn-pay {
    padding: 12px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.05);
    color: white;
    cursor: pointer;
    font-weight: bold;
}

.btn-pay.aba { background: #003e52; border-color: #00ffff; }

.modal-footer {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

.btn-confirm { flex: 2; padding: 12px; background: #27ae60; border: none; border-radius: 10px; color: white; cursor: pointer; font-weight: bold; }
.btn-cancel { flex: 1; padding: 12px; background: #e74c3c; border: none; border-radius: 10px; color: white; cursor: pointer; }

/* ៨. Loader & Admin */
.loader {
    border: 4px solid rgba(0,255,255,0.1);
    border-left: 4px solid var(--hologram-cyan);
    border-radius: 50%;
    width: 40px; height: 40px;
    animation: spin 1s linear infinite;
    margin: 20px auto;
}
@keyframes spin { 100% { transform: rotate(360deg); } }

.btn-admin-secret {
    position: fixed; bottom: 5px; right: 5px;
    opacity: 0.1; background: none; border: none; color: white; cursor: pointer;
}

/* ៩. Responsive */
@media (max-width: 850px) {
    #main-content { flex-direction: column; }
    #cart { width: 100%; box-sizing: border-box; }
    #menu { grid-template-columns: repeat(2, 1fr); }
}

/* ១០. ប៊ូតុងបែបហូឡូក្រាម */
.btn-holo {
    padding: 12px 24px;
    border-radius: 14px;
    background: linear-gradient(135deg, #00ffff, #00a8ff, #ff00ff);
    color: white;
    font-weight: bold;
    border: none;
    box-shadow: 0 0 12px rgba(0, 255, 255, 0.4);
    transition: 0.3s ease;
    text-transform: uppercase;
}

.btn-holo:hover {
    filter: brightness(1.3);
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.6);
}

/* ១១. ប៊ូតុងបិទបង្អួច */
.btn-close {
    position: absolute;
    top: 15px;
    right: 15px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid var(--hologram-cyan);
    color: var(--hologram-cyan);
    padding: 8px 12px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.2em;
    box-shadow: var(--neon-glow);
}

/* ១២. ប្លង់ហូឡូក្រាម */
.holo-frame {
    border: 2px solid transparent;
    border-image: linear-gradient(45deg, #00ffff, #ff00ff) 1;
    border-radius: 20px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.03);
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.2);
}

/* ១៣ អក្សរបែបហូឡូក្រាម */
.holo-text {
    background: linear-gradient(90deg, #00ffff, #ff00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    font-size: 1.5em;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
}

/* ១៤: LED Running Trace */
.btn-pay.led-loading {
    position: relative;
    overflow: hidden;
    z-index: 1;
    border: none !important;
}

.btn-pay.led-loading::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: conic-gradient(transparent, rgba(0, 255, 255, 0.1), var(--hologram-cyan));
    animation: rotateLED 1.5s linear infinite;
    z-index: -2;
}

.btn-pay.led-loading::after {
    content: '';
    position: absolute;
    inset: 2px;
    background: #0f172a; /* Matches your modal-content background */
    border-radius: inherit;
    z-index: -1;
}

@keyframes rotateLED {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* ១៦: Flight Radar Hologram Skin */
.flight-radar-container {
    position: relative;
    width: 100%;
    height: 250px;
    border-radius: 12px;
    overflow: hidden;
    margin-top: 15px;
    border: 1px solid rgba(0, 255, 255, 0.3);
}

.flight-radar-container iframe {
    width: 100%;
    height: 100%;
    border: none;
    /* Apply digital 'Night Vision' effect to the map */
    filter: hue-rotate(180deg) invert(1) brightness(0.8) contrast(1.2);
    opacity: 0.7;
}

/* Radar Sweep Effect overlay */
.radar-sweep {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(rgba(0, 255, 255, 0.15) 0%, transparent 40%);
    animation: radar-spin 4s linear infinite;
    transform-origin: center;
    pointer-events: none;
    z-index: 5;
}

@keyframes radar-spin {
    from { transform: translate(-50%, -50%) rotate(0deg); }
    to { transform: translate(-50%, -50%) rotate(360deg); }
}
