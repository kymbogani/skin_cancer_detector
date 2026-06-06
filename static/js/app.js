let selectedFile = null;

// ─────────────────────────────
// Upload handling
// ─────────────────────────────
function triggerUpload() {
  document.getElementById("fileInput").click();
}

function handleFile(file) {
  if (!file) return;

  selectedFile = file;

  const reader = new FileReader();
  reader.onload = function (e) {
    const img = document.getElementById("previewImg");
    img.src = e.target.result;
    img.style.display = "block";

    document.getElementById("dzIdle").style.display = "none";
    document.getElementById("changeBtn").style.display = "block";
    document.getElementById("analyzeBtn").disabled = false;
  };

  reader.readAsDataURL(file);
}

function resetUpload(event) {
  event.stopPropagation();

  selectedFile = null;

  document.getElementById("previewImg").style.display = "none";
  document.getElementById("dzIdle").style.display = "block";
  document.getElementById("changeBtn").style.display = "none";
  document.getElementById("analyzeBtn").disabled = true;

  document.getElementById("fileInput").value = "";
  document.getElementById("cameraInput").value = "";
}

function resetAll() {
  resetUpload({ stopPropagation: () => {} });

  document.getElementById("resultPanel").style.display = "none";
  document.getElementById("emptyPanel").style.display = "block";
}

// ─────────────────────────────
// Send to Flask backend
// ─────────────────────────────
async function analyze() {
  if (!selectedFile) return;

  const formData = new FormData();
  formData.append("image", selectedFile);

  // UI loading state
  document.getElementById("loadingWrap").style.display = "block";
  document.getElementById("analyzeBtn").disabled = true;

  try {
    const res = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    document.getElementById("loadingWrap").style.display = "none";

    if (data.error) {
      alert(data.error);
      document.getElementById("analyzeBtn").disabled = false;
      return;
    }

    showResult(data);

  } catch (err) {
    document.getElementById("loadingWrap").style.display = "none";
    alert("Server error: " + err.message);
    document.getElementById("analyzeBtn").disabled = false;
  }
}

// ─────────────────────────────
// Show result in UI
// ─────────────────────────────
function showResult(data) {
  document.getElementById("emptyPanel").style.display = "none";
  document.getElementById("resultPanel").style.display = "block";

  document.getElementById("resultName").innerText = data.prediction;
  document.getElementById("resultRisk").innerText = data.risk;
  document.getElementById("confNum").innerText = data.confidence + "%";
  document.getElementById("resultDesc").innerText = data.desc || "";
  document.getElementById("adviceBox").innerText = data.advice || "";
  document.getElementById("disclaimer").innerText = data.disclaimer || "";

  // icon
  const icon = document.getElementById("resultIcon");
  icon.innerText = data.icon || "🧠";
  icon.style.background = data.color || "#eee";
  icon.style.color = "#fff";

  // risk color
  document.getElementById("resultRisk").style.color = data.color;

  // bars
  const container = document.getElementById("barsContainer");
  container.innerHTML = "";

  const scores = data.all_scores || {};

  Object.entries(scores).forEach(([label, value]) => {
    const row = document.createElement("div");
    row.className = "bar-row";

    row.innerHTML = `
      <div class="bar-meta">
        <span class="bar-name">${label}</span>
        <span class="bar-pct">${value}%</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width:${value}% ; background:${data.color}"></div>
      </div>
    `;

    container.appendChild(row);
  });

  // animate bars
  setTimeout(() => {
    document.querySelectorAll(".bar-fill").forEach(bar => {
      bar.style.width = bar.style.width;
    });
  }, 100);
}