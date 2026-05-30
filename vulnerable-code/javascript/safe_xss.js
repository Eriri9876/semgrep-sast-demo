// ==============================================================
// 安全的XSS防护写法 (负样本 - 不应被DOM XSS规则误报)
// ==============================================================

// --- 安全写法1: textContent ---
function safe_textContent() {
    var hash = location.hash.substring(1);
    document.getElementById("content").textContent = hash;  // textContent 自动转义
}


// --- 安全写法2: DOMPurify 净化 ---
function safe_dompurify() {
    var userHTML = location.hash.substring(1);
    // var clean = DOMPurify.sanitize(userHTML);
    // document.getElementById("output").innerHTML = clean;
}


// --- 安全写法3: 白名单标签 ---
function safe_whitelist() {
    var allowed = ["b", "i", "em", "strong"];
    var userInput = location.hash.substring(1);
    var sanitized = userInput.replace(/<\/?[^>]+(>|$)/g, "");
    document.getElementById("output").textContent = sanitized;
}


// --- 安全写法4: encodeURIComponent ---
function safe_encode() {
    var name = new URLSearchParams(location.search).get("name");
    var safeName = encodeURIComponent(name);
    document.getElementById("greeting").textContent = decodeURIComponent(safeName);
}


// --- 安全写法5: CSP + 安全DOM操作 ---
function safe_csp() {
    // 使用 createElement + textContent
    var hash = location.hash.substring(1);
    var div = document.createElement("div");
    div.textContent = hash;
    document.body.appendChild(div);
}
