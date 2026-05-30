// ==============================================================
// DOM型XSS (应被 rule8: xss-dom-location 检测)
// CWE-79: Cross-Site Scripting
// ==============================================================

// --- 变体1: location.hash (核心规则匹配) ---
function unsafe_hash_xss() {
    var hash = location.hash;  // 触发 rule8: location.hash
    document.getElementById("content").innerHTML = hash.substring(1);
}


// --- 变体2: location.search ---
function unsafe_search_xss() {
    var params = new URLSearchParams(location.search);
    var name = params.get("name");
    document.write("<h1>Hello " + name + "</h1>");  // DOM XSS
}


// --- 变体3: location.href ---
function unsafe_href_xss() {
    var url = location.href;
    var parts = url.split("#");
    document.getElementById("msg").innerHTML = parts[1];  // DOM XSS
}


// --- 变体4: document.referrer ---
function unsafe_referrer_xss() {
    var ref = document.referrer;
    if (ref) {
        document.write("来自: " + ref);  // DOM XSS
    }
}


// --- 变体5: postMessage ---
window.addEventListener("message", function(event) {
    document.getElementById("output").innerHTML = event.data;  // DOM XSS (postMessage)
});
