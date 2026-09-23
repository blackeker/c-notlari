// C Dili Eğitim Portalı Frontend Mantığı (App.js - 30 Gün / 150 Ders / 2-Column Split IDE)

let lessonsData = [];
let quizzesData = {};
let cheatsheetData = [];
let snippetsData = [];
let completedLessons = new Set();
let currentLesson = null;
let compilerInfo = null;
let backendReady = false;
let autoSaveTimer = null;
let currentTheme = 'dark';

// Quiz Yönetim State'i (50 Soru / Gün)
let currentQuizDay = 1;
let currentQuizIndex = 0; // 0..49
let quizUserAnswers = {};
let quizScore = 0;

// Editör Font Zoom State'i
let editorFontSize = 13;

// Markdown İşleyici
function renderMarkdown(md) {
    if (!md) return "";
    let html = md;
    
    html = html.replace(/```c\s*([\s\S]*?)```/g, '<pre><code class="language-c">$1</code></pre>');
    html = html.replace(/```\s*([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^#### (.*$)/gim, '<h4>$1</h4>');
    
    html = html.replace(/^[\-\*]\s+(.*$)/gim, '<li>$1</li>');
    html = html.replace(/(?:<li>.*<\/li>\n?)+/gim, match => `<ul>${match}</ul>`);
    
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    html = html.replace(/^> \[!WARNING\]\s*\n> (.*$)/gim, '<blockquote class="warning-box">⚠️ <strong>UYARI:</strong> $1</blockquote>');
    html = html.replace(/^> (.*$)/gim, '<blockquote>$1</blockquote>');
    html = html.replace(/^---$/gim, '<hr class="md-hr">');
    html = html.replace(/\n\n/g, '<br><br>');
    
    return html;
}

// Uygulama Başlatma
document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

function initApp() {
    setupEventListeners();
    setupEditorShortcuts();
    initResizer();

    let tries = 0;
    const checkInterval = setInterval(() => {
        tries++;
        if (window.pywebview && window.pywebview.api) {
            clearInterval(checkInterval);
            if (!backendReady) {
                backendReady = true;
                onBackendReady();
            }
        } else if (tries >= 30) {
            clearInterval(checkInterval);
            console.warn("PyWebView API zaman aşımı.");
        }
    }, 100);

    window.addEventListener('pywebviewready', () => {
        if (!backendReady && window.pywebview && window.pywebview.api) {
            backendReady = true;
            clearInterval(checkInterval);
            onBackendReady();
        }
    });
}

function onBackendReady() {
    window.pywebview.api.get_compiler_info().then(info => {
        compilerInfo = info;
        updateCompilerStatusUI(info);
    }).catch(err => console.error("Derleyici bilgisi hatası:", err));

    window.pywebview.api.get_progress().then(state => {
        if (state && state.completed_lessons) {
            completedLessons = new Set(state.completed_lessons);
        }
        if (state && state.theme) {
            applyTheme(state.theme);
        }
        
        window.pywebview.api.get_curriculum().then(curriculum => {
            lessonsData = curriculum;
            renderAccordion(curriculum);
            updateProgressBar();

            let activeId = (state && state.active_lesson_id) ? state.active_lesson_id : "1.1";
            selectLesson(activeId);
        }).catch(err => console.error("Müfredat alma hatası:", err));
    }).catch(err => console.error("İlerleme alma hatası:", err));

    window.pywebview.api.get_quizzes().then(qz => {
        quizzesData = qz;
        renderQuizTab();
    }).catch(err => console.error("Quiz alma hatası:", err));

    window.pywebview.api.get_cheatsheet().then(cs => {
        cheatsheetData = cs;
        renderCheatsheetTab();
    }).catch(err => console.error("Cheatsheet alma hatası:", err));

    window.pywebview.api.get_snippets().then(sn => {
        snippetsData = sn;
        renderSnippetsTab();
    }).catch(err => console.error("Snippets alma hatası:", err));
    
    startAutoSave();
}

function initResizer() {
    const resizer = document.getElementById("column-resizer");
    const leftCol = document.getElementById("left-column");
    if (!resizer || !leftCol) return;

    let isDragging = false;

    resizer.addEventListener("mousedown", (e) => {
        isDragging = true;
        resizer.classList.add("dragging");
        document.body.style.cursor = "col-resize";
    });

    document.addEventListener("mousemove", (e) => {
        if (!isDragging) return;
        const mainContent = document.getElementById("main-content");
        const containerRect = mainContent.getBoundingClientRect();
        const newLeftWidth = e.clientX - containerRect.left;
        
        if (newLeftWidth > 280 && newLeftWidth < containerRect.width - 320) {
            leftCol.style.width = newLeftWidth + "px";
        }
    });

    document.addEventListener("mouseup", () => {
        if (isDragging) {
            isDragging = false;
            resizer.classList.remove("dragging");
            document.body.style.cursor = "default";
        }
    });
}

function switchLeftTab(tabName) {
    const tabs = ['theory', 'quiz', 'snippets', 'cheatsheet'];
    tabs.forEach(t => {
        const btn = document.getElementById(`tab-btn-${t}`);
        const content = document.getElementById(`tab-content-${t}`);
        if (t === tabName) {
            if (btn) btn.classList.add("active");
            if (content) content.classList.add("active");
        } else {
            if (btn) btn.classList.remove("active");
            if (content) content.classList.remove("active");
        }
    });

    if (tabName === 'quiz') {
        renderQuizTab();
    }
}

function updateCompilerStatusUI(info) {
    const dot = document.getElementById("compiler-status-dot");
    const text = document.getElementById("compiler-status-text");
    
    if (info && info.available) {
        dot.className = "status-dot green";
        text.innerText = `Derleyici: ${info.name}`;
    } else {
        dot.className = "status-dot red";
        text.innerText = info ? info.name : "Derleyici Bulunamadı (GCC)";
    }
}

function updateLineNumbers() {
    const editor = document.getElementById("code-editor");
    const gutter = document.getElementById("line-numbers");
    if (!editor || !gutter) return;

    const lineCount = editor.value.split('\n').length;
    let numbersHtml = "";
    for (let i = 1; i <= lineCount; i++) {
        numbersHtml += i + "<br>";
    }
    gutter.innerHTML = numbersHtml;
    gutter.scrollTop = editor.scrollTop;
    if (typeof syncHighlight === 'function') syncHighlight();
}

function renderAccordion(lessons) {
    const container = document.getElementById("accordion");
    if (!container) return;
    container.innerHTML = "";

    const daysMap = {};
    lessons.forEach(lesson => {
        if (!daysMap[lesson.day]) {
            daysMap[lesson.day] = {
                day: lesson.day,
                day_title: lesson.day_title,
                lessons: []
            };
        }
        daysMap[lesson.day].lessons.push(lesson);
    });

    Object.keys(daysMap).sort((a, b) => parseInt(a) - parseInt(b)).forEach(dayNum => {
        const group = daysMap[dayNum];
        
        const dayDiv = document.createElement("div");
        dayDiv.className = `day-group ${dayNum == 1 ? "open" : ""}`;
        dayDiv.dataset.day = dayNum;

        const headerDiv = document.createElement("div");
        headerDiv.className = "day-header";
        
        const dayLessons = group.lessons;
        const dayCompleted = dayLessons.filter(l => completedLessons.has(l.id)).length;
        const dayTotal = dayLessons.length;
        const dayPercent = Math.round((dayCompleted / dayTotal) * 100);
        const completedClass = dayCompleted === dayTotal ? ' day-done' : (dayCompleted > 0 ? ' day-partial' : '');
        
        headerDiv.innerHTML = `
            <div class="day-header-left">
                <span>${group.day_title}</span>
                <span class="day-progress-badge${completedClass}">${dayCompleted}/${dayTotal}</span>
            </div>
            <div class="day-header-right">
                <div class="day-mini-progress">
                    <div class="day-mini-bar" style="width: ${dayPercent}%"></div>
                </div>
                <span class="arrow">▶</span>
            </div>
        `;
        headerDiv.onclick = () => {
            dayDiv.classList.toggle("open");
        };

        const listDiv = document.createElement("div");
        listDiv.className = "lesson-list";

        group.lessons.forEach(les => {
            const itemDiv = document.createElement("div");
            itemDiv.className = "lesson-item";
            itemDiv.dataset.id = les.id;

            const isChecked = completedLessons.has(les.id) ? "checked" : "";

            itemDiv.innerHTML = `
                <input type="checkbox" ${isChecked} onclick="toggleLessonCheck(event, '${les.id}')" />
                <span class="lesson-title-text">${les.title}</span>
            `;

            itemDiv.onclick = (e) => {
                if (e.target.tagName !== 'INPUT') {
                    selectLesson(les.id);
                }
            };

            listDiv.appendChild(itemDiv);
        });

        dayDiv.appendChild(headerDiv);
        dayDiv.appendChild(listDiv);
        container.appendChild(dayDiv);
    });
}

function selectLesson(lessonId) {
    const les = lessonsData.find(l => l.id === lessonId);
    if (!les) return;

    currentLesson = les;

    document.querySelectorAll('.lesson-item').forEach(el => {
        if (el.dataset.id === lessonId) {
            el.classList.add('active');
            const parentGroup = el.closest('.day-group');
            if (parentGroup) parentGroup.classList.add('open');
        } else {
            el.classList.remove('active');
        }
    });

    document.getElementById("current-day-badge").innerText = `GÜN ${les.day}`;
    document.getElementById("current-lesson-id").innerText = les.id;
    document.getElementById("current-lesson-title").innerText = les.title;
    document.getElementById("theory-content").innerHTML = renderMarkdown(les.theory);

    updateCompletedBtnUI(les.id);

    if (window.pywebview && window.pywebview.api) {
        window.pywebview.api.get_draft(les.id).then(draft => {
            document.getElementById("code-editor").value = draft ? draft : les.starter_code;
            updateLineNumbers();
            updateRAMInspector();
        }).catch(() => {
            document.getElementById("code-editor").value = les.starter_code;
            updateLineNumbers();
            updateRAMInspector();
        });

        window.pywebview.api.set_active_lesson(les.id);
    } else {
        document.getElementById("code-editor").value = les.starter_code;
        updateLineNumbers();
        updateRAMInspector();
    }
}

function toggleLessonCheck(event, lessonId) {
    event.stopPropagation();
    const isCompleted = event.target.checked;
    
    if (isCompleted) {
        completedLessons.add(lessonId);
    } else {
        completedLessons.delete(lessonId);
    }

    if (window.pywebview && window.pywebview.api) {
        window.pywebview.api.mark_completed(lessonId, isCompleted);
    }

    updateProgressBar();
    if (currentLesson && currentLesson.id === lessonId) {
        updateCompletedBtnUI(lessonId);
    }
}

function updateCompletedBtnUI(lessonId) {
    const btn = document.getElementById("btn-toggle-completed");
    if (!btn) return;
    if (completedLessons.has(lessonId)) {
        btn.innerHTML = `✓ Tamamlandı`;
        btn.classList.replace("btn-outline", "btn-primary");
    } else {
        btn.innerHTML = `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Tamamlandı`;
        btn.classList.replace("btn-primary", "btn-outline");
    }
}

function updateProgressBar() {
    const total = 150;
    const count = completedLessons.size;
    const percent = Math.round((count / total) * 100);

    const txt = document.getElementById("progress-text");
    const cnt = document.getElementById("progress-count");
    const fill = document.getElementById("progress-bar-fill");

    if (txt) txt.innerText = `%${percent} Tamamlandı`;
    if (cnt) cnt.innerText = `${count}/${total} Ders`;
    if (fill) fill.style.width = `${percent}%`;
}

function filterLessons(query) {
    const q = query.toLowerCase().trim();
    
    document.querySelectorAll('.day-group').forEach(group => {
        let hasMatch = false;
        group.querySelectorAll('.lesson-item').forEach(item => {
            const title = item.querySelector('.lesson-title-text').innerText.toLowerCase();
            const lesId = item.dataset.id;

            if (title.includes(q) || lesId.includes(q)) {
                item.style.display = 'flex';
                hasMatch = true;
            } else {
                item.style.display = 'none';
            }
        });

        if (hasMatch || q === "") {
            group.style.display = 'block';
            if (q !== "") group.classList.add('open');
        } else {
            group.style.display = 'none';
        }
    });
}

function analyzeCCode() {
    const code = document.getElementById("code-editor").value;
    const termBody = document.getElementById("terminal-body");
    const warnings = [];

    if (/malloc|calloc|realloc/i.test(code) && !/free\s*\(/i.test(code)) {
        warnings.push("⚠️ <strong>Bellek Sızıntısı Uyarısı:</strong> Kodda dinamik bellek tahsisi (malloc/calloc) bulundu ancak <code>free()</code> ile serbest bırakılmamış olabilir!");
    }

    if (/\bgets\s*\(/i.test(code)) {
        warnings.push("⚠️ <strong>Güvenlik Uyarısı:</strong> <code>gets()</code> fonksiyonu bellek taşması riski taşır! Bunun yerine <code>fgets()</code> kullanın.");
    }

    if (/scanf\s*\(\s*"%s"/i.test(code)) {
        warnings.push("⚠️ <strong>Tampon Uyarısı:</strong> <code>scanf(\"%s\")</code> genişlik sınırı konulmazsa bellek taşabilir.");
    }

    if (warnings.length === 0) {
        termBody.innerHTML = `<div class="term-success">✨ Statik Kod Analizi: Kodda belirgin bellek sızıntısı veya güvenlik uyarısı tespit edilmedi.</div>`;
    } else {
        termBody.innerHTML = warnings.map(w => `<div class="linter-box">${w}</div>`).join('');
    }
}

function runCode() {
    const code = document.getElementById("code-editor").value;
    const stdinEl = document.getElementById("stdin-input");
    const stdinInput = stdinEl ? stdinEl.value : "";
    const termBody = document.getElementById("terminal-body");
    const execInfo = document.getElementById("terminal-exec-info");

    const usesScanf = /scanf|getchar|gets|fgets/i.test(code);
    if (usesScanf && !stdinInput.trim()) {
        stdinEl.classList.add("highlight-input");
        setTimeout(() => stdinEl.classList.remove("highlight-input"), 3000);
    }

    updateRAMInspector();

    termBody.innerHTML = `<span class="term-dim">Derleniyor ve çalıştırılıyor (GCC)...</span>`;
    execInfo.innerText = "GCC Çalıştırılıyor...";

    if (window.pywebview && window.pywebview.api) {
        window.pywebview.api.compile_and_run(code, stdinInput).then(res => {
            renderTerminalResult(res, usesScanf, stdinInput);
        }).catch(err => {
            termBody.innerHTML = `<span class="term-stderr">HATA: Derleme çağrısı başarısız oldu: ${err}</span>`;
            execInfo.innerText = "Hata Oluştu";
        });
    } else {
        termBody.innerHTML = `<span class="term-stderr">Derleyici API bağlantısı kuruluyor... Lütfen uygulamayı masaüstünden (.exe) çalıştırın.</span>`;
        execInfo.innerText = "Bağlantı Bekleniyor";
    }
}

function renderTerminalResult(res, usesScanf, stdinInput) {
    const termBody = document.getElementById("terminal-body");
    const execInfo = document.getElementById("terminal-exec-info");

    termBody.innerHTML = "";

    if (usesScanf && !stdinInput.trim()) {
        const hintDiv = document.createElement("div");
        hintDiv.className = "scanf-hint-box";
        hintDiv.innerHTML = `💡 <strong>İPUCU:</strong> Kodunuz <code>scanf()</code> ile klavyeden değer bekliyor.<br>Girdilerinizi (örneğin: <code>10 20</code>) aşağıdaki kutucuğa yazıp Enter'a veya Kodu Çalıştır'a basın.`;
        termBody.appendChild(hintDiv);
    }

    if (res.stderr && res.stderr.trim() !== "") {
        let formattedStderr = res.stderr;
        formattedStderr = formattedStderr.replace(/program\.c:(\d+):(\d+):/g, (match, lineNum, colNum) => {
            return `<span class="error-line-link" onclick="jumpToEditorLine(${lineNum})">[Satır ${lineNum}:${colNum}]</span>`;
        });

        const errDiv = document.createElement("div");
        errDiv.className = res.success ? "term-warning" : "term-stderr";
        errDiv.innerHTML = formattedStderr + "\n";
        termBody.appendChild(errDiv);
    }

    if (res.stdout && res.stdout.trim() !== "") {
        const outSpan = document.createElement("span");
        outSpan.className = "term-stdout";
        outSpan.innerText = res.stdout;
        termBody.appendChild(outSpan);
    }

    if (res.success) {
        execInfo.innerText = `Süre: ${res.elapsed_time}s | Exit Code: ${res.exit_code}`;
        const statusSpan = document.createElement("span");
        statusSpan.className = "term-success";
        statusSpan.innerText = `\n[Program başarıyla tamamlandı (Exit Code ${res.exit_code})]`;
        termBody.appendChild(statusSpan);
    } else {
        execInfo.innerText = `Hata ile sonlandı (${res.stage})`;
        const statusSpan = document.createElement("span");
        statusSpan.className = "term-stderr";
        statusSpan.innerText = `\n[Derleme/Çalıştırma Hatası]`;
        termBody.appendChild(statusSpan);
    }

    termBody.scrollTop = termBody.scrollHeight;
}

function jumpToEditorLine(lineNum) {
    const editor = document.getElementById("code-editor");
    if (!editor) return;

    const lines = editor.value.split('\n');
    if (lineNum > lines.length) return;

    let pos = 0;
    for (let i = 0; i < lineNum - 1; i++) {
        pos += lines[i].length + 1;
    }

    editor.focus();
    editor.selectionStart = pos;
    editor.selectionEnd = pos + lines[lineNum - 1].length;
}

// === CANLI STACK & HEAP RAM HARİTASI ===
function updateRAMInspector() {
    const container = document.getElementById("ram-table-container");
    if (!container) return;

    const code = document.getElementById("code-editor").value;
    const { stackVars, heapVars } = parseCVariables(code);

    if (stackVars.length === 0 && heapVars.length === 0) {
        container.innerHTML = `<span class="term-dim">Kodda tanımlanmış belirgin değişken bulunamadı.</span>`;
        return;
    }

    container.innerHTML = "";

    // STACK SECTION
    if (stackVars.length > 0) {
        const stackTitle = document.createElement("div");
        stackTitle.className = "ram-section-title";
        stackTitle.innerText = "📌 STACK BELLEK";
        container.appendChild(stackTitle);

        stackVars.forEach(v => {
            const card = document.createElement("div");
            card.className = `ram-var-card ${v.isPointer ? "is-pointer" : ""}`;
            card.innerHTML = `
                <div>
                    <span class="ram-addr">${v.address}</span>
                    <span class="ram-name">${v.type} ${v.name}</span>
                    <span class="ram-val">${v.value}</span>
                </div>
                ${v.isPointer ? `<div class="ram-ptr-target">➜ Hedef Adres: ${v.targetAddress}</div>` : ""}
            `;
            container.appendChild(card);
        });
    }

    // HEAP SECTION
    if (heapVars.length > 0) {
        const heapTitle = document.createElement("div");
        heapTitle.className = "ram-section-title";
        heapTitle.innerText = "💾 HEAP BELLEK (malloc / calloc)";
        container.appendChild(heapTitle);

        heapVars.forEach(v => {
            const card = document.createElement("div");
            card.className = "ram-var-card heap-card";
            card.innerHTML = `
                <div>
                    <span class="ram-addr">${v.address}</span>
                    <span class="ram-name">${v.type} ${v.name}</span>
                    <span class="ram-val">${v.size} Bayt</span>
                </div>
            `;
            container.appendChild(card);
        });
    }
}

function parseCVariables(code) {
    const stackVars = [];
    const heapVars = [];
    let baseAddr = 0x7FFE000;
    let heapAddr = 0x01A0000;
    const addrMap = {};
    let match;

    // 1. Array and String Declarations
    const arrRegex = /(int|float|double|char|short|long|struct\s+[a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\[(.*?)\](?:\s*=\s*([^;]+))?;/g;
    while ((match = arrRegex.exec(code)) !== null) {
        const type = match[1];
        const name = match[2];
        const sizeInfo = match[3].trim();
        const initVal = match[4] ? match[4].trim() : (sizeInfo ? `[size ${sizeInfo}]` : "[]");

        baseAddr += 16;
        const hexAddr = "0x" + baseAddr.toString(16).toUpperCase();
        addrMap[name] = hexAddr;

        stackVars.push({ address: hexAddr, type: `${type}[${sizeInfo}]`, name: name, value: initVal, isPointer: false });
    }

    // 2. Standard vars (including in for loops and structs)
    const varRegex = /(?:for\s*\(\s*)?(int|float|double|char|short|long|struct\s+[a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)(?:\s*=\s*([^;,\)]+))?[;,\)]/g;
    while ((match = varRegex.exec(code)) !== null) {
        const type = match[1];
        const name = match[2];
        const val = match[3] ? match[3].trim() : "uninitialized";

        baseAddr += 4;
        const hexAddr = "0x" + baseAddr.toString(16).toUpperCase();
        addrMap[name] = hexAddr;

        stackVars.push({ address: hexAddr, type: type, name: name, value: val, isPointer: false });
    }

    // 3. Pointers
    const ptrRegex = /(int|float|double|char|struct\s+[a-zA-Z_][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*&?([a-zA-Z_][a-zA-Z0-9_]*);/g;
    while ((match = ptrRegex.exec(code)) !== null) {
        const type = match[1] + "*";
        const name = match[2];
        const targetName = match[3];
        
        baseAddr += 8;
        const hexAddr = "0x" + baseAddr.toString(16).toUpperCase();

        const targetAddr = addrMap[targetName] || ("&" + targetName);

        stackVars.push({ address: hexAddr, type: type, name: name, value: targetAddr, isPointer: true, targetAddress: targetAddr });
    }

    // 4. Heap Allocation
    const heapRegex = /(int|float|double|char|struct\s+[a-zA-Z_][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\([^)]+\)\s*(malloc|calloc)\s*\(([^)]+)\);/g;
    while ((match = heapRegex.exec(code)) !== null) {
        const type = match[1] + "*";
        const name = match[2];
        const allocSize = match[4].trim();
        heapAddr += 32;
        const hexAddr = "0x0" + heapAddr.toString(16).toUpperCase();

        heapVars.push({ address: hexAddr, type: type, name: name, size: allocSize });
    }

    return { stackVars, heapVars };
}

function renderQuizTab() {
    if (!currentLesson) return;
    
    if (currentQuizDay !== currentLesson.day) {
        currentQuizDay = currentLesson.day;
        quizUserAnswers = {};
        quizScore = 0;
        currentQuizIndex = 0;
    }

    const title = document.getElementById("quiz-tab-title");
    if (title) title.innerText = `🧠 GÜN ${currentQuizDay} Quizi (50 Soru)`;

    const select = document.getElementById("quiz-jump-select");
    if (select) {
        select.innerHTML = "";
        for (let i = 0; i < 50; i++) {
            const opt = document.createElement("option");
            opt.value = i;
            opt.innerText = `Soru ${i + 1}`;
            select.appendChild(opt);
        }
        select.value = currentQuizIndex;
        select.onchange = (e) => {
            currentQuizIndex = parseInt(e.target.value);
            renderCurrentQuizQuestion();
        };
    }

    renderCurrentQuizQuestion();
}

function renderCurrentQuizQuestion() {
    const dayQuizzes = quizzesData[currentQuizDay] || [];
    const body = document.getElementById("quiz-tab-body");
    const counterText = document.getElementById("quiz-counter-text");
    const scoreBadge = document.getElementById("quiz-score-badge");
    const select = document.getElementById("quiz-jump-select");

    if (select) select.value = currentQuizIndex;
    if (counterText) counterText.innerText = `Soru ${currentQuizIndex + 1} / ${dayQuizzes.length}`;
    if (scoreBadge) scoreBadge.innerText = `Skor: ${quizScore} / ${dayQuizzes.length}`;

    if (!body) return;
    if (!dayQuizzes || dayQuizzes.length === 0 || !dayQuizzes[currentQuizIndex]) {
        body.innerHTML = `<p class="term-dim">Bu soru yüklenemedi.</p>`;
        return;
    }

    const q = dayQuizzes[currentQuizIndex];
    const answeredOpt = quizUserAnswers[currentQuizIndex];

    const card = document.createElement("div");
    card.className = "quiz-q-card";

    card.innerHTML = `
        <div class="quiz-question-text">${currentQuizIndex + 1}. ${q.question}</div>
        <div class="quiz-options-list">
            ${q.options.map((opt, oIdx) => {
                let btnClass = "quiz-option-btn";
                if (answeredOpt !== undefined) {
                    if (oIdx === q.answer) btnClass += " correct";
                    else if (oIdx === answeredOpt) btnClass += " incorrect";
                }
                return `
                    <button class="${btnClass}" ${answeredOpt !== undefined ? "disabled" : ""} onclick="answerQuizQuestion(${currentQuizIndex}, ${oIdx})">
                        ${String.fromCharCode(65 + oIdx)}) ${opt}
                    </button>
                `;
            }).join('')}
        </div>
        ${answeredOpt !== undefined ? `
        <div class="quiz-explanation ${answeredOpt === q.answer ? 'correct' : 'wrong'}">
            <strong>${answeredOpt === q.answer ? '✓ Doğru!' : '✗ Yanlış! Doğru cevap: ' + q.options[q.answer]}</strong>
            <p>${q.explanation}</p>
        </div>` : ""}
    `;

    body.innerHTML = "";
    body.appendChild(card);
}

function answerQuizQuestion(qIdx, selectedIdx) {
    if (quizUserAnswers[qIdx] !== undefined) return;

    quizUserAnswers[qIdx] = selectedIdx;
    const q = quizzesData[currentQuizDay][qIdx];

    if (selectedIdx === q.answer) {
        quizScore++;
    }

    renderCurrentQuizQuestion();
}

function prevQuizQuestion() {
    if (currentQuizIndex > 0) {
        currentQuizIndex--;
        renderCurrentQuizQuestion();
    }
}

function nextQuizQuestion() {
    const dayQuizzes = quizzesData[currentQuizDay] || [];
    if (currentQuizIndex < dayQuizzes.length - 1) {
        currentQuizIndex++;
        renderCurrentQuizQuestion();
    }
}

function renderSnippetsTab() {
    const body = document.getElementById("snippets-tab-body");
    if (!body) return;
    body.innerHTML = "";

    if (!snippetsData || snippetsData.length === 0) {
        body.innerHTML = `<p class="term-dim">Şablon kütüphanesi yüklenemedi.</p>`;
    } else {
        snippetsData.forEach(s => {
            const card = document.createElement("div");
            card.className = "snippet-card";
            card.innerHTML = `
                <div class="snippet-title">${s.title} <span class="snippet-cat">${s.category}</span></div>
                <pre class="snippet-code-prev"><code>${s.code}</code></pre>
                <button class="btn btn-secondary btn-small" onclick="insertSnippet('${s.id}')">Editöre Aktar</button>
            `;
            body.appendChild(card);
        });
    }
}

function insertSnippet(snippetId) {
    const s = snippetsData.find(sn => sn.id === snippetId);
    if (!s) return;

    document.getElementById("code-editor").value = s.code;
    updateLineNumbers();
    updateRAMInspector();
}

function renderCheatsheetTab() {
    const body = document.getElementById("cheatsheet-tab-body");
    if (!body) return;
    body.innerHTML = "";

    if (!cheatsheetData || cheatsheetData.length === 0) {
        body.innerHTML = `<p class="term-dim">Rehber yüklenemedi.</p>`;
    } else {
        cheatsheetData.forEach(lib => {
            const sec = document.createElement("div");
            sec.className = "cs-lib-section";
            sec.innerHTML = `
                <div class="cs-lib-title">${lib.library} - ${lib.desc}</div>
                ${lib.functions.map(f => `
                    <div class="cs-func-item">
                        <span class="cs-func-name">${f.name}</span>
                        <span class="cs-func-desc">${f.desc}</span>
                    </div>
                `).join('')}
            `;
            body.appendChild(sec);
        });
    }
}

function openAchievementsModal() {
    const modal = document.getElementById("achievements-modal");
    if (!modal) return;
    modal.classList.remove("hidden");

    const achievementsGrid = document.getElementById("achievements-grid");
    const certStamp = document.getElementById("cert-badge-stamp");
    
    let completedDays = new Set();
    completedLessons.forEach(id => {
        const les = lessonsData.find(l => l.id === id);
        if (les) completedDays.add(String(les.day));
    });

    const achs = [
        { title: "C Yolculuğu Başladı", icon: "🚀", unlocked: completedLessons.size >= 1 },
        { title: "İlk Hafta Tamamlandı", icon: "📅", unlocked: completedLessons.size >= 35 },
        { title: "Pointer Ustası", icon: "🧠", unlocked: completedDays.has("14") || completedDays.has("15") },
        { title: "Dinamik Bellek Yöneticisi", icon: "💾", unlocked: completedDays.has("18") },
        { title: "Yarı Yol", icon: "⭐", unlocked: completedLessons.size >= 75 },
        { title: "Algoritma Gurusu", icon: "⚡", unlocked: completedDays.has("27") || completedDays.has("28") },
        { title: "Veri Yapıları Uzmanı", icon: "🏗️", unlocked: completedDays.has("24") || completedDays.has("25") },
        { title: "C Masterclass Mezunu", icon: "👑", unlocked: completedLessons.size >= 150 }
    ];

    if (achievementsGrid) {
        achievementsGrid.innerHTML = achs.map(a => `
            <div class="ach-card ${a.unlocked ? 'unlocked' : 'locked'}">
                <div class="ach-icon">${a.unlocked ? a.icon : '🔒'}</div>
                <div class="ach-info">
                    <div class="ach-title">${a.title}</div>
                </div>
            </div>
        `).join('');
    }

    if (certStamp) {
        if (completedLessons.size >= 150) {
            certStamp.innerText = "C PROGRAMMING CERTIFIED";
        } else {
            const percent = Math.round((completedLessons.size / 150) * 100);
            certStamp.innerText = `TAMAMLANMA: %${percent}`;
        }
    }
}

function openShortcutsModal() {
    const modal = document.getElementById("shortcuts-modal");
    if (!modal) return;
    modal.classList.remove("hidden");

    const grid = document.getElementById("shortcuts-grid");
    if (!grid) return;

    const shortcuts = [
        { key: "F1", desc: "Kısayol Yardımı" },
        { key: "F5 / F9 / F10", desc: "Kodu Çalıştır" },
        { key: "F11", desc: "Tam Ekran" },
        { key: "Ctrl + S", desc: "Taslak Kaydet" },
        { key: "Ctrl + /", desc: "Yorum Satırı (Aç/Kapat)" },
        { key: "Ctrl + D", desc: "Bulunulan Satırı Kopyala (Altına)" },
        { key: "Ctrl + E", desc: "Bulunulan Satırı Sil" },
        { key: "Ctrl + Shift + ↑", desc: "Satırı Yukarı Taşı" },
        { key: "Ctrl + Shift + ↓", desc: "Satırı Aşağı Taşı" },
        { key: "Tab", desc: "Girinti Ekle (4 Boşluk)" },
        { key: "Shift + Tab", desc: "Girinti Kaldır (4 Boşluk)" },
        { key: "Ctrl + A", desc: "Tümünü Seç" },
        { key: "Ctrl + Z", desc: "Geri Al" }
    ];

    grid.innerHTML = shortcuts.map(s => `
        <div class="shortcut-item">
            <span class="shortcut-desc">${s.desc}</span>
            <span class="shortcut-key">${s.key}</span>
        </div>
    `).join('');
}

function formatCCode() {
    const editor = document.getElementById("code-editor");
    if (!editor) return;

    let lines = editor.value.split('\n');
    let indentLevel = 0;
    let formatted = [];

    lines.forEach(line => {
        let trimmed = line.trim();
        if (!trimmed) {
            formatted.push("");
            return;
        }

        if (trimmed.startsWith('}')) {
            indentLevel = Math.max(0, indentLevel - 1);
        }

        formatted.push("    ".repeat(indentLevel) + trimmed);

        if (trimmed.endsWith('{')) {
            indentLevel++;
        }
    });

    editor.value = formatted.join('\n');
    updateLineNumbers();
}

function saveDraft() {
    if (currentLesson && window.pywebview && window.pywebview.api) {
        const code = document.getElementById("code-editor").value;
        window.pywebview.api.save_draft(currentLesson.id, code);
        return true;
    }
    return false;
}

function showAutoSaveIndicator() {
    const indicator = document.getElementById("autosave-indicator");
    if (indicator) {
        indicator.innerText = "Kaydedildi ✓";
        indicator.classList.add("show");
        setTimeout(() => {
            indicator.classList.remove("show");
        }, 2000);
    }
}

function applyTheme(theme) {
    currentTheme = theme;
    if (theme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    } else {
        document.documentElement.removeAttribute('data-theme');
    }
    const btn = document.getElementById("btn-toggle-theme");
    if (btn) {
        btn.innerText = theme === 'dark' ? '🌙' : '☀️';
    }
}

function toggleTheme() {
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
    if (window.pywebview && window.pywebview.api && window.pywebview.api.save_theme) {
        window.pywebview.api.save_theme(newTheme);
    }
}

function startAutoSave() {
    if (autoSaveTimer) clearInterval(autoSaveTimer);
    autoSaveTimer = setInterval(() => {
        if (saveDraft()) {
            showAutoSaveIndicator();
        }
    }, 30000);
}

function exportNotes() {
    if (window.pywebview && window.pywebview.api) {
        window.pywebview.api.export_notes().then(mdContent => {
            const blob = new Blob([mdContent], { type: "text/markdown;charset=utf-8;" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "C_Dili_30_Gunluk_150_Derslik_Egitim_Notlari.md";
            a.click();
            URL.revokeObjectURL(url);
        });
    }
}

function changeFontSize(delta) {
    editorFontSize = Math.min(24, Math.max(10, editorFontSize + delta));
    const editor = document.getElementById("code-editor");
    const gutter = document.getElementById("line-numbers");
    const pre = document.getElementById("code-highlight");
    if (editor) editor.style.fontSize = editorFontSize + "px";
    if (gutter) gutter.style.fontSize = editorFontSize + "px";
    if (pre) pre.style.fontSize = editorFontSize + "px";
    syncHighlight();
}

function setupEditorShortcuts() {
    const editor = document.getElementById("code-editor");
    if (!editor) return;

    editor.addEventListener("input", () => {
        updateLineNumbers();
        updateRAMInspector();
        syncHighlight();
    });

    editor.addEventListener("scroll", () => {
        const gutter = document.getElementById("line-numbers");
        if (gutter) gutter.scrollTop = editor.scrollTop;
        const pre = document.getElementById("code-highlight");
        if (pre) {
            pre.scrollTop = editor.scrollTop;
            pre.scrollLeft = editor.scrollLeft;
        }
    });

    editor.addEventListener("keydown", (e) => {
        if (e.key === "Tab") {
            e.preventDefault();
            const start = editor.selectionStart;
            const end = editor.selectionEnd;
            const value = editor.value;

            if (start === end && !e.shiftKey) {
                editor.value = value.substring(0, start) + "    " + value.substring(end);
                editor.selectionStart = editor.selectionEnd = start + 4;
            } else {
                const lineStart = value.lastIndexOf('\n', start - 1) + 1;
                let lineEnd = value.indexOf('\n', end);
                if (lineEnd === -1) lineEnd = value.length;

                const lines = value.substring(lineStart, lineEnd).split('\n');
                let newLines;

                if (!e.shiftKey) {
                    newLines = lines.map(line => "    " + line);
                } else {
                    newLines = lines.map(line => line.replace(/^( {1,4}|\t)/, ''));
                }

                const newText = newLines.join('\n');
                editor.value = value.substring(0, lineStart) + newText + value.substring(lineEnd);
                editor.selectionStart = lineStart;
                editor.selectionEnd = lineStart + newText.length;
            }
            updateLineNumbers();
            updateRAMInspector();
        }

        else if ((e.ctrlKey && e.key === "/") || (e.ctrlKey && e.key.toLowerCase() === "k")) {
            e.preventDefault();
            toggleComment(editor);
        }

        else if (e.ctrlKey && e.key.toLowerCase() === "d") {
            e.preventDefault();
            duplicateLine(editor);
        }

        else if (e.ctrlKey && e.shiftKey && (e.key === "ArrowUp" || e.key === "ArrowDown")) {
            e.preventDefault();
            moveLine(editor, e.key === "ArrowUp" ? -1 : 1);
        }

        else if (e.ctrlKey && e.key.toLowerCase() === "e") {
            e.preventDefault();
            deleteLine(editor);
        }
    });
}

function toggleComment(editor) {
    const start = editor.selectionStart;
    const end = editor.selectionEnd;
    const value = editor.value;

    const lineStart = value.lastIndexOf('\n', start - 1) + 1;
    let lineEnd = value.indexOf('\n', end);
    if (lineEnd === -1) lineEnd = value.length;

    const lines = value.substring(lineStart, lineEnd).split('\n');
    const allCommented = lines.every(l => l.trim().startsWith('//'));

    const newLines = lines.map(line => {
        if (allCommented) {
            return line.replace(/^(\s*)\/\/\s?/, '$1');
        } else {
            return '// ' + line;
        }
    });

    const newText = newLines.join('\n');
    editor.value = value.substring(0, lineStart) + newText + value.substring(lineEnd);
    editor.selectionStart = lineStart;
    editor.selectionEnd = lineStart + newText.length;
    updateLineNumbers();
}

function duplicateLine(editor) {
    const start = editor.selectionStart;
    const end = editor.selectionEnd;
    const value = editor.value;

    const lineStart = value.lastIndexOf('\n', start - 1) + 1;
    let lineEnd = value.indexOf('\n', end);
    if (lineEnd === -1) lineEnd = value.length;

    const currentText = value.substring(lineStart, lineEnd);
    const insertText = "\n" + currentText;

    editor.value = value.substring(0, lineEnd) + insertText + value.substring(lineEnd);
    editor.selectionStart = lineEnd + insertText.length;
    editor.selectionEnd = lineEnd + insertText.length;
    updateLineNumbers();
}

function moveLine(editor, direction) {
    const start = editor.selectionStart;
    const value = editor.value;

    const lines = value.split('\n');
    let currentLineIndex = value.substring(0, start).split('\n').length - 1;
    let targetIndex = currentLineIndex + direction;

    if (targetIndex < 0 || targetIndex >= lines.length) return;

    const temp = lines[currentLineIndex];
    lines[currentLineIndex] = lines[targetIndex];
    lines[targetIndex] = temp;

    editor.value = lines.join('\n');
    let newPos = 0;
    for (let i = 0; i < targetIndex; i++) {
        newPos += lines[i].length + 1;
    }
    editor.selectionStart = editor.selectionEnd = newPos;
    updateLineNumbers();
}

function deleteLine(editor) {
    const start = editor.selectionStart;
    const end = editor.selectionEnd;
    const value = editor.value;

    const lineStart = value.lastIndexOf('\n', start - 1) + 1;
    let lineEnd = value.indexOf('\n', end);
    if (lineEnd === -1) lineEnd = value.length;
    else lineEnd += 1;

    editor.value = value.substring(0, lineStart) + value.substring(lineEnd);
    editor.selectionStart = editor.selectionEnd = lineStart;
    updateLineNumbers();
}

function setupEventListeners() {
    const searchInput = document.getElementById("search-input");
    if (searchInput) searchInput.addEventListener("input", (e) => filterLessons(e.target.value));

    const btnLoad = document.getElementById("btn-load-code");
    if (btnLoad) btnLoad.addEventListener("click", () => {
        if (currentLesson) {
            document.getElementById("code-editor").value = currentLesson.starter_code;
            updateLineNumbers();
            updateRAMInspector();
        }
    });

    const btnComp = document.getElementById("btn-toggle-completed");
    if (btnComp) btnComp.addEventListener("click", () => {
        if (!currentLesson) return;
        const isComp = completedLessons.has(currentLesson.id);
        const newCompState = !isComp;
        
        if (newCompState) completedLessons.add(currentLesson.id);
        else completedLessons.delete(currentLesson.id);

        const cb = document.querySelector(`.lesson-item[data-id="${currentLesson.id}"] input`);
        if (cb) cb.checked = newCompState;

        updateCompletedBtnUI(currentLesson.id);
        updateProgressBar();

        if (window.pywebview && window.pywebview.api) {
            window.pywebview.api.mark_completed(currentLesson.id, newCompState);
        }
    });

    const btnRun = document.getElementById("btn-run-code");
    if (btnRun) btnRun.addEventListener("click", runCode);

    const btnAnalyze = document.getElementById("btn-analyze-code");
    if (btnAnalyze) btnAnalyze.addEventListener("click", analyzeCCode);

    const btnReset = document.getElementById("btn-reset-code");
    if (btnReset) btnReset.addEventListener("click", () => {
        if (currentLesson) {
            document.getElementById("code-editor").value = currentLesson.starter_code;
            updateLineNumbers();
            updateRAMInspector();
        }
    });

    const btnClear = document.getElementById("btn-clear-code");
    if (btnClear) btnClear.addEventListener("click", () => {
        document.getElementById("code-editor").value = "";
        updateLineNumbers();
        updateRAMInspector();
    });

    const btnFormat = document.getElementById("btn-format-code");
    if (btnFormat) btnFormat.addEventListener("click", formatCCode);

    const btnExport = document.getElementById("btn-export-notes");
    if (btnExport) btnExport.addEventListener("click", exportNotes);

    const btnToggleTheme = document.getElementById("btn-toggle-theme");
    if (btnToggleTheme) btnToggleTheme.addEventListener("click", toggleTheme);

    const btnAch = document.getElementById("btn-open-achievements");
    if (btnAch) btnAch.addEventListener("click", openAchievementsModal);

    const btnCloseAch = document.getElementById("btn-close-achievements");
    if (btnCloseAch) btnCloseAch.addEventListener("click", () => {
        document.getElementById("achievements-modal").classList.add("hidden");
    });
    
    const btnCloseShortcuts = document.getElementById("btn-close-shortcuts");
    if (btnCloseShortcuts) btnCloseShortcuts.addEventListener("click", () => {
        document.getElementById("shortcuts-modal").classList.add("hidden");
    });

    const btnZoomIn = document.getElementById("btn-zoom-in");
    if (btnZoomIn) btnZoomIn.addEventListener("click", () => changeFontSize(1));

    const btnZoomOut = document.getElementById("btn-zoom-out");
    if (btnZoomOut) btnZoomOut.addEventListener("click", () => changeFontSize(-1));

    const btnRAM = document.getElementById("btn-toggle-ram");
    if (btnRAM) btnRAM.addEventListener("click", () => {
        const panel = document.getElementById("ram-inspector-panel");
        panel.classList.toggle("hidden");
        updateRAMInspector();
    });

    const btnCloseRAM = document.getElementById("btn-close-ram");
    if (btnCloseRAM) btnCloseRAM.addEventListener("click", () => {
        document.getElementById("ram-inspector-panel").classList.add("hidden");
    });

    const btnQuiz = document.getElementById("btn-open-quiz");
    if (btnQuiz) btnQuiz.addEventListener("click", () => {
        switchLeftTab('quiz');
    });

    const quizPrev = document.getElementById("quiz-prev-btn");
    if (quizPrev) quizPrev.addEventListener("click", prevQuizQuestion);

    const quizNext = document.getElementById("quiz-next-btn");
    if (quizNext) quizNext.addEventListener("click", nextQuizQuestion);

    const btnSend = document.getElementById("btn-send-stdin");
    if (btnSend) btnSend.addEventListener("click", runCode);
    
    const stdinInp = document.getElementById("stdin-input");
    if (stdinInp) {
        stdinInp.addEventListener("keydown", (e) => {
            if (e.key === "Enter") runCode();
        });
    }

    document.addEventListener("keydown", (e) => {
        if (e.key === "F1") {
            e.preventDefault();
            openShortcutsModal();
        } else if (e.key === "F9" || e.key === "F10" || e.key === "F11" || e.key === "F5") {
            e.preventDefault();
            runCode();
        } else if (e.ctrlKey && e.key.toLowerCase() === "s") {
            e.preventDefault();
            if (saveDraft()) {
                const execInfo = document.getElementById("terminal-exec-info");
                if (execInfo) execInfo.innerText = "Taslak kaydedildi!";
                showAutoSaveIndicator();
            }
        }
    });
}

// === SYNTAX HIGHLIGHTING ===
function highlightCCode(code) {
    if (!code) return "";
    
    let escapedCode = code
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
    
    const regex = /(\/\/.*|\/\*[\s\S]*?\*\/)|("[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')|(^[ \t]*#.*)|\b(int|float|double|char|void|return|if|else|for|while|do|switch|case|break|continue|default|struct|union|enum|typedef|sizeof|const|static|extern|unsigned|signed|long|short|volatile|register|goto|NULL)\b|(\b[a-zA-Z_]\w*\b)(?=\s*\()|(\b\d+(?:\.\d+)?(?:[fFlL])?\b)|([+\-*/=!|^~%?]+|&lt;|&gt;|&amp;)|([{}()[\]])/gm;

    let result = "";
    let lastIndex = 0;
    let match;
    
    while ((match = regex.exec(escapedCode)) !== null) {
        if (match.index > lastIndex) {
            result += escapedCode.substring(lastIndex, match.index);
        }
        
        let token = match[0];
        if (match[1]) result += `<span class="hl-comment">${token}</span>`;
        else if (match[2]) result += `<span class="hl-string">${token}</span>`;
        else if (match[3]) result += `<span class="hl-preprocessor">${token}</span>`;
        else if (match[4]) result += `<span class="hl-keyword">${token}</span>`;
        else if (match[5]) result += `<span class="hl-function">${token}</span>`;
        else if (match[6]) result += `<span class="hl-number">${token}</span>`;
        else if (match[7]) result += `<span class="hl-operator">${token}</span>`;
        else if (match[8]) result += `<span class="hl-bracket">${token}</span>`;
        
        lastIndex = regex.lastIndex;
    }
    
    if (lastIndex < escapedCode.length) {
        result += escapedCode.substring(lastIndex);
    }
    
    return result;
}

function syncHighlight() {
    const editor = document.getElementById("code-editor");
    const highlight = document.getElementById("code-highlight-content");
    if (!editor || !highlight) return;
    
    highlight.innerHTML = highlightCCode(editor.value);
}
